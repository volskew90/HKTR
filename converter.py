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
        
    def map_value(self, category, value, default=None):
        """通用映射函数，支持默认值"""
        if default is None:
            default = value
        return self.mappings.get(category, {}).get(value, default)

    def format_amount(self, value, precision=5):
        """格式化金额，确保精度符合 Num(x, precision)"""
        try:
            return round(float(value), precision)
        except (ValueError, TypeError):
            return 0.0

    def truncate_string(self, value, length=35):
        """截断字符串，符合 Varchar(length) 限制"""
        if not value:
            return ""
        val_str = str(value)
        return val_str[:length] if len(val_str) > length else val_str

    def validate_xml(self, xml_path, xsd_path):
        """增强的校验反馈：尝试定位错误节点"""
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
                # 增强反馈：提取错误路径
                print(f"  [ERROR] 行号 {error.line}: {error.message}")
                if "pattern" in error.message.lower():
                    print(f"    💡 提示: 该字段的值可能不符合正则表达式约束 (例如 LEI/UTI 格式错误)。")
            return False
        except Exception as e:
            print(f"💥 发生错误: {e}")
            return False

    def _build_counterparty_data(self, row):
        """子函数：构建交易对手报送块 (CP1, CP2, Submitting Agent)"""
        # 模拟 LEI，实际应从映射或 CSV 获取
        lei_cp1 = self.truncate_string(self.map_value('entities', 'MyOrg', '12345678901234567801'), 20)
        lei_cp2 = self.truncate_string(row.get('Counterparty_LEI', '98765432109876543202'), 20)
        
        # 1. Reporting Counterparty
        rptg_id = OrganisationIdentification15Choice1(lei=lei_cp1)
        rptg_lgl = LegalPersonIdentification11(id=rptg_id)
        rptg_pty = PartyIdentification248Choice1(lgl=rptg_lgl)
        
        # 动态转换方向 (Buy/Sell -> BYER/SLLR)
        direction_val = self.map_value('direction', row.get('Direction'), 'BYER')
        rptg_drctn = Direction4Choice1(ctr_pty_sd=OptionParty1Code(direction_val))
        rptg_ctr_pty = Counterparty451(id=rptg_pty, drctn_or_sd=rptg_drctn)
        
        # 2. Other Counterparty
        othr_id = OrganisationIdentification15Choice2(lei=lei_cp2)
        othr_lgl = LegalPersonIdentification12(id=othr_id)
        othr_pty = PartyIdentification248Choice2(lgl=othr_lgl)
        othr_ctr_pty = Counterparty461(id_tp=othr_pty)
        
        # 3. Submitting Agent & Responsible Entity
        submit_agent = OrganisationIdentification15Choice4(lei=lei_cp1)
        resp_id = OrganisationIdentification15Choice1(lei=lei_cp1)
        
        ctr_pty = TradeCounterpartyReport201(
            rptg_ctr_pty=rptg_ctr_pty,
            othr_ctr_pty=othr_ctr_pty,
            submitg_agt=submit_agent,
            ntty_rspnsbl_for_rpt=resp_id
        )
        return CounterpartySpecificData361(ctr_pty=ctr_pty)

    def _build_transaction_details(self, row):
        """子函数：根据资产类别构建复杂的交易详情"""
        # UTI 校验与截断
        uti = self.truncate_string(row.get('UTI', 'UTI123456789012345601TRADEIDABC123'), 52)
        tx_id_choice = UniqueTransactionIdentifier2Choice1(unq_tx_idr=uti)
        
        # 金额与精度处理
        price_val = self.format_amount(row.get('Price', 0))
        currency = self.map_value('currencies', row.get('Currency'), 'HKD')
        
        amt_dir = AmountAndDirection1062(
            amt=ActiveOrHistoricCurrencyAnd5DecimalAmount(value=price_val, ccy=currency)
        )
        ntnl_amt = NotionalAmountLegs51(frst_leg=NotionalAmount51(amt=amt_dir))
        
        # 时间戳处理
        now = datetime.now()
        exctn_tm = XmlDateTime(now.year, now.month, now.day, now.hour, now.minute, now.second)
        
        # 构建非清算详情
        no_reason = ClearingExceptionOrExemption3Choice1(rsn=NoReasonCode.NORE)
        trad_clr = TradeClearing111(clr_sts=Cleared23Choice1(non_clrd=no_reason))
        
        return TradeTransaction501(
            tx_id=tx_id_choice,
            coll_prtfl_cd=CollateralPortfolioCode6Choice1(mrgn_prtfl_cd=MarginPortfolio41()),
            ntnl_amt=ntnl_amt,
            exctn_tm_stmp=exctn_tm,
            xprtn_dt=XmlDate(now.year + 1, now.month, now.day),
            deriv_evt=DerivativeEvent61(
                tp=DerivativeEventType3Code1.TRAD, 
                tm_stmp=DateAndDateTime2Choice1(dt_tm=exctn_tm)
            ),
            trad_clr=trad_clr
        )

    def convert_row_to_doc(self, row):
        """主转换入口：组装所有模块"""
        # 1. 动态获取资产类别映射
        asset_class = self.map_value('asset_classes', row.get('AssetClass'), 'SWAP')
        
        ctrct_data = ContractType151(
            ctrct_tp=FinancialInstrumentContractType2Code(asset_class),
            asst_clss=ProductType4Code1.CURR
        )
        
        common_data = CommonTradeDataReport711(
            ctrct_data=ctrct_data,
            tx_data=self._build_transaction_details(row)
        )
        
        tech_attr = TechnicalAttributes51(tech_rcrd_id=f"REC_{self.truncate_string(row.get('Trade_ID'), 10)}")
        
        new_trade = TradeData431(
            ctr_pty_spcfc_data=self._build_counterparty_data(row),
            cmon_trad_data=common_data,
            tech_attrbts=tech_attr
        )
        
        trad_data = TradeData59Choice1(rpt=[TradeReport33Choice1(new=new_trade)])
        deriv_rpt = DerivativesTradeReportV04(rpt_hdr=TradeReportHeader41(nb_rcrds=1), trad_data=trad_data)
        
        return Document(derivs_trad_rpt=deriv_rpt)

    def save_xml(self, document, output_path):
        xml_content = self.serializer.render(document)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)

if __name__ == "__main__":
    converter = HKTRConverter()
    input_file = 'input.csv'
    xsd_file = 'assets/auth_030_001_04_HKMAUG_DATTAR.xsd'
    
    try:
        df = pd.read_csv(input_file)
        print(f"🚀 [V2] 开始处理 CSV，共 {len(df)} 条记录...")
        
        for index, row in df.iterrows():
            trade_id = str(row.get('Trade_ID', index))
            doc_obj = converter.convert_row_to_doc(row)
            
            output_file = f"HKTR_V2_{trade_id}.xml"
            converter.save_xml(doc_obj, output_file)
            
            if converter.validate_xml(output_file, xsd_file):
                print(f"✅ 记录 {index+1}: 成功 -> {output_file}")
            else:
                print(f"⚠️ 记录 {index+1}: 校验失败 -> {output_file}")
                
        print("\n✨ 处理完毕！")
    except Exception as e:
        import traceback
        traceback.print_exc()
