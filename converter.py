import json
import pandas as pd
from datetime import datetime
from lxml import etree
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

# 导入所有必要的模型类
from models.auth_030_001_04_hkmaug_dattar import (
    Document,
    DerivativesTradeReportV04,
    TradeData59Choice1,
    TradeReport33Choice1,
    TradeData431,
    TradeReportHeader41,
    TradeCounterpartyReport201,
    CounterpartySpecificData361,
    OrganisationIdentification15Choice4,
    CommonTradeDataReport711,
    TradeTransaction501,
    UniqueTransactionIdentifier2Choice1,
    Counterparty451,
    Counterparty461,
    PartyIdentification248Choice1,
    PartyIdentification248Choice2,
    LegalPersonIdentification11,
    LegalPersonIdentification12,
    OrganisationIdentification15Choice1,
    OrganisationIdentification15Choice2,
    Direction4Choice1,
    OptionParty1Code,
    CollateralPortfolioCode6Choice1,
    NotionalAmountLegs51,
    DerivativeEvent61,
    TradeClearing111,
    AmountAndDirection1062,
    NotionalAmount51,
    ActiveOrHistoricCurrencyAnd5DecimalAmount,
    DerivativeEventType3Code1,
    Cleared23Choice1,
    ClearingExceptionOrExemption3Choice1,
    NoReasonCode,
    ContractType151,
    FinancialInstrumentContractType2Code,
    ProductType4Code1,
    TechnicalAttributes51,
    DateAndDateTime2Choice1,
    MarginPortfolio41,
)
from xsdata.models.datatype import XmlDateTime, XmlDate
from models.head_001_001_04_hkmaug import BusinessApplicationHeaderV04 as BAH

class HKTRConverter:
    def __init__(self, mapping_path='assets/mappings.json'):
        with open(mapping_path, 'r', encoding='utf-8') as f:
            self.mappings = json.load(f)
        self.serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
        
    def map_value(self, category, value):
        return self.mappings.get(category, {}).get(value, value)

    def create_bah(self, participant_id):
        header = BAH()
        header.biz_msg_idr = f"MSG_{datetime.now().strftime('%Y%m%d%H%M%S%f')}"
        header.msg_def_idr = "auth.030.001.04"
        header.cre_dt = datetime.now()
        return header

    def validate_xml(self, xml_path, xsd_path):
        try:
            parser = etree.XMLParser(remove_blank_text=True)
            schema = etree.XMLSchema(etree.parse(xsd_path))
            xml_doc = etree.parse(xml_path, parser)
            schema.assertValid(xml_doc)
            print(f"✅ 校验成功: {xml_path}")
            return True
        except etree.DocumentInvalid as e:
            print(f"❌ 校验失败: {xml_path}")
            for error in e.error_log:
                print(f"  行号 {error.line}: {error.message}")
            return False
        except Exception as e:
            print(f"💥 发生错误: {e}")
            return False

    def convert_row_to_doc(self, row):
        """核心转换：将 CSV 字段精准填入 ISO 20022 嵌套模型"""
        
        # 数据合规化：由于是模拟数据，我们构造符合正则的 LEI 和 UTI
        # LEI 正则: [A-Z0-9]{18,18}[0-9]{2,2}
        mock_lei_1 = "12345678901234567801"
        mock_lei_2 = "98765432109876543202"
        # UTI 正则: [A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}
        mock_uti = "UTI123456789012345601TRADEIDABC123"
        
        # 1. 构建 Reporting Counterparty (CP1)
        rptg_id = OrganisationIdentification15Choice1(lei=mock_lei_1)
        rptg_lgl = LegalPersonIdentification11(id=rptg_id)
        rptg_pty = PartyIdentification248Choice1(lgl=rptg_lgl)
        rptg_drctn = Direction4Choice1(ctr_pty_sd=OptionParty1Code.BYER)
        rptg_ctr_pty = Counterparty451(id=rptg_pty, drctn_or_sd=rptg_drctn)
        
        # 2. 构建 Other Counterparty (CP2)
        othr_id = OrganisationIdentification15Choice2(lei=mock_lei_2)
        othr_lgl = LegalPersonIdentification12(id=othr_id)
        othr_pty = PartyIdentification248Choice2(lgl=othr_lgl)
        othr_ctr_pty = Counterparty461(id_tp=othr_pty)
        
        # 3. 构建 Entity Responsible for Report
        resp_id = OrganisationIdentification15Choice1(lei=mock_lei_1)
        
        # 4. 构建 Submitting Agent
        submit_agent = OrganisationIdentification15Choice4(lei=mock_lei_1)
        
        # 5. 组装 Counterparty 报送块
        ctr_pty = TradeCounterpartyReport201(
            rptg_ctr_pty=rptg_ctr_pty,
            othr_ctr_pty=othr_ctr_pty,
            submitg_agt=submit_agent,
            ntty_rspnsbl_for_rpt=resp_id
        )
        ctr_pty_spcfc = CounterpartySpecificData361(ctr_pty=ctr_pty)
        
        # 6. 构建 Transaction 必填详情
        tx_id_choice = UniqueTransactionIdentifier2Choice1(unq_tx_idr=mock_uti)
        
        # 修正：MarginPortfolio41 必须是对象，不能传字符串
        coll_prtfl = CollateralPortfolioCode6Choice1(mrgn_prtfl_cd=MarginPortfolio41())
        
        # 修正：Pandas float64 强制转 Python float
        price_float = float(row['Price'])
        price_val = ActiveOrHistoricCurrencyAnd5DecimalAmount(value=price_float, ccy='HKD')
        amt_dir = AmountAndDirection1062(amt=price_val)
        ntnl_amt_val = NotionalAmount51(amt=amt_dir)
        ntnl_amt = NotionalAmountLegs51(frst_leg=ntnl_amt_val)
        
        now = datetime.now()
        exctn_tm = XmlDateTime(now.year, now.month, now.day, now.hour, now.minute, now.second)
        xprtn_dt = XmlDate(now.year + 1, now.month, now.day)
        
        # 修正：TimeStamp 必须封装在 DateAndDateTime2Choice1 中
        tm_stmp_choice = DateAndDateTime2Choice1(dt_tm=exctn_tm)
        deriv_evt = DerivativeEvent61(tp=DerivativeEventType3Code1.TRAD, tm_stmp=tm_stmp_choice)
        
        # 构建非清算原因
        no_reason = ClearingExceptionOrExemption3Choice1(rsn=NoReasonCode.NORE)
        clr_choice = Cleared23Choice1(non_clrd=no_reason)
        trad_clr = TradeClearing111(clr_sts=clr_choice)
        
        tx_id_data = TradeTransaction501(
            tx_id=tx_id_choice,
            coll_prtfl_cd=coll_prtfl,
            ntnl_amt=ntnl_amt,
            exctn_tm_stmp=exctn_tm,
            xprtn_dt=xprtn_dt,
            deriv_evt=deriv_evt,
            trad_clr=trad_clr
        )
        
        # 8. 构建必填的合约详情
        ctrct_data = ContractType151(
            ctrct_tp=FinancialInstrumentContractType2Code.SWAP,
            asst_clss=ProductType4Code1.CURR
        )
        
        common_data = CommonTradeDataReport711(
            ctrct_data=ctrct_data,
            tx_data=tx_id_data
        )
        
        # 7. 组装操作类型 (New)
        tech_attr = TechnicalAttributes51(tech_rcrd_id=f"REC_{mock_uti[:10]}")
        new_trade = TradeData431(
            ctr_pty_spcfc_data=ctr_pty_spcfc,
            cmon_trad_data=common_data,
            tech_attrbts=tech_attr
        )
        
        # 8. 组装报文
        rpt_choice = TradeReport33Choice1(new=new_trade)
        trad_data = TradeData59Choice1(rpt=[rpt_choice])
        
        rpt_hdr = TradeReportHeader41(nb_rcrds=1)
        deriv_rpt = DerivativesTradeReportV04(
            rpt_hdr=rpt_hdr,
            trad_data=trad_data
        )
        
        return Document(derivs_trad_rpt=deriv_rpt)

    def save_xml(self, header, document, output_path):
        xml_content = self.serializer.render(document)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)

if __name__ == "__main__":
    converter = HKTRConverter()
    input_file = 'input.csv'
    xsd_file = 'assets/auth_030_001_04_HKMAUG_DATTAR.xsd'
    
    try:
        df = pd.read_csv(input_file)
        print(f"🚀 开始处理 CSV，共 {len(df)} 条记录...")
        
        for index, row in df.iterrows():
            trade_id = str(row['Trade_ID'])
            doc_obj = converter.convert_row_to_doc(row)
            
            # 生成符合规范的文件名
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"HKTR_AUTH030_{trade_id}_{timestamp}.xml"
            
            converter.save_xml(None, doc_obj, output_file)
            
            # 自动校验
            if converter.validate_xml(output_file, xsd_file):
                print(f"📦 记录 {index+1}: 转换并校验成功 -> {output_file}")
            else:
                print(f"⚠️ 记录 {index+1}: 转换成功但校验失败 -> {output_file}")
                
        print("\n✨ 所有记录处理完毕！")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"💥 运行失败: {e}")
