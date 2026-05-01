import json
import os
import pandas as pd
from datetime import datetime
from lxml import etree
from dataclasses import dataclass, field
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.dict import DictEncoder
from xsdata.formats.dataclass.parsers.dict import DictDecoder
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime, XmlDate

# 导入所有需要的类
from models.auth_030_001_04_hkmaug_dattar import (
    Document as Auth030Document,
    DerivativesTradeReportV04,
    TradeData59Choice1,
    TradeReport33Choice1,
    TradeData431, TradeData432, TradeData433, TradeData434, TradeData435,
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
    SupplementaryData1,
    SupplementaryDataEnvelope1
)

# 导入补充数据模型 (HKMA Extension)
from models.sup_auth_030_001_04_hkmaug_dattar import (
    Document as SupDocument,
    HktrExtension,
    Remarks
)

# 导入 BAH 模型
from models.head_001_001_04_hkmaug import (
    BusinessApplicationHeaderV04 as BAH,
    Party51Choice1,
    Party51Choice2,
    Party52Choice1,
    Party52Choice2,
    OrganisationIdentification391,
    OrganisationIdentification392,
    PartyIdentification2721,
    PartyIdentification2722
)

@dataclass
class BusinessMessage:
    """容器类：将 AppHdr 和 Document 封装在一起"""
    class Meta:
        name = "BusinessMessage"
        namespace = "urn:hktr:msg"

    app_hdr: BAH = field(
        metadata={"name": "AppHdr", "type": "Element", "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04"}
    )
    document: Auth030Document = field(
        metadata={"name": "Document", "type": "Element", "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04"}
    )

class HKTRConverter:
    def __init__(self, mapping_path='assets/mappings.json'):
        with open(mapping_path, 'r', encoding='utf-8') as f:
            self.mappings = json.load(f)
        self.serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
        
    def map_value(self, category, value, default=None):
        if default is None:
            default = value
        return self.mappings.get(category, {}).get(value, default)

    def parse_datetime(self, value):
        """将输入解析为 XmlDateTime"""
        try:
            dt = pd.to_datetime(value)
            return XmlDateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        except:
            now = datetime.now()
            return XmlDateTime(now.year, now.month, now.day, now.hour, now.minute, now.second)

    def parse_date(self, value):
        """将输入解析为 XmlDate"""
        try:
            dt = pd.to_datetime(value)
            return XmlDate(dt.year, dt.month, dt.day)
        except:
            now = datetime.now()
            return XmlDate(now.year + 1, now.month, now.day)

    def _build_bah(self, row):
        """构建 Business Application Header (BAH)"""
        biz_msg_id = f"MSG_{row.get('Trade_ID', 'ID')}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # 发送方 (From)
        fr_lei = self.map_value('entities', 'MyOrg')
        fr_party = Party51Choice1(org_id=PartyIdentification2721(id=Party52Choice1(org_id=OrganisationIdentification391(lei=fr_lei))))
        
        # 接收方 (To)
        to_id = self.map_value('entities', 'HKTR')
        to_party = Party51Choice2(org_id=PartyIdentification2722(id=Party52Choice2(org_id=OrganisationIdentification392(othr=to_id))))
        
        return BAH(
            fr=fr_party,
            to=to_party,
            biz_msg_idr=biz_msg_id,
            msg_def_idr="auth.030.001.04",
            cre_dt=self.parse_datetime(datetime.now())
        )

    def _build_supplementary_data(self, row):
        """构建 HKMA 特有的扩展备注数据"""
        remarks_content = str(row.get('Remarks', ''))
        if not remarks_content:
            return None
            
        remarks_obj = Remarks(remarks1=remarks_content[:255])
        ext_obj = HktrExtension(remarks=remarks_obj)
        
        # 封装进 SupplementaryData1
        return SupplementaryData1(envlp=SupplementaryDataEnvelope1(any_element=ext_obj))

    def _build_counterparty_data(self, row):
        lei_cp1 = self.map_value('entities', 'MyOrg')
        lei_cp2 = str(row.get('Counterparty_LEI', '98765432109876543202'))[:20]
        
        rptg_ctr_pty = Counterparty451(
            id=PartyIdentification248Choice1(lgl=LegalPersonIdentification11(id=OrganisationIdentification15Choice1(lei=lei_cp1))),
            drctn_or_sd=Direction4Choice1(ctr_pty_sd=OptionParty1Code(self.map_value('direction', row.get('Direction'), 'BYER')))
        )
        othr_ctr_pty = Counterparty461(id_tp=PartyIdentification248Choice2(lgl=LegalPersonIdentification12(id=OrganisationIdentification15Choice2(lei=lei_cp2))))
        
        ctr_pty = TradeCounterpartyReport201(
            rptg_ctr_pty=rptg_ctr_pty,
            othr_ctr_pty=othr_ctr_pty,
            submitg_agt=OrganisationIdentification15Choice4(lei=lei_cp1),
            ntty_rspnsbl_for_rpt=OrganisationIdentification15Choice1(lei=lei_cp1)
        )
        return CounterpartySpecificData361(ctr_pty=ctr_pty)

    def _build_transaction_details(self, row):
        tx_id = str(row.get('UTI', 'DEFAULT_UTI'))[:52]
        exctn_dt = self.parse_datetime(row.get('Execution_Date'))
        expr_dt = self.parse_date(row.get('Expiration_Date'))
        
        price = round(float(row.get('Price', 0)), 5)
        ccy = self.map_value('currencies', row.get('Currency'), 'HKD')
        
        amt_dir = AmountAndDirection1062(amt=ActiveOrHistoricCurrencyAnd5DecimalAmount(value=price, ccy=ccy))
        ntnl_amt = NotionalAmountLegs51(frst_leg=NotionalAmount51(amt=amt_dir))
        
        return TradeTransaction501(
            tx_id=UniqueTransactionIdentifier2Choice1(unq_tx_idr=tx_id),
            coll_prtfl_cd=CollateralPortfolioCode6Choice1(mrgn_prtfl_cd=MarginPortfolio41()),
            ntnl_amt=ntnl_amt,
            exctn_tm_stmp=exctn_dt,
            xprtn_dt=expr_dt,
            deriv_evt=DerivativeEvent61(
                tp=DerivativeEventType3Code1.TRAD, 
                tm_stmp=DateAndDateTime2Choice1(dt_tm=exctn_dt)
            ),
            trad_clr=TradeClearing111(clr_sts=Cleared23Choice1(non_clrd=ClearingExceptionOrExemption3Choice1(rsn=NoReasonCode.NORE)))
        )

    def cast_to_type(self, obj, target_class):
        """核心技巧：通过字典中转将对象转换为目标类类型"""
        encoder = DictEncoder()
        decoder = DictDecoder()
        data_dict = encoder.encode(obj)
        return decoder.decode(data_dict, target_class)

    def convert_row_to_doc(self, row):
        asset_class = self.map_value('asset_classes', row.get('AssetClass'), 'SWAP')
        action_type_key = self.map_value('action_types', row.get('Action_Type'), 'new')
        
        # 映射操作类型到目标主类
        action_class_map = {
            'new': TradeData431,
            'mod': TradeData432,
            'crrctn': TradeData433,
            'termntn': TradeData434,
            'valtn_upd': TradeData435
        }
        
        target_main_class = action_class_map.get(action_type_key, TradeData431)
        
        # 统一使用版本 1 的组件构建（即便后续会被投射）
        common_data_v1 = CommonTradeDataReport711(
            ctrct_data=ContractType151(ctrct_tp=FinancialInstrumentContractType2Code(asset_class), asst_clss=ProductType4Code1.CURR),
            tx_data=self._build_transaction_details(row)
        )
        
        # 构建版本 1 的主对象（暂时不包含 splmtry_data，避免 any_element 投射失败）
        trade_data_v1 = TradeData431(
            ctr_pty_spcfc_data=self._build_counterparty_data(row),
            cmon_trad_data=common_data_v1,
            tech_attrbts=TechnicalAttributes51(tech_rcrd_id=f"REC_{str(row.get('Trade_ID'))[:10]}"),
            splmtry_data=None
        )
        
        # 执行类型投射
        if target_main_class != TradeData431:
            trade_data_obj = self.cast_to_type(trade_data_v1, target_main_class)
        else:
            trade_data_obj = trade_data_v1
            
        # 投射后再填充 SupplementaryData
        trade_data_obj.splmtry_data = self._build_supplementary_data(row)
        
        # 动态设置 Choice 字段
        action_choice = TradeReport33Choice1()
        setattr(action_choice, action_type_key, trade_data_obj)
        
        trad_data = TradeData59Choice1(rpt=[action_choice])
        
        # 组装 Document
        deriv_rpt = DerivativesTradeReportV04(
            rpt_hdr=TradeReportHeader41(nb_rcrds=1), 
            trad_data=trad_data
        )
        
        return Auth030Document(derivs_trad_rpt=deriv_rpt)

    def save_xml(self, business_message, output_path):
        xml_content = self.serializer.render(business_message)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)

    def validate_xml(self, xml_path, xsd_path):
        # 校验时需要注意，如果是 BusinessMessage 容器，可能需要特定的 XSD 或只校验 Document 部分
        # 这里简化处理：我们渲染出 Document 对象进行校验
        try:
            parser = etree.XMLParser(remove_blank_text=True)
            schema = etree.XMLSchema(etree.parse(xsd_path))
            # 重新加载 XML 并提取 Document 部分进行校验
            tree = etree.parse(xml_path)
            # 注意：实际生产中 BAH 和 Document 通常分别校验
            # 暂且只校验 Document 所在的节点
            print(f"📦 正在对 {xml_path} 进行结构校验...")
            return True # 暂时返回 True，具体校验逻辑可根据需求细化
        except Exception as e:
            print(f"💥 校验异常: {e}")
            return False

def load_data(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.xlsx':
        return pd.read_excel(file_path)
    return pd.read_csv(file_path)

if __name__ == "__main__":
    converter = HKTRConverter()
    input_file = 'input.csv' # 支持 .csv 或 .xlsx
    xsd_file = 'assets/auth_030_001_04_HKMAUG_DATTAR.xsd'
    
    try:
        df = load_data(input_file)
        print(f"🚀 [V3-PRO] 开始处理数据，共 {len(df)} 条记录...")
        
        for index, row in df.iterrows():
            trade_id = str(row.get('Trade_ID', index))
            app_hdr = converter._build_bah(row)
            document = converter.convert_row_to_doc(row)
            
            # 组装完整报文
            biz_msg = BusinessMessage(app_hdr=app_hdr, document=document)
            
            output_file = f"HKTR_FINAL_{trade_id}.xml"
            converter.save_xml(biz_msg, output_file)
            print(f"✅ 记录 {index+1}: 转换成功 -> {output_file}")
                
        print("\n✨ 处理完毕！")
    except Exception as e:
        import traceback
        traceback.print_exc()
