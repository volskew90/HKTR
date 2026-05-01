from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from xsdata.models.datatype import XmlDate, XmlDateTime

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04"


@dataclass(kw_only=True)
class ActiveOrHistoricCurrencyAnd13DecimalAmount:
    """
    ActiveOrHistoricCurrencyAnd13DecimalAmount A number of monetary units
    specified in an active or a historic currency where the unit of
    currency is explicit and compliant with ISO 4217.

    The number of fractional digits (or minor unit of currency) is not
    checked as per ISO 4217: It must be lesser than or equal to 13. Note:
    The decimal separator is a dot.

    :ivar value:
    :ivar ccy: Currency Medium of exchange of value.
    """

    value: Decimal = field(
        metadata={
            "min_inclusive": Decimal("0"),
            "total_digits": 18,
            "fraction_digits": 13,
        }
    )
    ccy: str = field(
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "pattern": r"[A-Z]{3,3}",
        }
    )


@dataclass(kw_only=True)
class ActiveOrHistoricCurrencyAnd5DecimalAmount:
    """
    ActiveOrHistoricCurrencyAnd5DecimalAmount A number of monetary units
    specified in an active or a historic currency where the unit of
    currency is explicit and compliant with ISO 4217.

    :ivar value:
    :ivar ccy: Currency Medium of exchange of value.
    """

    value: Decimal = field(
        metadata={
            "min_inclusive": Decimal("0"),
            "total_digits": 25,
            "fraction_digits": 5,
        }
    )
    ccy: str = field(
        metadata={
            "name": "Ccy",
            "type": "Attribute",
            "pattern": r"[A-Z]{3,3}",
        }
    )


class AssetClassDetailedSubProductType10Code(Enum):
    """
    AssetClassDetailedSubProductType10Code Further sub product code list
    for commodity derivative Non-Precious.

    :cvar ALUM: Aluminium Commodity attribute of type aluminium.
    :cvar ALUA: AluminiumAlloy Commodity attribute of type aluminium
        alloy.
    :cvar CBLT: Cobalt Commodity attribute of type cobalt.
    :cvar COPR: Copper Commodity attribute of type copper.
    :cvar IRON: IronOre Commodity attribute of type iron ore.
    :cvar MOLY: Molybdenum Commodity attribute of type molybdenum.
    :cvar NASC: NASAAC Commodity attribute of type NASAAC (North
        American Special Aluminum Alloy Contract).
    :cvar NICK: Nickel Commodity attribute of type nickel.
    :cvar STEL: Steel Commodity attribute of type steel.
    :cvar TINN: Tin Commodity attribute of type tin.
    :cvar ZINC: Zinc Commodity attribute of type zinc.
    :cvar OTHR: Other Commodity attribute of other type.
    :cvar LEAD: Lead Commodity attribute of type lead.
    """

    ALUM = "ALUM"
    ALUA = "ALUA"
    CBLT = "CBLT"
    COPR = "COPR"
    IRON = "IRON"
    MOLY = "MOLY"
    NASC = "NASC"
    NICK = "NICK"
    STEL = "STEL"
    TINN = "TINN"
    ZINC = "ZINC"
    OTHR = "OTHR"
    LEAD = "LEAD"


class AssetClassDetailedSubProductType11Code(Enum):
    """
    AssetClassDetailedSubProductType11Code Further sub product code list
    for commodity derivative Precious.

    :cvar GOLD: Gold Commodity attribute of type gold.
    :cvar OTHR: Other Commodity attribute of other type.
    :cvar PLDM: Palladium Commodity attribute of type palladium.
    :cvar PTNM: Platinum Commodity attribute of type platinum.
    :cvar SLVR: Silver Commodity attribute of type silver.
    """

    GOLD = "GOLD"
    OTHR = "OTHR"
    PLDM = "PLDM"
    PTNM = "PTNM"
    SLVR = "SLVR"


class AssetClassDetailedSubProductType1Code(Enum):
    """
    AssetClassDetailedSubProductType1Code Further sub product code list for
    commodity derivative Grains Oil Seeds.

    :cvar FWHT: FeedWheat Commodity attribute of type feed wheat.
    :cvar SOYB: Soybeans Commodity attribute of type soybeans.
    :cvar RPSD: Rapeseed Commodity attribute of type rapeseed.
    :cvar OTHR: Other Commodity attribute of other type.
    :cvar CORN: Maize Commodity attribute of type maize.
    :cvar RICE: Rice Commodity attribute of type rice.
    """

    FWHT = "FWHT"
    SOYB = "SOYB"
    RPSD = "RPSD"
    OTHR = "OTHR"
    CORN = "CORN"
    RICE = "RICE"


class AssetClassDetailedSubProductType29Code(Enum):
    """
    AssetClassDetailedSubProductType29Code Further sub product code list
    for commodity derivative Olive Oil.

    :cvar LAMP: Lampante Commodity attribute of type lampante.
    :cvar OTHR: Other Commodity attribute of other type.
    """

    LAMP = "LAMP"
    OTHR = "OTHR"


class AssetClassDetailedSubProductType2Code(Enum):
    """
    AssetClassDetailedSubProductType2Code Further sub product code list for
    commodity derivative Softs.

    :cvar ROBU: RobustaCoffee Commodity attribute of type robusta
        coffee.
    :cvar CCOA: Cocoa Commodity attribute of type cocoa.
    :cvar BRWN: RawSugar Commodity attribute of type raw sugar.
    :cvar WHSG: WhiteSugar Commodity attribute of type white sugar.
    :cvar OTHR: Other Commodity attribute of other type.
    """

    ROBU = "ROBU"
    CCOA = "CCOA"
    BRWN = "BRWN"
    WHSG = "WHSG"
    OTHR = "OTHR"


class AssetClassDetailedSubProductType30Code(Enum):
    """
    AssetClassDetailedSubProductType30Code Further sub product code list
    for commodity derivative Grain.

    :cvar MWHT: MillingWheat Commodity attribute of type milled wheat.
    :cvar OTHR: Other Commodity attribute of other type.
    """

    MWHT = "MWHT"
    OTHR = "OTHR"


class AssetClassDetailedSubProductType31Code(Enum):
    """
    AssetClassDetailedSubProductType31Code Further sub product code list
    for commodity derivative Natural Gas.

    :cvar GASP: GasPool Commodity attribute of type GASPOOL.
    :cvar LNGG: LNG Commodity attribute of type liquid natural gas.
    :cvar NCGG: NCG Commodity attribute of type NCG (NetConnect
        Germany).
    :cvar TTFG: TTF Commodity attribute of type TTF (Dutch Title
        Transfer Facility).
    :cvar NBPG: NBP Commodity attribute of type NBP (National Balancing
        Point).
    :cvar OTHR: Other Commodity attribute of other type.
    """

    GASP = "GASP"
    LNGG = "LNGG"
    NCGG = "NCGG"
    TTFG = "TTFG"
    NBPG = "NBPG"
    OTHR = "OTHR"


class AssetClassDetailedSubProductType32Code(Enum):
    """
    AssetClassDetailedSubProductType32Code Further sub product code list
    for commodity derivative Oil.

    :cvar BAKK: Bakken Commodity attribute of type bakken.
    :cvar BDSL: Biodiesel Commodity attribute of type biodiesel.
    :cvar BRNT: Brent Commodity attribute of type Brent.
    :cvar BRNX: BrentNX Commodity attribute of type Brent NX (New
        Expiry).
    :cvar CNDA: Canadian Commodity attribute of type canadian.
    :cvar COND: Condensate Commodity attribute of type condensate.
    :cvar DSEL: Diesel Commodity attribute of type diesel.
    :cvar DUBA: Dubai Commodity attribute of type Dubai.
    :cvar ESPO: ESPO Commodity attribute of type ESPO (Eastern Siberia
        Pacific Ocean).
    :cvar ETHA: Ethanol Commodity attribute of type ethanol.
    :cvar FUEL: Fuel Commodity attribute of type fuel.
    :cvar FOIL: FuelOil Commodity attribute of type fuel oil.
    :cvar GOIL: Gasoil Commodity attribute of type gasoil.
    :cvar GSLN: Gasoline Commodity attribute of type gasoline.
    :cvar HEAT: HeatingOil Commodity attribute of type heating oil.
    :cvar JTFL: JetFuel Commodity attribute of type jet fuel.
    :cvar KERO: Kerosene Commodity attribute of type kerosene.
    :cvar LLSO: LightLouisianaSweet Commodity attribute of type light
        Louisiana sweet (LLS).
    :cvar MARS: Mars Commodity attribute of type mars.
    :cvar NAPH: Naphta Commodity attribute of type naptha.
    :cvar NGLO: NGL Commodity attribute of type NGL (Natural Gas
        Liquids).
    :cvar TAPI: Tapis Commodity attribute of type tapis.
    :cvar WTIO: WTI Commodity attribute of type WTI (West Texas
        Intermediate).
    :cvar URAL: Urals Commodity attribute of type urals.
    :cvar OTHR: Other Commodity attribute of other type.
    """

    BAKK = "BAKK"
    BDSL = "BDSL"
    BRNT = "BRNT"
    BRNX = "BRNX"
    CNDA = "CNDA"
    COND = "COND"
    DSEL = "DSEL"
    DUBA = "DUBA"
    ESPO = "ESPO"
    ETHA = "ETHA"
    FUEL = "FUEL"
    FOIL = "FOIL"
    GOIL = "GOIL"
    GSLN = "GSLN"
    HEAT = "HEAT"
    JTFL = "JTFL"
    KERO = "KERO"
    LLSO = "LLSO"
    MARS = "MARS"
    NAPH = "NAPH"
    NGLO = "NGLO"
    TAPI = "TAPI"
    WTIO = "WTIO"
    URAL = "URAL"
    OTHR = "OTHR"


class AssetClassDetailedSubProductType33Code(Enum):
    """
    AssetClassDetailedSubProductType33Code Further sub product code list
    for commodity derivative Dry.

    :cvar DBCR: DryBulkCarrier Commodity attribute of type dry bulk
        carrier.
    :cvar OTHR: Other Commodity attribute of other type.
    """

    DBCR = "DBCR"
    OTHR = "OTHR"


class AssetClassDetailedSubProductType34Code(Enum):
    """
    AssetClassDetailedSubProductType34Code Further sub product code list
    for commodity derivative Wet.

    :cvar TNKR: Tanker Commodity attribute of type tanker.
    :cvar OTHR: Other Commodity attribute of other type.
    """

    TNKR = "TNKR"
    OTHR = "OTHR"


class AssetClassDetailedSubProductType5Code(Enum):
    """
    AssetClassDetailedSubProductType5Code Further sub product code list for
    commodity derivative Electricity.

    :cvar BSLD: BaseLoad Commodity attribute of type base load.
    :cvar FITR: FinancialTransmissionRights Commodity attribute of type
        financial transmission rights.
    :cvar PKLD: PeakLoad Commodity attribute of type peak load.
    :cvar OFFP: OffPeak Commodity attribute of type off-peak.
    :cvar OTHR: Other Commodity attribute of other type.
    """

    BSLD = "BSLD"
    FITR = "FITR"
    PKLD = "PKLD"
    OFFP = "OFFP"
    OTHR = "OTHR"


class AssetClassDetailedSubProductType8Code(Enum):
    """
    AssetClassDetailedSubProductType8Code Further sub product code list for
    commodity derivative Emissions.

    :cvar CERE: CER Commodity attribute of type emissions allowance CER
        (Certified Emission Reduction).
    :cvar ERUE: ERU Commodity attribute of type emissions allowance ERU
        (European Reduction Unit).
    :cvar EUAE: EUA Commodity attribute of type emissions allowance EUA
        (European Union Allowance).
    :cvar EUAA: EUAA Commodity attribute of type emissions allowance
        EUAA (European Union Aviation Allowance).
    :cvar OTHR: Other Commodity attribute of other type.
    """

    CERE = "CERE"
    ERUE = "ERUE"
    EUAE = "EUAE"
    EUAA = "EUAA"
    OTHR = "OTHR"


class AssetClassProductType11Code(Enum):
    """
    AssetClassProductType11Code Commodity derivative base product code list
    for Other C10.

    :cvar OTHC: OtherC10 Commodity of other type C10.
    """

    OTHC = "OTHC"


class AssetClassProductType12Code(Enum):
    """
    AssetClassProductType12Code Commodity derivative base product code list
    for Inflation.

    :cvar INFL: Inflation Commodity of type inflation.
    """

    INFL = "INFL"


class AssetClassProductType13Code(Enum):
    """
    AssetClassProductType13Code Commodity derivative base product code list
    for Multi Commodity Exotic.

    :cvar MCEX: MultiCommodityExotic Commodity of type multi commodity
        exotic.
    """

    MCEX = "MCEX"


class AssetClassProductType14Code(Enum):
    """
    AssetClassProductType14Code Commodity derivative base product code list
    for Official Economic Statistics.

    :cvar OEST: OfficialEconomicStatistic Commodity of type official
        economic statistic.
    """

    OEST = "OEST"


class AssetClassProductType15Code(Enum):
    """
    AssetClassProductType15Code Commodity derivative base product code list
    for Other.

    :cvar OTHR: Other Commodity of other type.
    """

    OTHR = "OTHR"


class AssetClassProductType16Code(Enum):
    """
    AssetClassProductType16Code Commodity derivative base product code list
    for Index.

    :cvar INDX: Index Index type of commodities.
    """

    INDX = "INDX"


class AssetClassProductType1Code(Enum):
    """
    AssetClassProductType1Code Commodity derivative base product code list
    for Agricultural.

    :cvar AGRI: Agricultural Commodity of type agricultural.
    """

    AGRI = "AGRI"


class AssetClassProductType2Code(Enum):
    """
    AssetClassProductType2Code Commodity derivative base product code list
    for Energy.

    :cvar NRGY: Energy Commodity of type energy.
    """

    NRGY = "NRGY"


class AssetClassProductType3Code(Enum):
    """
    AssetClassProductType3Code Commodity derivative base product code list
    for Environmental.

    :cvar ENVR: Environmental Commodity of type environmental.
    """

    ENVR = "ENVR"


class AssetClassProductType4Code(Enum):
    """
    AssetClassProductType4Code Commodity derivative base product code list
    for Freight.

    :cvar FRGT: Freight Commodity of type freight.
    """

    FRGT = "FRGT"


class AssetClassProductType5Code(Enum):
    """
    AssetClassProductType5Code Commodity derivative base product code list
    for Fertilizer.

    :cvar FRTL: Fertilizer Commodity of type fertilizer.
    """

    FRTL = "FRTL"


class AssetClassProductType6Code(Enum):
    """
    AssetClassProductType6Code Commodity derivative base product code list
    for Industrial Product.

    :cvar INDP: IndustrialProduct Commodity of type industrial product.
    """

    INDP = "INDP"


class AssetClassProductType7Code(Enum):
    """
    AssetClassProductType7Code Commodity derivative base product code list
    for Metal.

    :cvar METL: Metal Commodity of type metal.
    """

    METL = "METL"


class AssetClassProductType8Code(Enum):
    """
    AssetClassProductType8Code Commodity derivative base product code list
    for Paper.

    :cvar PAPR: Paper Commodity of type paper.
    """

    PAPR = "PAPR"


class AssetClassProductType9Code(Enum):
    """
    AssetClassProductType9Code Commodity derivative base product code list
    for Polypropylene.

    :cvar POLY: Polypropylene Commodity of type polypropylene.
    """

    POLY = "POLY"


class AssetClassSubProductType10Code(Enum):
    """
    AssetClassSubProductType10Code Defines the sub-product of type
    Emission.

    :cvar EMIS: Emission Commodity of type emission.
    """

    EMIS = "EMIS"


class AssetClassSubProductType15Code(Enum):
    """
    AssetClassSubProductType15Code Defines the sub-product of type Non
    Precious Metal.

    :cvar NPRM: NonPrecious Commodity of type non precious metals.
    """

    NPRM = "NPRM"


class AssetClassSubProductType16Code(Enum):
    """
    AssetClassSubProductType16Code Defines the sub-product of type Precious
    Metal.

    :cvar PRME: Precious Commodity of type precious metals.
    """

    PRME = "PRME"


class AssetClassSubProductType18Code(Enum):
    """
    AssetClassSubProductType18Code Defines the sub-product of type Plastic.

    :cvar PLST: Plastic Commodity of type plastic.
    """

    PLST = "PLST"


class AssetClassSubProductType1Code(Enum):
    """
    AssetClassSubProductType1Code Defines the sub-product of type Grain Oil
    Seeds.

    :cvar GROS: GrainOilSeeds Commodity of type grain oil seeds.
    """

    GROS = "GROS"


class AssetClassSubProductType20Code(Enum):
    """
    AssetClassSubProductType20Code Defines the sub-product of type Dairy.

    :cvar DIRY: Dairy Commodity of type dairy.
    """

    DIRY = "DIRY"


class AssetClassSubProductType21Code(Enum):
    """
    AssetClassSubProductType21Code Defines the sub-product of type
    Forestry.

    :cvar FRST: Forestry Commodity of type forestry.
    """

    FRST = "FRST"


class AssetClassSubProductType22Code(Enum):
    """
    AssetClassSubProductType22Code Defines the sub-product of type
    Livestock.

    :cvar LSTK: Livestock Commodity of type livestock.
    """

    LSTK = "LSTK"


class AssetClassSubProductType23Code(Enum):
    """
    AssetClassSubProductType23Code Defines the sub-product of type Seafood.

    :cvar SEAF: Seafood Commodity of type seafood.
    """

    SEAF = "SEAF"


class AssetClassSubProductType24Code(Enum):
    """
    AssetClassSubProductType24Code Defines the sub-product of type Coal.

    :cvar COAL: Coal Commodity of type coal.
    """

    COAL = "COAL"


class AssetClassSubProductType25Code(Enum):
    """
    AssetClassSubProductType25Code Defines the sub-product of type
    Distillates.

    :cvar DIST: Distillates Commodity of type distillates.
    """

    DIST = "DIST"


class AssetClassSubProductType26Code(Enum):
    """
    AssetClassSubProductType26Code Defines the sub-product of type Inter
    Energy.

    :cvar INRG: InterEnergy Commodity of type inter energy.
    """

    INRG = "INRG"


class AssetClassSubProductType27Code(Enum):
    """
    AssetClassSubProductType27Code Defines the sub-product of type Light
    Ends.

    :cvar LGHT: LightEnds Commodity of type light ends.
    """

    LGHT = "LGHT"


class AssetClassSubProductType28Code(Enum):
    """
    AssetClassSubProductType28Code Defines the sub-product of type
    Renewable Energy.

    :cvar RNNG: RenewableEnergy Commodity of type renewable energy.
    """

    RNNG = "RNNG"


class AssetClassSubProductType29Code(Enum):
    """
    AssetClassSubProductType29Code Defines the sub-product of type Carbon
    Related.

    :cvar CRBR: CarbonRelated Commodity of type carbon related.
    """

    CRBR = "CRBR"


class AssetClassSubProductType2Code(Enum):
    """
    AssetClassSubProductType2Code Defines the sub-product of type Softs.

    :cvar SOFT: Softs Commodity of type softs.
    """

    SOFT = "SOFT"


class AssetClassSubProductType30Code(Enum):
    """
    AssetClassSubProductType30Code Defines the sub-product of type Weather.

    :cvar WTHR: Weather Commodity of type weather.
    """

    WTHR = "WTHR"


class AssetClassSubProductType31Code(Enum):
    """
    AssetClassSubProductType31Code Defines the sub-product of type Dry
    Freight.

    :cvar DRYF: Dry Commodity of type dry freight.
    """

    DRYF = "DRYF"


class AssetClassSubProductType32Code(Enum):
    """
    AssetClassSubProductType32Code Defines the sub-product of type Wet
    Freight.

    :cvar WETF: Wet Commodity of type wet freight.
    """

    WETF = "WETF"


class AssetClassSubProductType33Code(Enum):
    """
    AssetClassSubProductType33Code Defines the sub-product of type
    Construction.

    :cvar CSTR: Construction Commodity of type construction.
    """

    CSTR = "CSTR"


class AssetClassSubProductType34Code(Enum):
    """
    AssetClassSubProductType34Code Defines the sub-product of type
    Manufacturing.

    :cvar MFTG: Manufacturing Commodity of type manufacturing.
    """

    MFTG = "MFTG"


class AssetClassSubProductType35Code(Enum):
    """
    AssetClassSubProductType35Code Defines the sub-product of type
    Containerboard.

    :cvar CBRD: Containerboard Commodity of type containerboard.
    """

    CBRD = "CBRD"


class AssetClassSubProductType36Code(Enum):
    """
    AssetClassSubProductType36Code Defines the sub-product of type
    Newsprint.

    :cvar NSPT: Newsprint Commodity of type newsprint.
    """

    NSPT = "NSPT"


class AssetClassSubProductType37Code(Enum):
    """
    AssetClassSubProductType37Code Defines the sub-product of type Pulp.

    :cvar PULP: Pulp Commodity of type pulp.
    """

    PULP = "PULP"


class AssetClassSubProductType39Code(Enum):
    """
    AssetClassSubProductType39Code Defines the sub-product of type Ammonia.

    :cvar AMMO: Ammonia Commodity of type ammonia.
    """

    AMMO = "AMMO"


class AssetClassSubProductType3Code(Enum):
    """
    AssetClassSubProductType3Code Defines the sub-product of type Olive
    Oil.

    :cvar OOLI: OliveOil Commodity of type olive oil.
    """

    OOLI = "OOLI"


class AssetClassSubProductType40Code(Enum):
    """
    AssetClassSubProductType40Code Defines the sub-product of type
    Diammonium Phosphate.

    :cvar DAPH: DiammoniumPhosphate Commodity of type diammonium
        phosphate.
    """

    DAPH = "DAPH"


class AssetClassSubProductType41Code(Enum):
    """
    AssetClassSubProductType41Code Defines the sub-product of type Potash.

    :cvar PTSH: Potash Commodity of type potash.
    """

    PTSH = "PTSH"


class AssetClassSubProductType42Code(Enum):
    """
    AssetClassSubProductType42Code Defines the sub-product of type Sulphur.

    :cvar SLPH: Sulphur Commodity of type sulphur.
    """

    SLPH = "SLPH"


class AssetClassSubProductType43Code(Enum):
    """
    AssetClassSubProductType43Code Defines the sub-product of type Urea.

    :cvar UREA: Urea Commodity of type urea.
    """

    UREA = "UREA"


class AssetClassSubProductType44Code(Enum):
    """
    AssetClassSubProductType44Code Defines the sub-product of type Urea and
    Ammonium Nitrate.

    :cvar UAAN: UreaAndAmmoniumNitrite Commodity of type urea and
        ammonium nitrite.
    """

    UAAN = "UAAN"


class AssetClassSubProductType45Code(Enum):
    """
    AssetClassSubProductType45Code Defines the sub-product of type Potato.

    :cvar POTA: Potato Commodity of type potato.
    """

    POTA = "POTA"


class AssetClassSubProductType46Code(Enum):
    """
    AssetClassSubProductType46Code Defines the sub-product of type
    Container Ship Freight.

    :cvar CSHP: ContainerShip Commodity of type container ships.
    """

    CSHP = "CSHP"


class AssetClassSubProductType49Code(Enum):
    """
    AssetClassSubProductType49Code Defines the sub-product of type as
    Other.

    :cvar OTHR: Other Commodity of other type.
    """

    OTHR = "OTHR"


class AssetClassSubProductType50Code(Enum):
    """
    AssetClassSubProductType50Code Defines the sub-product of type as
    either recovered paper or other.

    :cvar OTHR: Other Commodity of other type.
    :cvar RCVP: RecoveredPaper Commodity of type recovered paper.
    """

    OTHR = "OTHR"
    RCVP = "RCVP"


class AssetClassSubProductType5Code(Enum):
    """
    AssetClassSubProductType5Code Defines the sub-product of type Grain.

    :cvar GRIN: Grain Commodity of type grain.
    """

    GRIN = "GRIN"


class AssetClassSubProductType6Code(Enum):
    """
    AssetClassSubProductType6Code Defines the sub-product of type
    Electricity.

    :cvar ELEC: Electricity Commodity of type electricity.
    """

    ELEC = "ELEC"


class AssetClassSubProductType7Code(Enum):
    """
    AssetClassSubProductType7Code Defines the sub-product of type Natural
    Gas.

    :cvar NGAS: NaturalGas Commodity of type natural gas.
    """

    NGAS = "NGAS"


class AssetClassSubProductType8Code(Enum):
    """
    AssetClassSubProductType8Code Defines the sub-product of type Oil.

    :cvar OILP: Oil Commodity of type oil.
    """

    OILP = "OILP"


@dataclass(kw_only=True)
class CurrencyExchange231:
    """
    CurrencyExchange23__1 Describes the details of the currency exchange.

    :ivar ccy: Currency Indicates the currency.
    :ivar fxg_dt: FixingDate Specifies the date when a derivative will
        fix against an interest rate or an exchange rate that will be
        used to compute the cash settlement.
    """

    class Meta:
        name = "CurrencyExchange23__1"

    ccy: str = field(
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{3,3}",
        }
    )
    fxg_dt: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "FxgDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class DateAndDateTime2Choice1:
    """
    DateAndDateTime2Choice__1 Choice between a date or a date and time
    format.

    :ivar dt_tm: DateTime Specified date and time.
    """

    class Meta:
        name = "DateAndDateTime2Choice__1"

    dt_tm: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "DtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


class DebtInstrumentSeniorityType2Code(Enum):
    """
    DebtInstrumentSeniorityType2Code Specifies the seniority type of a
    specific debt instrument.

    :cvar SBOD: SubordinatedDebt Debt owed to an unsecured creditor that
        can only be paid, in the event of a liquidation, after the
        claims of secured creditors have been met.
    :cvar SNDB: SeniorDebt Debt that takes priority over other unsecured
        or otherwise more junior debt owed by the issuer.
    :cvar OTHR: Other Other type of debts.
    """

    SBOD = "SBOD"
    SNDB = "SNDB"
    OTHR = "OTHR"


class DerivativeEventType3Code1(Enum):
    """
    DerivativeEventType3Code__1 Explanation or reason for the action being
    taken on the transaction reporting.

    :cvar ALOC: Allocation Allocation event, where an existing
        derivative is allocated to different counterparties and reported
        as new derivatives.
    :cvar CLRG: Clearing Process in which a CCP interposes itself
        between the counterparties to the contract becoming the buyer to
        the counterparty that was a seller and the seller to the
        counterparty that was a buyer.
    :cvar CLAL: ClearingAndAllocation Simultaneous clearing and
        allocation event in a derivatives clearing organisation.
    :cvar COMP: Compression Compression or post-trade risk reduction
        exercise.
    :cvar CORP: CorporateAction Result of a corporate action.
    :cvar EXER: Exercise The exercise of an option or a swaption by one
        counterparty of the transaction, fully or partially.
    :cvar INCP: InclusionInPosition Inclusion of an ETD or CFD into a
        position, where an existing derivative is terminated and either
        a new position is created or the notional of an existing
        position is modified.
    :cvar NOVA: Novation The replacement of a party to a derivative
        contract with another party giving rise to a new derivative
        contract.
    :cvar PTNG: Porting The process by which a derivative transaction is
        transferred to another trade repository using the same UTI.
    :cvar TRAD: Trade Conclusion of a derivative or renegotiation of its
        terms that does not result in change of a counterparty.
    :cvar UPDT: Update Outstanding derivative is updated to comply with
        the revised requirements on reporting.
    """

    ALOC = "ALOC"
    CLRG = "CLRG"
    CLAL = "CLAL"
    COMP = "COMP"
    CORP = "CORP"
    EXER = "EXER"
    INCP = "INCP"
    NOVA = "NOVA"
    PTNG = "PTNG"
    TRAD = "TRAD"
    UPDT = "UPDT"


class DerivativeEventType3Code2(Enum):
    """
    DerivativeEventType3Code__2 Explanation or reason for the action being
    taken on the transaction reporting.

    :cvar ALOC: Allocation Allocation event, where an existing
        derivative is allocated to different counterparties and reported
        as new derivatives.
    :cvar COMP: Compression Compression or post-trade risk reduction
        exercise.
    :cvar CORP: CorporateAction Result of a corporate action.
    :cvar CREV: CreditEvent Applies only to credit derivatives. A credit
        event that results in a termination or modification of a
        derivative, at a trade or position level.
    :cvar ETRM: EarlyTermination Termination of an existing derivative
        transaction prior to scheduled termination or maturity date.
    :cvar EXER: Exercise The exercise of an option or a swaption by one
        counterparty of the transaction, fully or partially.
    :cvar INCP: InclusionInPosition Inclusion of an ETD or CFD into a
        position, where an existing derivative is terminated and either
        a new position is created or the notional of an existing
        position is modified.
    :cvar NOVA: Novation The replacement of a party to a derivative
        contract with another party giving rise to a new derivative
        contract.
    :cvar TRAD: Trade Conclusion of a derivative or renegotiation of its
        terms that does not result in change of a counterparty.
    :cvar UPDT: Update Outstanding derivative is updated to comply with
        the revised requirements on reporting.
    """

    ALOC = "ALOC"
    COMP = "COMP"
    CORP = "CORP"
    CREV = "CREV"
    ETRM = "ETRM"
    EXER = "EXER"
    INCP = "INCP"
    NOVA = "NOVA"
    TRAD = "TRAD"
    UPDT = "UPDT"


class DerivativeEventType3Code3(Enum):
    """
    DerivativeEventType3Code__3 Explanation or reason for the action being
    taken on the transaction reporting.

    :cvar ALOC: Allocation Allocation event, where an existing
        derivative is allocated to different counterparties and reported
        as new derivatives.
    :cvar CLRG: Clearing Process in which a CCP interposes itself
        between the counterparties to the contract becoming the buyer to
        the counterparty that was a seller and the seller to the
        counterparty that was a buyer.
    :cvar CLAL: ClearingAndAllocation Simultaneous clearing and
        allocation event in a derivatives clearing organisation.
    :cvar COMP: Compression Compression or post-trade risk reduction
        exercise.
    :cvar CORP: CorporateAction Result of a corporate action.
    :cvar CREV: CreditEvent Applies only to credit derivatives. A credit
        event that results in a termination or modification of a
        derivative, at a trade or position level.
    :cvar ETRM: EarlyTermination Termination of an existing derivative
        transaction prior to scheduled termination or maturity date.
    :cvar EXER: Exercise The exercise of an option or a swaption by one
        counterparty of the transaction, fully or partially.
    :cvar INCP: InclusionInPosition Inclusion of an ETD or CFD into a
        position, where an existing derivative is terminated and either
        a new position is created or the notional of an existing
        position is modified.
    :cvar NOVA: Novation The replacement of a party to a derivative
        contract with another party giving rise to a new derivative
        contract.
    """

    ALOC = "ALOC"
    CLRG = "CLRG"
    CLAL = "CLAL"
    COMP = "COMP"
    CORP = "CORP"
    CREV = "CREV"
    ETRM = "ETRM"
    EXER = "EXER"
    INCP = "INCP"
    NOVA = "NOVA"


class DerivativeEventType3Code4(Enum):
    """
    DerivativeEventType3Code__4 Explanation or reason for the action being
    taken on the transaction reporting.

    :cvar PTNG: Porting The process by which a derivative transaction is
        transferred to another trade repository using the same UTI.
    """

    PTNG = "PTNG"


@dataclass(kw_only=True)
class DerivativePartyIdentification1Choice:
    """
    DerivativePartyIdentification1Choice Reference entity of a single name
    credit default swap (CDS) or a derivative on single name credit default
    swap (CDS).

    :ivar ctry: Country Country of the reference entity.
    :ivar ctry_sub_dvsn: CountrySubDivision Country and country sub-
        division of the reference entity.
    :ivar lei: LEI Identification of the reference party through Legal
        entity identifier.
    """

    ctry: None | str = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    ctry_sub_dvsn: None | str = field(
        default=None,
        metadata={
            "name": "CtrySubDvsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{2,2}\-[0-9A-Z]{1,3}",
        },
    )
    lei: None | str = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


class EmbeddedType1Code(Enum):
    """
    EmbeddedType1Code Specifies the list of codes applicable to embedded
    option types.

    :cvar CANC: Cancellable Option can be cancelled.
    :cvar EXTD: Extendible Option can be extended.
    :cvar OPET: OptionalEarlyTermination Option can be early terminated.
    :cvar OTHR: Other Option type is other.
    :cvar MDET: MandatoryEarlyTermination Option must be early
        terminated.
    """

    CANC = "CANC"
    EXTD = "EXTD"
    OPET = "OPET"
    OTHR = "OTHR"
    MDET = "MDET"


@dataclass(kw_only=True)
class EventIdentifier1Choice1:
    """
    EventIdentifier1Choice__1 Indicates an event identifier or post trade
    risk reduction identifier.

    :ivar evt_idr: EventIdentifier Specifies event identifier.
    """

    class Meta:
        name = "EventIdentifier1Choice__1"

    evt_idr: None | str = field(
        default=None,
        metadata={
            "name": "EvtIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )


@dataclass(kw_only=True)
class ExchangeRateBasis1:
    """
    ExchangeRateBasis1 Provides information about the terms of the foreign
    exchange transaction.

    :ivar base_ccy: BaseCurrency Currency in which the rate of exchange
        is expressed in a currency exchange.&#13; &#13; Usage: In the
        example one GBP equals xxxUSD, the unit currency is GBP.
    :ivar qtd_ccy: QuotedCurrency Currency into which the base currency
        is converted, in a currency exchange.
    """

    base_ccy: str = field(
        metadata={
            "name": "BaseCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{3,3}",
        }
    )
    qtd_ccy: str = field(
        metadata={
            "name": "QtdCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{3,3}",
        }
    )


@dataclass(kw_only=True)
class ExerciseDate1Choice1:
    """
    ExerciseDate1Choice__1 Choice between a known exercise date and a
    pending date.

    :ivar frst_exrc_dt: FirstExerciseDate Specifies the earliest
        unadjusted date during the exercise period on which an option
        can be exercised.&#13; Usage : For European style options, the
        first possible exercise date is the same as the ExpirationDate.
        &#13; For American style options, the first possible exercise
        date is the same as the ExecutionTimeStamp. &#13; For Knock-in
        options, the first exercise date is reported when
        available.&#13;
    """

    class Meta:
        name = "ExerciseDate1Choice__1"

    frst_exrc_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "FrstExrcDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


class FinancialInstrumentContractType2Code(Enum):
    """
    FinancialInstrumentContractType2Code Specifies the contract type of a
    derivative.

    :cvar CFDS: ContractForDifference Contract of type contracts for
        difference.
    :cvar FRAS: ForwardRateAgreement Contract of type forward rate
        agreement.
    :cvar FUTR: Futures Contract of type future.
    :cvar FORW: Forward Contract of type forward.&#13; &#13;
    :cvar OPTN: Option Contract of type option.&#13;
    :cvar SPDB: SpreadBetting Contract of type spread betting.&#13;
    :cvar SWAP: Swap Contract of type swap.&#13;
    :cvar SWPT: Swaption Contract of type swaption.&#13;
    :cvar OTHR: Other Contract of other financial instrument contract
        type.
    """

    CFDS = "CFDS"
    FRAS = "FRAS"
    FUTR = "FUTR"
    FORW = "FORW"
    OPTN = "OPTN"
    SPDB = "SPDB"
    SWAP = "SWAP"
    SWPT = "SWPT"
    OTHR = "OTHR"


class FinancialPartySectorType3Code(Enum):
    """
    FinancialPartySectorType3Code Specifies the nature of the reporting
    counterparty business activities.

    :cvar AIFD: AlternativeInvestmentFund Alternative investment fund
        managed by an alternative investment fund manager (AIFM).
    :cvar CSDS: CentralSecuritiesDepository Central securities
        depository.
    :cvar CCPS: CentralCounterparty Central counterparty.
    :cvar CDTI: CreditInstitution Credit institution that takes deposits
        or other repayable funds from the public and grants credits for
        its own account.&#13;
    :cvar INUN: InsuranceUndertaking Insurance undertaking.
    :cvar ORPI: OccupationalRetirementProvisionInstitution Institution
        for occupational retirement provision established for the
        purpose of providing retirement benefits in the context of an
        occupational activity.
    :cvar INVF: InvestmentFirm Investment firm.&#13;
    :cvar REIN: ReinsuranceUndertaking Reinsurance undertaking
        performing the activity of accepting risks ceded by an insurance
        undertaking or by another reinsurance undertaking.
    :cvar UCIT: UCITSManagementCompany Undertaking for collective
        investment in transferable securities (UCITS) and its management
        company.
    :cvar ASSU: AssuranceUndertaking Assurance undertaking.&#13;
    :cvar OTHR: Other Other type of financial institution.
    """

    AIFD = "AIFD"
    CSDS = "CSDS"
    CCPS = "CCPS"
    CDTI = "CDTI"
    INUN = "INUN"
    ORPI = "ORPI"
    INVF = "INVF"
    REIN = "REIN"
    UCIT = "UCIT"
    ASSU = "ASSU"
    OTHR = "OTHR"


@dataclass(kw_only=True)
class FloatingRateIdentification8Choice1:
    """
    FloatingRateIdentification8Choice__1 Identifies various types of
    floating rates.

    :ivar cd: Code List of floating rate curves.
    """

    class Meta:
        name = "FloatingRateIdentification8Choice__1"

    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )


class Frequency13Code1(Enum):
    """
    Frequency13Code__1 Specifies the frequency of an interest payment with
    a time unit.

    :cvar DAIL: Daily Event takes place every day.
    :cvar WEEK: Weekly Event takes place once a week.
    :cvar MNTH: Monthly Event takes place every month or once a month.
    :cvar YEAR: Annual Event takes place every year or once a year.
    :cvar ADHO: Adhoc Event takes place on request or as necessary.
    :cvar EXPI: OnExpiry Event occurs on expiry of a financial contract.
    """

    DAIL = "DAIL"
    WEEK = "WEEK"
    MNTH = "MNTH"
    YEAR = "YEAR"
    ADHO = "ADHO"
    EXPI = "EXPI"


class Frequency19Code1(Enum):
    """
    Frequency19Code__1 Specifies the frequency of an interest payment with
    a time unit.

    :cvar DAIL: Daily Event takes place every day.
    :cvar WEEK: Weekly Event takes place once a week.
    :cvar MNTH: Monthly Event takes place every month or once a month.
    :cvar YEAR: Annual Event takes place every year or once a year.
    :cvar ADHO: Adhoc Event takes place on request or as necessary.
    :cvar EXPI: OnExpiry Event occurs on expiry of a financial contract.
    :cvar HOUL: Hourly Event takes place every hours.
    :cvar ODMD: OnDemand Event takes place on demand.
    """

    DAIL = "DAIL"
    WEEK = "WEEK"
    MNTH = "MNTH"
    YEAR = "YEAR"
    ADHO = "ADHO"
    EXPI = "EXPI"
    HOUL = "HOUL"
    ODMD = "ODMD"


@dataclass(kw_only=True)
class GenericIdentification1751:
    """
    GenericIdentification175__1 Information related to an identification,
    for example party identification or account identification.

    :ivar id: Identification Identification assigned by an institution.
    """

    class Meta:
        name = "GenericIdentification175__1"

    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 72,
        }
    )


@dataclass(kw_only=True)
class GenericIdentification1753:
    """
    GenericIdentification175__3 Information related to an identification,
    for example party identification or account identification.

    :ivar id: Identification Identification assigned by an institution.
    """

    class Meta:
        name = "GenericIdentification175__3"

    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 12,
        }
    )


@dataclass(kw_only=True)
class GenericIdentification1754:
    """
    GenericIdentification175__4 Information related to an identification,
    for example party identification or account identification.

    :ivar id: Identification Identification assigned by an institution.
    :ivar schme_nm: SchemeName Name of the identification scheme.
    """

    class Meta:
        name = "GenericIdentification175__4"

    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 72,
        }
    )
    schme_nm: None | str = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass(kw_only=True)
class GenericIdentification184:
    """
    GenericIdentification184 Information related to an identification, for
    example, party identification or account identification.

    :ivar id: Identification Indicates other identifier of an underlier.
    :ivar src: Source Indicates the source of the identifier that
        represent the underlier.
    """

    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 210,
        }
    )
    src: str = field(
        metadata={
            "name": "Src",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 100,
        }
    )


@dataclass(kw_only=True)
class GenericIdentification1851:
    """
    GenericIdentification185__1 Information related to an identification,
    for example party identification or account identification.

    :ivar id: Identification Identification assigned by an institution.
    :ivar schme_nm: SchemeName Name of the identification scheme.
    """

    class Meta:
        name = "GenericIdentification185__1"

    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 100,
        }
    )
    schme_nm: None | str = field(
        default=None,
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )


class HktrpartyScheme(Enum):
    """
    HKTRPartyScheme The type of identification code.

    :cvar BRNO: BRN
    :cvar CICR: CICR
    :cvar TRID: TREntityID
    :cvar UBIN: UniqueBusinessIdentifier
    :cvar USDC: UserDefinedCode
    """

    BRNO = "BRNO"
    CICR = "CICR"
    TRID = "TRID"
    UBIN = "UBIN"
    USDC = "USDC"


@dataclass(kw_only=True)
class IndexIdentification11:
    """
    IndexIdentification1__1 Specifies the elements for the identification
    of an index.

    ISIN is the preferred format.

    :ivar isin: ISIN International Securities Identification Number
        (ISIN). A numbering system designed by the United Nation's
        International Organisation for Standardisation (ISO). The ISIN
        is composed of a 2-character prefix representing the country of
        issue, followed by the national security number (if one exists),
        and a check digit. Each country has a national numbering agency
        that assigns ISIN numbers for securities in that country.
    :ivar nm: Name Proprietary identification of the index on which the
        financial instrument is based.
    """

    class Meta:
        name = "IndexIdentification1__1"

    isin: None | str = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    nm: None | str = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 50,
        },
    )


class InterestComputationMethod4Code(Enum):
    """
    InterestComputationMethod4Code Specifies the method used to compute
    accruing interest of a financial instrument.

    :cvar A004: Actual360 Method whereby interest is calculated based on
        the actual number of accrued days in the interest period and a
        360-day year.
    :cvar A019: Actual360NL Method whereby interest is calculated based
        on the actual number of accrued days in the interest period,
        excluding any leap day from the count, and a 360-day year.
    :cvar A017: Actual364 Method whereby interest is calculated based on
        the actual number of accrued days in the interest period divided
        by 364.&#13; Method equal to Act364 in the FixML model.
    :cvar A005: Actual365Fixed Method whereby interest is calculated
        based on the actual number of accrued days in the interest
        period and a 365-day year.
    :cvar A009: Actual365LorActuActubasisRule Method whereby interest is
        calculated based on the actual number of accrued days and a
        365-day year (if the coupon payment date is NOT in a leap year)
        or a 366-day year (if the coupon payment date is in a leap
        year).
    :cvar A014: Actual365NL Method whereby interest is calculated based
        on the actual number of accrued days in the interest period,
        excluding any leap day from the count, and a 365-day year.
    :cvar A010: ActualActualAFB Method whereby interest is calculated
        based on the actual number of accrued days and a 366-day year
        (if 29 Feb falls in the coupon period) or a 365-day year (if 29
        Feb does not fall in the coupon period). If a coupon period is
        longer than one year, it is split by repetitively separating
        full year subperiods counting backwards from the end of the
        coupon period (a year backwards from 28 Feb being 29 Feb, if it
        exists). The first of the subperiods starts on the start date of
        the accrued interest period and thus is possibly shorter than a
        year. Then the interest computation is operated separately on
        each subperiod and the intermediate results are summed up.
    :cvar A006: ActualActualICMA Method whereby interest is calculated
        based on the actual number of accrued days and the assumed
        number of days in a year, that is, the actual number of days in
        the coupon period multiplied by the number of interest payments
        in the year. If the coupon period is irregular (first or last
        coupon), it is extended or split into quasi-interest periods
        that have the length of a regular coupon period and the
        computation is operated separately on each quasi-interest period
        and the intermediate results are summed up.
    :cvar A008: ActualActualISDA Method whereby interest is calculated
        based on the actual number of accrued days of the interest
        period that fall (falling on a normal year, year) divided by
        365, added to the actual number of days of the interest period
        that fall (falling on a leap year, year) divided by 366.
    :cvar A015: ActualActualUltimo Method whereby interest is calculated
        based on the actual number of days in the coupon period divided
        by the actual number of days in the year. This method is a
        variation of the ActualActualICMA method with the exception that
        it assumes that the coupon always falls on the last day of the
        month. Method equal to ACT/ACT.ISMA in the FpML model and
        Act/Act (ICSMA Ultimo) in the FixML model.
    :cvar A018: Business252 Method whereby interest is calculated based
        on the actual number of business days in the interest period
        divided by 252. &#13; Usage: Brazilian Currency Swaps. &#13;
        Method equal to BUS/252 in the FpML model and BusTwoFiftyTwo in
        the FixML model.
    :cvar A011: IC30360ICMAor30360basicrule Method whereby interest is
        calculated based on a 30-day month and a 360-day year. Accrued
        interest to a value date on the last day of a month shall be the
        same as to the 30th calendar day of the same month, except for
        February. This means that the 31st is assumed to be the 30th and
        28 Feb (or 29 Feb for a leap year) is assumed to be the 28th (or
        29th). It is the most commonly used 30/360 method for non-US
        straight and convertible bonds issued before 1 January 1999.
    :cvar A001: IC30360ISDAor30360AmericanBasicRule Method whereby
        interest is calculated based on a 30-day month and a 360-day
        year. Accrued interest to a value date on the last day of a
        month shall be the same as to the 30th calendar day of the same
        month, except for February, and provided that the interest
        period started on a 30th or a 31st. This means that a 31st is
        assumed to be a 30th if the period started on a 30th or a 31st
        and the 28 Feb (or 29 Feb for a leap year) is assumed to be the
        28th (or 29th). This is the most commonly used 30/360 method for
        US straight and convertible bonds.
    :cvar A002: IC30365 Method whereby interest is calculated based on a
        30-day month in a way similar to the 30/360 (basic rule) and a
        365-day year. Accrued interest to a value date on the last day
        of a month shall be the same as to the 30th calendar day of the
        same month, except for February. This means that a 31st is
        assumed to be the 30th and the 28 Feb (or 29 Feb for a leap
        year) is assumed to be the 28th (or 29th).
    :cvar A003: IC30Actual Method whereby interest is calculated based
        on a 30-day month in a way similar to the 30/360 (basic rule)
        and the assumed number of days in a year in a way similar to the
        Actual/Actual (ICMA). Accrued interest to a value date on the
        last day of a month shall be the same as to the 30th calendar
        day of the same month, except for February. This means that the
        31st is assumed to be the 30th and 28 Feb (or 29 Feb for a leap
        year) is assumed to be the 28th (or 29th). The assumed number of
        days in a year is computed as the actual number of days in the
        coupon period multiplied by the number of interest payments in
        the year.
    :cvar A012: IC30E2360orEurobondbasismodel2 Method whereby interest
        is calculated based on a 30-day month and a 360-day year.
        Accrued interest to a value date on the last day of a month
        shall be the same as to the 30th calendar day of the same month,
        except for the last day of February whose day of the month value
        shall be adapted to the value of the first day of the interest
        period if the latter is higher and if the period is one of a
        regular schedule. This means that the 31st is assumed to be the
        30th and 28 Feb of a non-leap year is assumed to be equivalent
        to 29 Feb when the first day of the interest period is the 29th,
        or to 30 Feb when the first day of the interest period is the
        30th or the 31st. The 29th day of February in a leap year is
        assumed to be equivalent to 30 Feb when the first day of the
        interest period is the 30th or the 31st. Similarly, if the
        coupon period starts on the last day of February, it is assumed
        to produce only one day of interest in February as if it was
        starting on 30 Feb when the end of the period is the 30th or the
        31st, or two days of interest in February when the end of the
        period is the 29th, or three days of interest in February when
        it is 28 Feb of a non-leap year and the end of the period is
        before the 29th.
    :cvar A013: IC30E3360orEurobondbasismodel3 Method whereby interest
        is calculated based on a 30-day month and a 360-day year.
        Accrued interest to a value date on the last day of a month
        shall be the same as to the 30th calendar day of the same month.
        This means that the 31st is assumed to be the 30th and 28 Feb
        (or 29 Feb for a leap year) is assumed to be equivalent to 30
        Feb. It is a variation of the 30E/360 (or Eurobond basis) method
        where the last day of February is always assumed to be the 30th,
        even if it is the last day of the maturity coupon period.
    :cvar A007: IC30E360orEuroBondBasismodel1 Method whereby interest is
        calculated based on a 30-day month and a 360-day year. Accrued
        interest to a value date on the last day of a month shall be the
        same as to the 30th calendar day of the same month. This means
        that the 31st is assumed to be the 30th and the 28 Feb (or 29
        Feb for a leap year) is assumed to be equivalent to 30 Feb.
        However, if the last day of the maturity coupon period is the
        last day of February, it will not be assumed to be the 30th. It
        is a variation of the 30/360 (ICMA) method commonly used for
        eurobonds. The usage of this variation is only relevant when the
        coupon periods are scheduled to end on the last day of the
        month.
    :cvar A016: IC30EPlus360 Method whereby interest is calculated based
        on a 30-day month and a 360-day year. Accrued interest to a
        value date on the last day of a month shall be the same as to
        the 30th calendar day of the same month. This means that the
        31st is assumed to be the 30th and 28 Feb (or 29 Feb for a leap
        year) is assumed to be equivalent to 30 Feb. This method is a
        variation of the 30E360 method with the exception that if the
        coupon falls on the last day of the month, change it to 1 and
        increase the month by 1 (ie next month). Method equal to
        ThirtyEPlusThreeSixty in the FixML model.
    :cvar NARR: Narrative Other method than A001-A020. See Narrative.
    :cvar A020: OneOne Also named 1/1. &#13;&#13; ELABORATION: If
        parties specify the Day Count Fraction to be 1/1 then in
        calculating the applicable amount, 1 is simply input into the
        calculation as the relevant Day Count Fraction. See also 2006
        ISDA Definitions, Section 4.16. Day Count Fraction, paragraph
        (a).
    """

    A004 = "A004"
    A019 = "A019"
    A017 = "A017"
    A005 = "A005"
    A009 = "A009"
    A014 = "A014"
    A010 = "A010"
    A006 = "A006"
    A008 = "A008"
    A015 = "A015"
    A018 = "A018"
    A011 = "A011"
    A001 = "A001"
    A002 = "A002"
    A003 = "A003"
    A012 = "A012"
    A013 = "A013"
    A007 = "A007"
    A016 = "A016"
    NARR = "NARR"
    A020 = "A020"


class NoReasonCode(Enum):
    """
    NoReasonCode Specifies that there is no reason available.

    :cvar NORE: NoReason No reason to report or no reason available to
        report.
    """

    NORE = "NORE"


class NotApplicable1Code(Enum):
    """
    NotApplicable1Code Specifies special purpose codes.

    :cvar NOAP: NotApplicable Not applicable (N/A).
    """

    NOAP = "NOAP"


class OptionParty1Code(Enum):
    """
    OptionParty1Code Specifies if a trade party is a buyer or a seller.

    :cvar SLLR: Seller Seller in a trade.
    :cvar BYER: Buyer Buyer in a trade.
    """

    SLLR = "SLLR"
    BYER = "BYER"


class OptionParty3Code(Enum):
    """
    OptionParty3Code Specifies if a trade party is a taker or a maker.

    :cvar MAKE: Maker Indicates the receiver of the trade.
    :cvar TAKE: Taker Indicates the initiator of the trade.
    """

    MAKE = "MAKE"
    TAKE = "TAKE"


class OptionStyle6Code(Enum):
    """
    OptionStyle6Code Specifies how an option can be exercised.

    :cvar EURO: European Option that can be exercised on expiry date
        only.
    :cvar BERM: Bermudan Option that can be exercised on multiple
        discrete dates prior to, or on expiry date.
    :cvar ASIA: Asian Option where the payoff is not determined by the
        underlying price at maturity but by the average underlying price
        over some pre-set period of time.
    :cvar AMER: American Option can be exercised before or on expiry
        date.
    """

    EURO = "EURO"
    BERM = "BERM"
    ASIA = "ASIA"
    AMER = "AMER"


class OptionType2Code(Enum):
    """
    OptionType2Code Specifies whether it is a call option (right to
    purchase a specific underlying asset) or a put option (right to sell a
    specific underlying asset) or any other type of option.

    :cvar CALL: Call Right to buy a quantity of an asset for an agreed
        price at exercise date.
    :cvar PUTO: Put Right to sell a quantity of an asset for an agreed
        price at exercise date.
    :cvar OTHR: Other Right where the holder of the option decides
        whether the option is put or call.
    """

    CALL = "CALL"
    PUTO = "PUTO"
    OTHR = "OTHR"


@dataclass(kw_only=True)
class OrganisationIdentification15Choice1:
    """
    OrganisationIdentification15Choice__1 Provides the identification of
    the organisation.

    :ivar lei: LEI Identification is done through the use of legal
        entity identifier code.
    """

    class Meta:
        name = "OrganisationIdentification15Choice__1"

    lei: None | str = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )


class PaymentType4Code(Enum):
    """
    PaymentType4Code Specifies the type, or nature, of the payment.

    :cvar UFRO: Upfront Transaction is an initial payment made by one of
        the counterparties  either to bring a transaction to fair value
        or for any other reason that may be the cause of an off-market
        transaction.
    :cvar UWIN: UnWind Transaction is the final settlement payment made
        when a transaction is unwound prior to its end date or a payment
        that may result due to the full termination of derivative
        transaction(s).
    :cvar PEXH: PrincipalExchange Transaction is an exchange of notional
        values for cross-currency swaps.
    """

    UFRO = "UFRO"
    UWIN = "UWIN"
    PEXH = "PEXH"


class PhysicalTransferType4Code(Enum):
    """
    PhysicalTransferType4Code Specifies the asset delivery type when the
    financial instrument is settled.

    :cvar PHYS: Physical Physical transfer.
    :cvar OPTL: Optional Determined by a third party or optional for
        counterparty.
    :cvar CASH: Cash Cash transfer.
    """

    PHYS = "PHYS"
    OPTL = "OPTL"
    CASH = "CASH"


@dataclass(kw_only=True)
class PortfolioIdentification31:
    """
    PortfolioIdentification3__1 Identifies the portfolio if the collateral
    is reported on a portfolio basis.

    :ivar cd: Code Unique code determined by the reporting counterparty
        to identify the portfolio if collateral is reported on a
        portfolio basis.
    """

    class Meta:
        name = "PortfolioIdentification3__1"

    cd: str = field(
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 52,
        }
    )


class ProductType4Code1(Enum):
    """
    ProductType4Code__1 Specifies the underlying type of product or
    financial instrument.

    :cvar CRDT: Credit Identifies categories of instruments that are
        credits.
    :cvar CURR: Currency Identifies categories of currency instruments.
    :cvar EQUI: Equity Identifies the nature or type of an equity.
    :cvar INTR: InterestRate Identifies categories of instruments that
        are interest rates based.
    :cvar COMM: Commodity Identifies categories of instruments that are
        commodities.
    """

    CRDT = "CRDT"
    CURR = "CURR"
    EQUI = "EQUI"
    INTR = "INTR"
    COMM = "COMM"


@dataclass(kw_only=True)
class Schedule101:
    """
    Schedule10__1 Indicates the unadjusted effective and end date of the
    schedule.

    :ivar qty: Quantity Number of units of the financial instrument,
        that is, the nominal value.
    :ivar uadjstd_fctv_dt: UnadjustedEffectiveDate Indicates the
        unadjusted date at which obligations under the  derivative
        transaction come into effect, as included in the confirmation.
    :ivar uadjstd_end_dt: UnadjustedEndDate Indicates the end date
        agreed in the derivative transaction without adjustment.
    """

    class Meta:
        name = "Schedule10__1"

    qty: Decimal = field(
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 25,
            "fraction_digits": 5,
        }
    )
    uadjstd_fctv_dt: XmlDate = field(
        metadata={
            "name": "UadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    uadjstd_end_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "UadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class SecuritiesTransactionPrice14Choice1:
    """
    SecuritiesTransactionPrice14Choice__1 Choice to define the price of the
    securities transaction.

    :ivar dcml: Decimal
    """

    class Meta:
        name = "SecuritiesTransactionPrice14Choice__1"

    dcml: None | Decimal = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass(kw_only=True)
class SupplementaryDataEnvelope1:
    """
    SupplementaryDataEnvelope1 Technical component that contains the
    validated supplementary data information.

    This technical envelope allows to segregate the supplementary data
    information from any other information.
    """

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class TechnicalAttributes51:
    """
    TechnicalAttributes5__1 Specifies technical attributes of the message.

    :ivar tech_rcrd_id: TechnicalRecordIdentification Unique identifier
        of a record in a message used as part of error management and
        status advice message.
    """

    class Meta:
        name = "TechnicalAttributes5__1"

    tech_rcrd_id: str = field(
        metadata={
            "name": "TechRcrdId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 140,
        }
    )


class TradeConfirmationType1Code(Enum):
    """
    TradeConfirmationType1Code Specifies whether the contract was
    electronically confirmed or non-electronically confirmed.

    :cvar ECNF: ElectronicallyConfirmed Electronically confirmed.
    :cvar YCNF: NonElectronicallyConfirmed Non-electronically confirmed.
    """

    ECNF = "ECNF"
    YCNF = "YCNF"


class TradeConfirmationType2Code(Enum):
    """
    TradeConfirmationType2Code Specifies that the contract was
    electronically non-confirmed.

    :cvar NCNF: NonConfirmed Non-confirmed.
    """

    NCNF = "NCNF"


@dataclass(kw_only=True)
class TradeReportHeader41:
    """
    TradeReportHeader4__1 Provides the details of the header for a trade
    transaction query message.

    :ivar nb_rcrds: NumberRecords Indicates the number of records in the
        page.
    """

    class Meta:
        name = "TradeReportHeader4__1"

    nb_rcrds: Decimal = field(
        metadata={
            "name": "NbRcrds",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 4,
            "fraction_digits": 0,
        }
    )


class TradingCapacity7Code(Enum):
    """
    TradingCapacity7Code Specifies the role of a trading party in a
    transaction.

    :cvar AGEN: Agent Trading as Agent on behalf of a customer.
    :cvar PRIN: Principal Trading as Principal.
    """

    AGEN = "AGEN"
    PRIN = "PRIN"


@dataclass(kw_only=True)
class Tranche3:
    """
    Tranche3 Indicates derivative contract was tranched.

    :ivar attchmnt_pt: AttachmentPoint Indicates the lower point at
        which the level of losses in the underlying portfolio reduces
        the notional of the tranche.
    :ivar dtchmnt_pt: DetachmentPoint Indicates the point beyond which
        the losses in the underlying portfolio no longer reduce the
        notional of the tranche.
    """

    attchmnt_pt: None | Decimal = field(
        default=None,
        metadata={
            "name": "AttchmntPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    dtchmnt_pt: None | Decimal = field(
        default=None,
        metadata={
            "name": "DtchmntPt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass(kw_only=True)
class UnitOfMeasure8Choice1:
    """
    UnitOfMeasure8Choice__1 Unit of measure in which the quantity is
    expressed.

    :ivar cd: Code Unit of measure, as defined in an external code set.
    """

    class Meta:
        name = "UnitOfMeasure8Choice__1"

    cd: None | str = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 4,
        },
    )


class ValuationType1Code(Enum):
    """
    ValuationType1Code Specifies the type used for the calculation of the
    valuation.

    :cvar CCPV: CCPValuation Central counterparty (CCP) valuation.
    :cvar MTMA: MarkToMarket Mark to market valuation.&#13; &#13;
    :cvar MTMO: MarkToModel Mark to model valuation.&#13;
    """

    CCPV = "CCPV"
    MTMA = "MTMA"
    MTMO = "MTMO"


@dataclass(kw_only=True)
class AgriculturalCommodityDairy2:
    """
    AgriculturalCommodityDairy2 Defines commodity sub-product attributes of
    an agricultural derivative of type dairy.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType1Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType20Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AgriculturalCommodityForestry2:
    """
    AgriculturalCommodityForestry2 Defines commodity sub-product attributes
    of an agricultural derivative of type forestry.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType1Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType21Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AgriculturalCommodityGrain3:
    """
    AgriculturalCommodityGrain3 Defines commodity sub-product attributes of
    an agricultural derivative of type grain.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    :ivar addtl_sub_pdct: AdditionalSubProduct Further subproduct type
        related to instruments that have a non-financial instrument or
        commodity as underlying.
    """

    base_pdct: AssetClassProductType1Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType5Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    addtl_sub_pdct: None | AssetClassDetailedSubProductType30Code = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AgriculturalCommodityLiveStock2:
    """
    AgriculturalCommodityLiveStock2 Defines commodity sub-product
    attributes of an agricultural derivative of type livestock.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType1Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType22Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AgriculturalCommodityOilSeed2:
    """
    AgriculturalCommodityOilSeed2 Defines commodity sub-product attributes
    of an agricultural derivative of type oil seed.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    :ivar addtl_sub_pdct: AdditionalSubProduct Further subproduct type
        related to instruments that have a non-financial instrument or
        commodity as underlying.
    """

    base_pdct: AssetClassProductType1Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType1Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    addtl_sub_pdct: None | AssetClassDetailedSubProductType1Code = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AgriculturalCommodityOliveOil3:
    """
    AgriculturalCommodityOliveOil3 Defines commodity sub-product attributes
    of an agricultural derivative of type olive oil.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    :ivar addtl_sub_pdct: AdditionalSubProduct Further subproduct type
        related to instruments that have a non-financial instrument or
        commodity as underlying.
    """

    base_pdct: AssetClassProductType1Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType3Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    addtl_sub_pdct: None | AssetClassDetailedSubProductType29Code = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AgriculturalCommodityOther2:
    """
    AgriculturalCommodityOther2 Other agricultural commodity derivative.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType1Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType49Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AgriculturalCommodityPotato2:
    """
    AgriculturalCommodityPotato2 Defines commodity sub-product attributes
    of an agricultural derivative of type potato.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType1Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType45Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AgriculturalCommoditySeafood2:
    """
    AgriculturalCommoditySeafood2 Defines commodity sub-product attributes
    of an agricultural derivative of type seafood.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType1Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType23Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AgriculturalCommoditySoft2:
    """
    AgriculturalCommoditySoft2 Defines commodity sub-product attributes of
    an agricultural derivative of type soft.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    :ivar addtl_sub_pdct: AdditionalSubProduct Further subproduct type
        related to instruments that have a non-financial instrument or
        commodity as underlying.
    """

    base_pdct: AssetClassProductType1Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType2Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    addtl_sub_pdct: None | AssetClassDetailedSubProductType2Code = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AmountAndDirection1061:
    """
    AmountAndDirection106__1 Posting of an item to a cash account, in the
    context of a cash transaction, that results in an increase or decrease
    to the balance of the account.

    :ivar amt: Amount Amount of money in the cash entry.
    :ivar sgn: Sign Indicates that the amount value is positive or
        negative.
    """

    class Meta:
        name = "AmountAndDirection106__1"

    amt: ActiveOrHistoricCurrencyAnd13DecimalAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sgn: None | bool = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AmountAndDirection1062:
    """
    AmountAndDirection106__2 Posting of an item to a cash account, in the
    context of a cash transaction, that results in an increase or decrease
    to the balance of the account.

    :ivar amt: Amount Amount of money in the cash entry.
    :ivar sgn: Sign Indicates that the amount value is positive or
        negative.
    """

    class Meta:
        name = "AmountAndDirection106__2"

    amt: ActiveOrHistoricCurrencyAnd5DecimalAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sgn: None | bool = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AmountAndDirection1063:
    """
    AmountAndDirection106__3 Posting of an item to a cash account, in the
    context of a cash transaction, that results in an increase or decrease
    to the balance of the account.

    :ivar amt: Amount Amount of money in the cash entry.
    """

    class Meta:
        name = "AmountAndDirection106__3"

    amt: ActiveOrHistoricCurrencyAnd5DecimalAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class AmountAndDirection1091:
    """
    AmountAndDirection109__1 Posting of an item to a cash account, in the
    context of a cash transaction, that results in an increase or decrease
    to the balance of the account.

    :ivar amt: Amount Amount of money in the cash entry.
    :ivar sgn: Sign Indicates that the amount value is positive or
        negative.
    """

    class Meta:
        name = "AmountAndDirection109__1"

    amt: ActiveOrHistoricCurrencyAnd5DecimalAmount = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sgn: None | bool = field(
        default=None,
        metadata={
            "name": "Sgn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AssetClassCommodityC10Other1:
    """
    AssetClassCommodityC10Other1 Defines commodity attributes of a
    derivative where the type is other C10.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    """

    base_pdct: AssetClassProductType11Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class AssetClassCommodityIndex1:
    """
    AssetClassCommodityIndex1 Defines commodity attributes of a derivative
    where the type is index.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    """

    base_pdct: AssetClassProductType16Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class AssetClassCommodityInflation1:
    """
    AssetClassCommodityInflation1 Defines commodity attributes of a
    derivative where the type is inflation.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    """

    base_pdct: AssetClassProductType12Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class AssetClassCommodityMultiCommodityExotic1:
    """
    AssetClassCommodityMultiCommodityExotic1 Defines commodity attributes
    of a derivative where the type is multi commodity exotic.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    """

    base_pdct: AssetClassProductType13Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class AssetClassCommodityOfficialEconomicStatistics1:
    """
    AssetClassCommodityOfficialEconomicStatistics1 Defines commodity
    attributes of a derivative where the type is official economic
    statistics.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    """

    base_pdct: AssetClassProductType14Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class AssetClassCommodityOther1:
    """
    AssetClassCommodityOther1 Defines commodity attributes of a derivative
    where the type is other.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    """

    base_pdct: AssetClassProductType15Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class ClearingExceptionOrExemption3Choice1:
    """
    ClearingExceptionOrExemption3Choice__1 Information about contract
    status.

    :ivar rsn: Reason No reason to report or no reason available to
        report.
    """

    class Meta:
        name = "ClearingExceptionOrExemption3Choice__1"

    rsn: None | NoReasonCode = field(
        default=None,
        metadata={
            "name": "Rsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class ContractType152:
    """
    ContractType15__2 Information related to contract attributes.

    :ivar asst_clss: AssetClass Specifies the classification according
        to the asset class of the contract.
    """

    class Meta:
        name = "ContractType15__2"

    asst_clss: ProductType4Code1 = field(
        metadata={
            "name": "AsstClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class DerivativeEvent61:
    """
    DerivativeEvent6__1 Information related to derivative details.

    :ivar tp: Type Classification of derivative event type.
    :ivar id: Identification Indicates means of identification of a
        derivative event.
    :ivar tm_stmp: TimeStamp Indicates the time stamp of a derivative
        event.
    """

    class Meta:
        name = "DerivativeEvent6__1"

    tp: DerivativeEventType3Code1 = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    id: None | EventIdentifier1Choice1 = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    tm_stmp: DateAndDateTime2Choice1 = field(
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class DerivativeEvent62:
    """
    DerivativeEvent6__2 Information related to derivative details.

    :ivar tp: Type Classification of derivative event type.
    :ivar id: Identification Indicates means of identification of a
        derivative event.
    :ivar tm_stmp: TimeStamp Indicates the time stamp of a derivative
        event.
    """

    class Meta:
        name = "DerivativeEvent6__2"

    tp: None | DerivativeEventType3Code2 = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    id: None | EventIdentifier1Choice1 = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    tm_stmp: DateAndDateTime2Choice1 = field(
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class DerivativeEvent63:
    """
    DerivativeEvent6__3 Information related to derivative details.

    :ivar id: Identification Indicates means of identification of a
        derivative event.
    :ivar tm_stmp: TimeStamp Indicates the time stamp of a derivative
        event.
    """

    class Meta:
        name = "DerivativeEvent6__3"

    id: None | EventIdentifier1Choice1 = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    tm_stmp: DateAndDateTime2Choice1 = field(
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class DerivativeEvent64:
    """
    DerivativeEvent6__4 Information related to derivative details.

    :ivar tp: Type Classification of derivative event type.
    :ivar id: Identification Indicates means of identification of a
        derivative event.
    :ivar tm_stmp: TimeStamp Indicates the time stamp of a derivative
        event.
    """

    class Meta:
        name = "DerivativeEvent6__4"

    tp: DerivativeEventType3Code3 = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    id: None | EventIdentifier1Choice1 = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    tm_stmp: DateAndDateTime2Choice1 = field(
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class DerivativeEvent65:
    """
    DerivativeEvent6__5 Information related to derivative details.

    :ivar id: Identification Indicates means of identification of a
        derivative event.
    """

    class Meta:
        name = "DerivativeEvent6__5"

    id: None | EventIdentifier1Choice1 = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class DerivativeEvent66:
    """
    DerivativeEvent6__6 Information related to derivative details.

    :ivar tp: Type Classification of derivative event type.
    """

    class Meta:
        name = "DerivativeEvent6__6"

    tp: DerivativeEventType3Code4 = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class Direction21:
    """
    Direction2__1 Elements indicating the direction of the derivative
    transaction.

    :ivar drctn_of_the_frst_leg: DirectionOfTheFirstLeg Identifies
        whether the reporting counterparty is the payer (Taker) or the
        receiver (Maker) of the first leg as determined at the time of
        transaction.
    :ivar drctn_of_the_scnd_leg: DirectionOfTheSecondLeg Identifies
        whether the reporting counterparty is the payer (Taker) or the
        receiver (Maker) of the second leg as determined at the time of
        transaction.
    """

    class Meta:
        name = "Direction2__1"

    drctn_of_the_frst_leg: OptionParty3Code = field(
        metadata={
            "name": "DrctnOfTheFrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    drctn_of_the_scnd_leg: OptionParty3Code = field(
        metadata={
            "name": "DrctnOfTheScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class EnergyCommodityCoal2:
    """
    EnergyCommodityCoal2 Defines commodity sub-product attributes of an
    energy derivative of type coal.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType2Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType24Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class EnergyCommodityDistillates2:
    """
    EnergyCommodityDistillates2 Defines commodity sub-product attributes of
    an energy derivative of type distillates.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType2Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType25Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class EnergyCommodityElectricity2:
    """
    EnergyCommodityElectricity2 Defines commodity sub-product attributes of
    an energy derivative of type electricity.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    :ivar addtl_sub_pdct: AdditionalSubProduct Further subproduct type
        related to instruments that have a non-financial instrument or
        commodity as underlying.
    """

    base_pdct: AssetClassProductType2Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType6Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    addtl_sub_pdct: None | AssetClassDetailedSubProductType5Code = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class EnergyCommodityInterEnergy2:
    """
    EnergyCommodityInterEnergy2 Defines commodity sub-product attributes of
    an energy derivative of type inter energy.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType2Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType26Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class EnergyCommodityLightEnd2:
    """
    EnergyCommodityLightEnd2 Defines commodity sub-product attributes of an
    energy derivative of type light end.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType2Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType27Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class EnergyCommodityNaturalGas3:
    """
    EnergyCommodityNaturalGas3 Defines commodity sub-product attributes of
    an energy derivative of type natural gas.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    :ivar addtl_sub_pdct: AdditionalSubProduct Further subproduct type
        related to instruments that have a non-financial instrument or
        commodity as underlying.
    """

    base_pdct: AssetClassProductType2Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType7Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    addtl_sub_pdct: None | AssetClassDetailedSubProductType31Code = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class EnergyCommodityOil3:
    """
    EnergyCommodityOil3 Defines commodity sub-product attributes of an
    energy derivative of type oil.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    :ivar addtl_sub_pdct: AdditionalSubProduct Further subproduct type
        related to instruments that have a non-financial instrument or
        commodity as underlying.
    """

    base_pdct: AssetClassProductType2Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType8Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    addtl_sub_pdct: None | AssetClassDetailedSubProductType32Code = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class EnergyCommodityOther2:
    """
    EnergyCommodityOther2 Other energy commodity derivative.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType2Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType49Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class EnergyCommodityRenewableEnergy2:
    """
    EnergyCommodityRenewableEnergy2 Defines commodity sub-product
    attributes of an energy derivative of type renewable energy.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType2Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType28Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class EnvironmentCommodityOther2:
    """
    EnvironmentCommodityOther2 Other environment commodity derivative.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType3Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType49Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class EnvironmentalCommodityCarbonRelated2:
    """
    EnvironmentalCommodityCarbonRelated2 Defines commodity sub-product
    attributes of an environmental derivative of type carbon related.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType3Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType29Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class EnvironmentalCommodityEmission3:
    """
    EnvironmentalCommodityEmission3 Defines commodity sub-product
    attributes of an environmental derivative of type emission.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    :ivar addtl_sub_pdct: AdditionalSubProduct Further subproduct type
        related to instruments that have a non-financial instrument or
        commodity as underlying.
    """

    base_pdct: AssetClassProductType3Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType10Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    addtl_sub_pdct: None | AssetClassDetailedSubProductType8Code = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class EnvironmentalCommodityWeather2:
    """
    EnvironmentalCommodityWeather2 Defines commodity sub-product attributes
    of an environmental derivative of type weather.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType3Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType30Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class ExchangeRateBasis1Choice1:
    """
    ExchangeRateBasis1Choice__1 Provides information about the exchange
    rate basis for a foreign exchange transaction.

    :ivar ccy_pair: CurrencyPair Exchange rate basis expressed as a
        currency pair.
    """

    class Meta:
        name = "ExchangeRateBasis1Choice__1"

    ccy_pair: None | ExchangeRateBasis1 = field(
        default=None,
        metadata={
            "name": "CcyPair",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FertilizerCommodityAmmonia2:
    """
    FertilizerCommodityAmmonia2 Defines commodity sub-product attributes of
    a fertilizer derivative of type ammonia.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType5Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType39Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FertilizerCommodityDiammoniumPhosphate2:
    """
    FertilizerCommodityDiammoniumPhosphate2 Defines commodity sub-product
    attributes of a fertilizer derivative of type diammonium phosphate.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType5Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType40Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FertilizerCommodityOther2:
    """
    FertilizerCommodityOther2 Other fertlizer commodity derivative.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType5Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType49Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FertilizerCommodityPotash2:
    """
    FertilizerCommodityPotash2 Defines commodity sub-product attributes of
    a fertilizer derivative of type potash.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType5Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType41Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FertilizerCommoditySulphur2:
    """
    FertilizerCommoditySulphur2 Defines commodity sub-product attributes of
    a fertilizer derivative of type sulphur.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType5Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType42Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FertilizerCommodityUrea2:
    """
    FertilizerCommodityUrea2 Defines commodity sub-product attributes of a
    fertilizer derivative of type urea.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType5Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType43Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FertilizerCommodityUreaAndAmmoniumNitrate2:
    """
    FertilizerCommodityUreaAndAmmoniumNitrate2 Defines commodity
    sub-product attributes of a fertilizer derivative of type urea and
    ammonium nitrate.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType5Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType44Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FinancialPartyClassification2Choice1:
    """
    FinancialPartyClassification2Choice__1 Specifies the classification of
    a financial institution.

    :ivar cd: Code Classification of the business activities of the
        counterparty via a pre-determined code list.
    """

    class Meta:
        name = "FinancialPartyClassification2Choice__1"

    cd: None | FinancialPartySectorType3Code = field(
        default=None,
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FreightCommodityContainerShip2:
    """
    FreightCommodityContainerShip2 Defines commodity sub-product attributes
    of a freight derivative of type container ships.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType4Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType46Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FreightCommodityDry3:
    """
    FreightCommodityDry3 Defines commodity sub-product attributes of a
    freight derivative of type dry.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    :ivar addtl_sub_pdct: AdditionalSubProduct Further subproduct type
        related to instruments that have a non-financial instrument or
        commodity as underlying.
    """

    base_pdct: AssetClassProductType4Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType31Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    addtl_sub_pdct: None | AssetClassDetailedSubProductType33Code = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FreightCommodityOther2:
    """
    FreightCommodityOther2 Other freight commodity derivative.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType4Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType49Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FreightCommodityWet3:
    """
    FreightCommodityWet3 Defines commodity sub-product attributes of a
    freight derivative of type wet.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    :ivar addtl_sub_pdct: AdditionalSubProduct Further subproduct type
        related to instruments that have a non-financial instrument or
        commodity as underlying.
    """

    base_pdct: AssetClassProductType4Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType32Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    addtl_sub_pdct: None | AssetClassDetailedSubProductType34Code = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class GenericIdentification1752:
    """
    GenericIdentification175__2 Information related to an identification,
    for example party identification or account identification.

    :ivar id: Identification Identification assigned by an institution.
    :ivar schme_nm: SchemeName Name of the identification scheme.
    """

    class Meta:
        name = "GenericIdentification175__2"

    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 72,
        }
    )
    schme_nm: HktrpartyScheme = field(
        metadata={
            "name": "SchmeNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class IndustrialProductCommodityConstruction2:
    """
    IndustrialProductCommodityConstruction2 Defines commodity sub-product
    attributes of an industrial product derivative of type construction.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType6Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType33Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class IndustrialProductCommodityManufacturing2:
    """
    IndustrialProductCommodityManufacturing2 Defines commodity sub-product
    attributes of an industrial product derivative of type manufacturing.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType6Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType34Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class InstrumentIdentification6Choice1:
    """
    InstrumentIdentification6Choice__1 Choice between different instrument
    identification schemes.

    :ivar isin: ISIN International Securities Identification Number
        (ISIN). A numbering system designed by the United Nation's
        International Organisation for Standardisation (ISO). The ISIN
        is composed of a 2-character prefix representing the country of
        issue, followed by the national security number (if one exists),
        and a check digit. Each country has a national numbering agency
        that assigns ISIN numbers for securities in that country.
    :ivar othr_id: OtherIdentification Other identification of a
        security assigned by an institution or organisation.
    """

    class Meta:
        name = "InstrumentIdentification6Choice__1"

    isin: None | str = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    othr_id: None | GenericIdentification184 = field(
        default=None,
        metadata={
            "name": "OthrId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class InterestComputationMethodFormat71:
    """
    InterestComputationMethodFormat7__1 Choice between a standard code or
    proprietary code to specify the type of interest computation method.

    :ivar cd: Code Standard code to specify the method used to compute
        accruing interest of a financial instrument.
    """

    class Meta:
        name = "InterestComputationMethodFormat7__1"

    cd: InterestComputationMethod4Code = field(
        metadata={
            "name": "Cd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class InterestRateContractTerm41:
    """
    InterestRateContractTerm4__1 Describes how interest rates are reported.

    :ivar unit: Unit Unit for the rate basis.
    :ivar val: Value Specifies the number of time units (as expressed by
        the payment frequency period) that detemines the frequency at
        which periodic payment dates occur.
    """

    class Meta:
        name = "InterestRateContractTerm4__1"

    unit: None | Frequency13Code1 = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    val: None | Decimal = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )


@dataclass(kw_only=True)
class LegalPersonIdentification11:
    """
    LegalPersonIdentification1__1 Provides the identification of the
    organisation which is a legal person.

    :ivar id: Identification Unique and unambiguous identification of
        the legal person.
    """

    class Meta:
        name = "LegalPersonIdentification1__1"

    id: OrganisationIdentification15Choice1 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class MetalCommodityNonPrecious2:
    """
    MetalCommodityNonPrecious2 Defines commodity sub-product attributes of
    a metal derivative of type non-precious.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    :ivar addtl_sub_pdct: AdditionalSubProduct Further subproduct type
        related to instruments that have a non-financial instrument or
        commodity as underlying.
    """

    base_pdct: AssetClassProductType7Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType15Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    addtl_sub_pdct: None | AssetClassDetailedSubProductType10Code = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class MetalCommodityPrecious2:
    """
    MetalCommodityPrecious2 Defines commodity sub-product attributes of a
    metal derivative of type precious.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    :ivar addtl_sub_pdct: AdditionalSubProduct Further subproduct type
        related to instruments that have a non-financial instrument or
        commodity as underlying.
    """

    base_pdct: AssetClassProductType7Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType16Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    addtl_sub_pdct: None | AssetClassDetailedSubProductType11Code = field(
        default=None,
        metadata={
            "name": "AddtlSubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class NaturalPersonIdentification21:
    """
    NaturalPersonIdentification2__1 Identifies a natural person through
    identification number, name and domicile.

    :ivar id: Identification Unique and unambiguous identification of
        the natural person.
    """

    class Meta:
        name = "NaturalPersonIdentification2__1"

    id: GenericIdentification1751 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class NonFinancialInstitutionSector101:
    """
    NonFinancialInstitutionSector10__1 Provides detailed information
    concerning non financial counterparties.

    :ivar sctr: Sector Taxonomy for non-financial counterparties. The
        categories correspond to the main sections of NACE
        classification as defined in the regulation.
    """

    class Meta:
        name = "NonFinancialInstitutionSector10__1"

    sctr: GenericIdentification1751 = field(
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class OrganisationIdentification383:
    """
    OrganisationIdentification38__3 Identifies an organisation through
    client identification, a name and a domicile.

    :ivar id: Identification Unique and unambiguous identification of
        the organisation.
    """

    class Meta:
        name = "OrganisationIdentification38__3"

    id: GenericIdentification1753 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class OrganisationIdentification384:
    """
    OrganisationIdentification38__4 Identifies an organisation through
    client identification, a name and a domicile.

    :ivar id: Identification Unique and unambiguous identification of
        the organisation.
    """

    class Meta:
        name = "OrganisationIdentification38__4"

    id: GenericIdentification1751 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class PaperCommodityContainerBoard2:
    """
    PaperCommodityContainerBoard2 Defines commodity sub-product attributes
    of a paper derivative of type container board.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType8Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType35Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PaperCommodityNewsprint2:
    """
    PaperCommodityNewsprint2 Defines commodity sub-product attributes of a
    paper derivative of type newsprint.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType8Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType36Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PaperCommodityOther1:
    """
    PaperCommodityOther1 Defines commodity sub-product attributes of a
    paper derivative of type other.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType8Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType49Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PaperCommodityPulp2:
    """
    PaperCommodityPulp2 Defines commodity sub-product attributes of a paper
    derivative of type pulp.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType8Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType37Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PaperCommodityRecoveredPaper3:
    """
    PaperCommodityRecoveredPaper3 Defines commodity sub-product attributes
    of a paper derivative of type recovered paper.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType8Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType50Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PaymentType5Choice1:
    """
    PaymentType5Choice__1 Choice beween a payment type from a predefined
    list and a proprietary payment type.

    :ivar tp: Type Type, or nature, of the payment.
    """

    class Meta:
        name = "PaymentType5Choice__1"

    tp: None | PaymentType4Code = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PolypropyleneCommodityOther2:
    """
    PolypropyleneCommodityOther2 Defines commodity sub-product attributes
    of a propylene derivative of type recovered paper.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType9Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType49Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PolypropyleneCommodityPlastic2:
    """
    PolypropyleneCommodityPlastic2 Defines commodity sub-product attributes
    of a polypropylene derivative of type plastic.

    :ivar base_pdct: BaseProduct Base product for the underlying asset
        class as specified in the classification of commodities
        derivatives table.
    :ivar sub_pdct: SubProduct Sub-product for the underlying asset
        class.
    """

    base_pdct: AssetClassProductType9Code = field(
        metadata={
            "name": "BasePdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sub_pdct: None | AssetClassSubProductType18Code = field(
        default=None,
        metadata={
            "name": "SubPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PortfolioCode5Choice1:
    """
    PortfolioCode5Choice__1 Element is a choice between a known portfolio
    code and a code applicable when the code is unknown.

    :ivar prtfl: Portfolio Unique code determined by the reporting
        counterparty to identify the portfolio if collateral is reported
        on a portfolio basis.
    :ivar no_prtfl: NoPortfolio Collateralisation was performed on a
        transaction level basis or if the collateral portfolio code is
        not known at the time of reporting.
    """

    class Meta:
        name = "PortfolioCode5Choice__1"

    prtfl: None | PortfolioIdentification31 = field(
        default=None,
        metadata={
            "name": "Prtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    no_prtfl: None | NotApplicable1Code = field(
        default=None,
        metadata={
            "name": "NoPrtfl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class QuantityTerm11:
    """
    QuantityTerm1__1 Describes the notional quantity frequency.

    :ivar qty: Quantity Number of units of the financial instrument,
        that is, the nominal value.
    :ivar val: Value Specifies the number of time units (as expressed by
        the frequency period) that determines the frequency at which
        periodic dates occur.
    :ivar tm_unit: TimeUnit Unit for the frequency period.
    """

    class Meta:
        name = "QuantityTerm1__1"

    qty: None | Decimal = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 25,
            "fraction_digits": 5,
        },
    )
    val: None | Decimal = field(
        default=None,
        metadata={
            "name": "Val",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 3,
            "fraction_digits": 0,
        },
    )
    tm_unit: None | Frequency19Code1 = field(
        default=None,
        metadata={
            "name": "TmUnit",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class SupplementaryData1:
    """
    SupplementaryData1 Additional information that can not be captured in
    the structured fields and/or any other specific block.

    :ivar plc_and_nm: PlaceAndName Unambiguous reference to the location
        where the supplementary data must be inserted in the message
        instance.&#13; In the case of XML, this is expressed by a valid
        XPath.
    :ivar envlp: Envelope Technical element wrapping the supplementary
        data.
    """

    plc_and_nm: None | str = field(
        default=None,
        metadata={
            "name": "PlcAndNm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    envlp: SupplementaryDataEnvelope1 = field(
        metadata={
            "name": "Envlp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class TradeConfirmation51:
    """
    TradeConfirmation5__1 Specifies time and type of contract confirmation.

    :ivar tp: Type Specifies whether the contract was confirmed
        electronically or non-electronically.
    """

    class Meta:
        name = "TradeConfirmation5__1"

    tp: TradeConfirmationType1Code = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class TradeNonConfirmation1:
    """
    TradeNonConfirmation1 Identifies contract that is not confirmed.

    :ivar tp: Type Specifies that the contract remains unconfirmed.
    """

    tp: TradeConfirmationType2Code = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class TrancheIndicator3Choice1:
    """
    TrancheIndicator3Choice__1 Indication whether a derivative contract is
    tranched.

    :ivar trnchd: Tranched Indication that derivative contract is
        tranched.
    """

    class Meta:
        name = "TrancheIndicator3Choice__1"

    trnchd: None | Tranche3 = field(
        default=None,
        metadata={
            "name": "Trnchd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class UniqueProductIdentifier2Choice1:
    """
    UniqueProductIdentifier2Choice__1 Element is a choice between a
    standard identifier and a proprietary code.

    :ivar id: Identification Identification through a unique product
        identifier.
    :ivar prtry: Proprietary Product identifier expressed in a
        proprietary notation.
    """

    class Meta:
        name = "UniqueProductIdentifier2Choice__1"

    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 52,
        },
    )
    prtry: None | GenericIdentification1851 = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class UniqueTransactionIdentifier2Choice1:
    """
    UniqueTransactionIdentifier2Choice__1 Element is a choice between a
    standard identifier and a proprietary code.

    :ivar unq_tx_idr: UniqueTransactionIdentifier Unique trade
        identifier (UTI) as agreed with the counterparty.
    :ivar prtry: Proprietary Trade identifier expressed in a proprietary
        notation.
    """

    class Meta:
        name = "UniqueTransactionIdentifier2Choice__1"

    unq_tx_idr: None | str = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    prtry: None | GenericIdentification1754 = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class UniqueTransactionIdentifier3Choice1:
    """
    UniqueTransactionIdentifier3Choice__1 Element is a choice between a
    standard identifier and a proprietary code.

    :ivar unq_tx_idr: UniqueTransactionIdentifier Unique trade
        identifier (UTI) as agreed with the counterparty.
    :ivar prtry: Proprietary Trade identifier expressed in a proprietary
        notation.
    """

    class Meta:
        name = "UniqueTransactionIdentifier3Choice__1"

    unq_tx_idr: None | str = field(
        default=None,
        metadata={
            "name": "UnqTxIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}",
        },
    )
    prtry: None | GenericIdentification1754 = field(
        default=None,
        metadata={
            "name": "Prtry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AssetClassCommodityAgricultural6Choice:
    """
    AssetClassCommodityAgricultural6Choice Defines commodity attributes of
    a derivative where the type is agricultural.

    :ivar grn_oil_seed: GrainOilSeed Grain oil seed agricultural
        commodity derivative.
    :ivar soft: Soft Soft agricultural commodity derivative.
    :ivar ptt: Potato Potato agricultural commodity derivative.
    :ivar olv_oil: OliveOil Olive oil agricultural commodity derivative.
    :ivar dairy: Dairy Dairy agricultural commodity derivative.
    :ivar frstry: Forestry Forestry agricultural commodity derivative.
    :ivar sfd: Seafood Seafood agricultural commodity derivative.
    :ivar live_stock: LiveStock Livestock agricultural commodity
        derivative.
    :ivar grn: Grain Grain agricultural commodity derivative.
    :ivar othr: Other Other agricultural commodity derivative.
    """

    grn_oil_seed: None | AgriculturalCommodityOilSeed2 = field(
        default=None,
        metadata={
            "name": "GrnOilSeed",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    soft: None | AgriculturalCommoditySoft2 = field(
        default=None,
        metadata={
            "name": "Soft",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ptt: None | AgriculturalCommodityPotato2 = field(
        default=None,
        metadata={
            "name": "Ptt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    olv_oil: None | AgriculturalCommodityOliveOil3 = field(
        default=None,
        metadata={
            "name": "OlvOil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    dairy: None | AgriculturalCommodityDairy2 = field(
        default=None,
        metadata={
            "name": "Dairy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    frstry: None | AgriculturalCommodityForestry2 = field(
        default=None,
        metadata={
            "name": "Frstry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    sfd: None | AgriculturalCommoditySeafood2 = field(
        default=None,
        metadata={
            "name": "Sfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    live_stock: None | AgriculturalCommodityLiveStock2 = field(
        default=None,
        metadata={
            "name": "LiveStock",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    grn: None | AgriculturalCommodityGrain3 = field(
        default=None,
        metadata={
            "name": "Grn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr: None | AgriculturalCommodityOther2 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AssetClassCommodityEnergy3Choice:
    """
    AssetClassCommodityEnergy3Choice Defines commodity attributes of a
    derivative where the type is energy.

    :ivar elctrcty: Electricity Definition of Electricity energy
        commodity derivative.
    :ivar ntrl_gas: NaturalGas Definition of Natural Gas energy
        commodity derivative.
    :ivar oil: Oil Definition of Oil energy commodity derivative.
    :ivar coal: Coal Definition of Coal energy commodity derivative.
    :ivar intr_nrgy: InterEnergy Inter energy commodity derivative.
    :ivar rnwbl_nrgy: RenewableEnergy Renewable energy commodity
        derivative.
    :ivar lght_end: LightEnd Light end energy commodity derivative.
    :ivar dstllts: Distillates Distillates energy commodity derivative.
    :ivar othr: Other Other energy commodity derivative.
    """

    elctrcty: None | EnergyCommodityElectricity2 = field(
        default=None,
        metadata={
            "name": "Elctrcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ntrl_gas: None | EnergyCommodityNaturalGas3 = field(
        default=None,
        metadata={
            "name": "NtrlGas",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    oil: None | EnergyCommodityOil3 = field(
        default=None,
        metadata={
            "name": "Oil",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    coal: None | EnergyCommodityCoal2 = field(
        default=None,
        metadata={
            "name": "Coal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    intr_nrgy: None | EnergyCommodityInterEnergy2 = field(
        default=None,
        metadata={
            "name": "IntrNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    rnwbl_nrgy: None | EnergyCommodityRenewableEnergy2 = field(
        default=None,
        metadata={
            "name": "RnwblNrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    lght_end: None | EnergyCommodityLightEnd2 = field(
        default=None,
        metadata={
            "name": "LghtEnd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    dstllts: None | EnergyCommodityDistillates2 = field(
        default=None,
        metadata={
            "name": "Dstllts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr: None | EnergyCommodityOther2 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AssetClassCommodityEnvironmental3Choice:
    """
    AssetClassCommodityEnvironmental3Choice Defines commodity attributes of
    a derivative where the type is environmental.

    :ivar emssns: Emissions Emissions environmental commodity
        derivative.
    :ivar wthr: Weather Weather environmental commodity derivative.
    :ivar crbn_rltd: CarbonRelated Carbon related environmental
        commodity derivative.
    :ivar othr: Other Other environmental commodity derivative.
    """

    emssns: None | EnvironmentalCommodityEmission3 = field(
        default=None,
        metadata={
            "name": "Emssns",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    wthr: None | EnvironmentalCommodityWeather2 = field(
        default=None,
        metadata={
            "name": "Wthr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    crbn_rltd: None | EnvironmentalCommodityCarbonRelated2 = field(
        default=None,
        metadata={
            "name": "CrbnRltd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr: None | EnvironmentCommodityOther2 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AssetClassCommodityFertilizer4Choice:
    """
    AssetClassCommodityFertilizer4Choice Defines commodity attributes of a
    derivative where the type is fertilizer.

    :ivar ammn: Ammonia Ammonia fertilizer commodity derivative.
    :ivar dmmnm_phspht: DiammoniumPhosphate Diammonium phosphate
        fertilizer commodity derivative.
    :ivar ptsh: Potash Potash fertilizer commodity derivative.
    :ivar slphr: Sulphur Sulphur fertilizer commodity derivative.
    :ivar urea: Urea Urea fertilizer commodity derivative.
    :ivar urea_and_ammnm_ntrt: UreaAndAmmoniumNitrate Urea and ammonium
        nitrate fertilizer commodity derivative.
    :ivar othr: Other Other fertilizer commodity derivative.
    """

    ammn: None | FertilizerCommodityAmmonia2 = field(
        default=None,
        metadata={
            "name": "Ammn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    dmmnm_phspht: None | FertilizerCommodityDiammoniumPhosphate2 = field(
        default=None,
        metadata={
            "name": "DmmnmPhspht",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ptsh: None | FertilizerCommodityPotash2 = field(
        default=None,
        metadata={
            "name": "Ptsh",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    slphr: None | FertilizerCommoditySulphur2 = field(
        default=None,
        metadata={
            "name": "Slphr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    urea: None | FertilizerCommodityUrea2 = field(
        default=None,
        metadata={
            "name": "Urea",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    urea_and_ammnm_ntrt: None | FertilizerCommodityUreaAndAmmoniumNitrate2 = (
        field(
            default=None,
            metadata={
                "name": "UreaAndAmmnmNtrt",
                "type": "Element",
                "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            },
        )
    )
    othr: None | FertilizerCommodityOther2 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AssetClassCommodityFreight4Choice:
    """
    AssetClassCommodityFreight4Choice Defines commodity attributes of a
    derivative where the type is freight.

    :ivar dry: Dry Dry freight commodity derivative.
    :ivar wet: Wet Wet freight commodity derivative.
    :ivar cntnr_ship: ContainerShip Container ship freight commodity
        derivative.
    :ivar othr: Other Other freight commodity derivative.
    """

    dry: None | FreightCommodityDry3 = field(
        default=None,
        metadata={
            "name": "Dry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    wet: None | FreightCommodityWet3 = field(
        default=None,
        metadata={
            "name": "Wet",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    cntnr_ship: None | FreightCommodityContainerShip2 = field(
        default=None,
        metadata={
            "name": "CntnrShip",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr: None | FreightCommodityOther2 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AssetClassCommodityIndustrialProduct2Choice:
    """
    AssetClassCommodityIndustrialProduct2Choice Defines commodity
    attributes of a derivative where the type is industrial product.

    :ivar cnstrctn: Construction Construction related industrial product
        commodity derivative.
    :ivar manfctg: Manufacturing Manufacturing related industrial
        product commodity derivative.
    """

    cnstrctn: None | IndustrialProductCommodityConstruction2 = field(
        default=None,
        metadata={
            "name": "Cnstrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    manfctg: None | IndustrialProductCommodityManufacturing2 = field(
        default=None,
        metadata={
            "name": "Manfctg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AssetClassCommodityMetal2Choice:
    """
    AssetClassCommodityMetal2Choice Defines commodity attributes of a
    derivative where the type is metal.

    :ivar non_prcs: NonPrecious Non-precious metal commodity derivative.
    :ivar prcs: Precious Precious metal commodity derivative.
    """

    non_prcs: None | MetalCommodityNonPrecious2 = field(
        default=None,
        metadata={
            "name": "NonPrcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    prcs: None | MetalCommodityPrecious2 = field(
        default=None,
        metadata={
            "name": "Prcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AssetClassCommodityPaper5Choice:
    """
    AssetClassCommodityPaper5Choice Defines commodity attributes of a
    derivative where the type is paper.

    :ivar cntnr_brd: ContainerBoard Container board commodity
        derivative.
    :ivar nwsprnt: Newsprint Newsprint commodity derivative.
    :ivar pulp: Pulp Pulp commodity derivative.
    :ivar rcvrd_ppr: RecoveredPaper Recovered paper commodity
        derivative.
    :ivar othr: Other Other commodity derivative
    """

    cntnr_brd: None | PaperCommodityContainerBoard2 = field(
        default=None,
        metadata={
            "name": "CntnrBrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    nwsprnt: None | PaperCommodityNewsprint2 = field(
        default=None,
        metadata={
            "name": "Nwsprnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    pulp: None | PaperCommodityPulp2 = field(
        default=None,
        metadata={
            "name": "Pulp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    rcvrd_ppr: None | PaperCommodityRecoveredPaper3 = field(
        default=None,
        metadata={
            "name": "RcvrdPpr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr: None | PaperCommodityOther1 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class AssetClassCommodityPolypropylene4Choice:
    """
    AssetClassCommodityPolypropylene4Choice Defines commodity attributes of
    a derivative where the type is polypropylene.

    :ivar plstc: Plastic Plastic commodity derivative.
    :ivar othr: Other Other commodity derivative
    """

    plstc: None | PolypropyleneCommodityPlastic2 = field(
        default=None,
        metadata={
            "name": "Plstc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr: None | PolypropyleneCommodityOther2 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class BasketConstituents31:
    """
    BasketConstituents3__1 Choice between ISIN and an alternative format
    for the identification of a financial instrument.

    ISIN is the preferred format.

    :ivar instrm_id: InstrumentIdentification Proprietary identification
        of a security assigned by an institution or organisation.
    :ivar qty: Quantity Indicates the number of units of a particular
        constituent in a custom basket.
    :ivar unit_of_measr: UnitOfMeasure Specifies the unit of measure in
        which the number of units of a particular custom basket
        constituent is expressed.
    """

    class Meta:
        name = "BasketConstituents3__1"

    instrm_id: InstrumentIdentification6Choice1 = field(
        metadata={
            "name": "InstrmId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    qty: None | Decimal = field(
        default=None,
        metadata={
            "name": "Qty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 18,
            "fraction_digits": 13,
        },
    )
    unit_of_measr: None | UnitOfMeasure8Choice1 = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class ContractValuationData81:
    """
    ContractValuationData8__1 Information related to contract valuation.

    :ivar ctrct_val: ContractValue Specifies the current value of the
        outstanding contract.&#13;
    :ivar tm_stmp: TimeStamp Indicates the date and time of the last
        valuation marked to market provided by the central counterparty
        (CCP) or calculated using the current or last available market
        price of the inputs.
    :ivar tp: Type Indicates the source and method used for the
        valuation of the transaction by the reporting counterparty.&#13;
        &#13; Usage:&#13; If at least one valuation input is used that
        is classified as mark-to-model, the whole valuation is
        classified as mark-to-model.&#13; If only inputs are used that
        are classified as mark-to-market; the whole valuation is
        classified as mark-to-market.&#13;&#13;
    :ivar dlta: Delta Specifies the ratio of the absolute change in
        price of a derivative transaction to the change in price of the
        underlier, at the time a new transaction is reported or when a
        change in the notional amount is reported.
    """

    class Meta:
        name = "ContractValuationData8__1"

    ctrct_val: AmountAndDirection1091 = field(
        metadata={
            "name": "CtrctVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tm_stmp: XmlDateTime = field(
        metadata={
            "name": "TmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tp: ValuationType1Code = field(
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    dlta: None | Decimal = field(
        default=None,
        metadata={
            "name": "Dlta",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 25,
            "fraction_digits": 5,
        },
    )


@dataclass(kw_only=True)
class CreditDerivative41:
    """
    CreditDerivative4__1 Information related specifically to credit
    derivatives attributes.

    :ivar snrty: Seniority Classification of seniority in case of
        contract on index or on a single name entity.
    :ivar ref_pty: ReferenceParty Designation of the underlying
        reference obligation.
    :ivar srs: Series Indicates the series number of the composition of
        the index if applicable.
    :ivar vrsn: Version New version of a series is issued if one of the
        constituents defaults and the index has to be re-weighted to
        account for the new number of total constituents within the
        index.
    :ivar indx_fctr: IndexFactor Factor to apply to the actual notional
        to adjust it to all the previous credit events in the index
        series. &#13; &#13; Usage: The figure varies between 0 and 100.
    :ivar trch: Tranche Indicates whether the derivative contract is
        tranched or not.
    """

    class Meta:
        name = "CreditDerivative4__1"

    snrty: None | DebtInstrumentSeniorityType2Code = field(
        default=None,
        metadata={
            "name": "Snrty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ref_pty: None | DerivativePartyIdentification1Choice = field(
        default=None,
        metadata={
            "name": "RefPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    srs: None | Decimal = field(
        default=None,
        metadata={
            "name": "Srs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    vrsn: None | Decimal = field(
        default=None,
        metadata={
            "name": "Vrsn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )
    indx_fctr: None | Decimal = field(
        default=None,
        metadata={
            "name": "IndxFctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    trch: None | TrancheIndicator3Choice1 = field(
        default=None,
        metadata={
            "name": "Trch",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class CurrencyExchange221:
    """
    CurrencyExchange22__1 Describes the details of the currency exchange.

    :ivar xchg_rate: ExchangeRate Indicates the exchange rate between
        the two currencies specified in the derivative transaction
        agreed by the counterparties at the inception of the
        transaction,  expressed as the rate of exchange from converting
        the unit currency into the quoted currency.
    :ivar xchg_rate_bsis: ExchangeRateBasis Indicates, for equity
        options, commodity options and similar products, the currency in
        which the strike price is denominated.  In case of foreign
        exchange options, indicates the currency pair and order in which
        the strike price is expressed as unit currency and quoted
        currency.
    """

    class Meta:
        name = "CurrencyExchange22__1"

    xchg_rate: None | Decimal = field(
        default=None,
        metadata={
            "name": "XchgRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 18,
            "fraction_digits": 13,
        },
    )
    xchg_rate_bsis: None | ExchangeRateBasis1Choice1 = field(
        default=None,
        metadata={
            "name": "XchgRateBsis",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class Direction4Choice1:
    """
    Direction4Choice__1 Choice between elements indicating the direction of
    the derivative transaction.

    :ivar drctn: Direction Identifies whether the reporting counterparty
        is the payer (Taker) or the receiver (Maker).&#13; &#13;
        Usage:&#13; DirectionOfTheFirstLeg should be used for most swaps
        and swap-like contracts including interest rate swaps, credit
        total return swaps, and equity swaps (except for credit default
        swaps, variance, volatility, and correlation swaps) as well as
        for the foreign exchange swaps, forwards and non-deliverable
        forwards.&#13;
    :ivar ctr_pty_sd: CounterpartySide Identifies whether the reporting
        counterparty is the buyer or the seller as determined at the
        time of transaction.
    """

    class Meta:
        name = "Direction4Choice__1"

    drctn: None | Direction21 = field(
        default=None,
        metadata={
            "name": "Drctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ctr_pty_sd: None | OptionParty1Code = field(
        default=None,
        metadata={
            "name": "CtrPtySd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FinancialInstitutionSector11:
    """
    FinancialInstitutionSector1__1 Provides detailed information concerning
    financial counterparties.

    :ivar sctr: Sector Specifies the nature of the counterparty business
        activities.
    """

    class Meta:
        name = "FinancialInstitutionSector1__1"

    sctr: FinancialPartyClassification2Choice1 = field(
        metadata={
            "name": "Sctr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class InterestRateFrequency3Choice1:
    """
    InterestRateFrequency3Choice__1 Describes frequency of payments for
    interest rates, either using term notation or a proprietary notation.

    :ivar term: Term Frequency expressed in tenor notation.
    """

    class Meta:
        name = "InterestRateFrequency3Choice__1"

    term: None | InterestRateContractTerm41 = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class MarginPortfolio41:
    """
    MarginPortfolio4__1 Specifies the margin portfolio unique codes.

    :ivar initl_mrgn_prtfl_cd: InitialMarginPortfolioCode Specifies the
        unique code assigned by the reporting counterparty to the
        portfolio if the collateral is posted on a portfolio basis.&#13;
        &#13; Usage:&#13; NoPortfolio is reported if the
        collateralisation was performed on a transaction level basis, or
        if there is no collateral agreement or if no collateral is
        posted or received.
    :ivar vartn_mrgn_prtfl_cd: VariationMarginPortfolioCode Specifies
        the unique code assigned by the reporting counterparty to the
        portfolio if the collateral is posted on a portfolio basis.&#13;
        &#13; Usage:&#13; NoPortfolio is reported if the
        collateralisation was performed on a transaction level basis, or
        if there is no collateral agreement or if no collateral is
        posted or received.
    """

    class Meta:
        name = "MarginPortfolio4__1"

    initl_mrgn_prtfl_cd: None | PortfolioCode5Choice1 = field(
        default=None,
        metadata={
            "name": "InitlMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    vartn_mrgn_prtfl_cd: None | PortfolioCode5Choice1 = field(
        default=None,
        metadata={
            "name": "VartnMrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class NaturalPersonIdentification31:
    """
    NaturalPersonIdentification3__1 Identifies a natural person through
    identification number, name and domicile.

    :ivar id: Identification Unique and unambiguous identification of
        the natural person.
    :ivar ctry: Country Code of country of residence of a natural
        person.
    """

    class Meta:
        name = "NaturalPersonIdentification3__1"

    id: NaturalPersonIdentification21 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    ctry: None | str = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass(kw_only=True)
class NaturalPersonIdentification32:
    """
    NaturalPersonIdentification3__2 Identifies a natural person through
    identification number, name and domicile.

    :ivar id: Identification Unique and unambiguous identification of
        the natural person.
    """

    class Meta:
        name = "NaturalPersonIdentification3__2"

    id: NaturalPersonIdentification21 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class OrganisationIdentification15Choice4:
    """
    OrganisationIdentification15Choice__4 Provides the identification of
    the organisation.

    :ivar lei: LEI Identification is done through the use of legal
        entity identifier code.
    :ivar othr: Other Unique identification of an organisation, using a
        client code or a business identification code.
    """

    class Meta:
        name = "OrganisationIdentification15Choice__4"

    lei: None | str = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: None | OrganisationIdentification383 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class OrganisationIdentification15Choice5:
    """
    OrganisationIdentification15Choice__5 Provides the identification of
    the organisation.

    :ivar othr: Other Unique identification of an organisation, using a
        client code or a business identification code.
    """

    class Meta:
        name = "OrganisationIdentification15Choice__5"

    othr: None | OrganisationIdentification384 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class OrganisationIdentification381:
    """
    OrganisationIdentification38__1 Identifies an organisation through
    client identification, a name and a domicile.

    :ivar id: Identification Unique and unambiguous identification of
        the organisation.
    :ivar nm: Name Indicates the name of the organisation.
    """

    class Meta:
        name = "OrganisationIdentification38__1"

    id: GenericIdentification1752 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    nm: None | str = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 105,
        },
    )


@dataclass(kw_only=True)
class OrganisationIdentification382:
    """
    OrganisationIdentification38__2 Identifies an organisation through
    client identification, a name and a domicile.

    :ivar id: Identification Unique and unambiguous identification of
        the organisation.
    """

    class Meta:
        name = "OrganisationIdentification38__2"

    id: GenericIdentification1752 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class PartyIdentification248Choice1:
    """
    PartyIdentification248Choice__1 Provides the identification of the
    organisation.

    :ivar lgl: Legal Party is a legal person.
    """

    class Meta:
        name = "PartyIdentification248Choice__1"

    lgl: None | LegalPersonIdentification11 = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class QuantityOrTerm1Choice1:
    """
    QuantityOrTerm1Choice__1 Indicates the schedule or frequency of the
    derivative transactions.

    :ivar schdl_prd: SchedulePeriod Specifies the effective date and end
        date of the schedule for derivative transactions negotiated in
        non-monetary amounts with a notional quantity varying throughout
        the life of the transaction.
    :ivar term: Term Frequency expressed in tenor notation.
    """

    class Meta:
        name = "QuantityOrTerm1Choice__1"

    schdl_prd: list[Schedule101] = field(
        default_factory=list,
        metadata={
            "name": "SchdlPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "max_occurs": 600,
        },
    )
    term: None | QuantityTerm11 = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class Schedule111:
    """
    Schedule11__1 Indicates the unadjusted effective and end date of the
    schedule.

    :ivar uadjstd_fctv_dt: UnadjustedEffectiveDate Indicates the
        unadjusted date at which obligations under the  derivative
        transaction come into effect, as included in the confirmation.
    :ivar uadjstd_end_dt: UnadjustedEndDate Indicates the end date
        agreed in the derivative transaction without adjustment.
    :ivar amt: Amount Indicates the price per derivative excluding,
        where applicable, commission and accrued interest.
    """

    class Meta:
        name = "Schedule11__1"

    uadjstd_fctv_dt: XmlDate = field(
        metadata={
            "name": "UadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    uadjstd_end_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "UadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    amt: AmountAndDirection1062 = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class SecuritiesTransactionPrice17Choice1:
    """
    SecuritiesTransactionPrice17Choice__1 Choice to define the price of the
    securities transaction.

    :ivar mntry_val: MonetaryValue Indicates that price is expressed as
        a monetary value.
    :ivar dcml: Decimal
    """

    class Meta:
        name = "SecuritiesTransactionPrice17Choice__1"

    mntry_val: None | AmountAndDirection1061 = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    dcml: None | Decimal = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass(kw_only=True)
class SecuritiesTransactionPrice20Choice1:
    """
    SecuritiesTransactionPrice20Choice__1 Choice to define the price of the
    securities transaction.

    :ivar mntry_val: MonetaryValue Indicates that price is expressed as
        a monetary value.
    :ivar dcml: Decimal
    :ivar bsis_pt_sprd: BasisPointSpread Used to express differences in
        interest rates, for example, a difference of 0.10% is equivalent
        to a change of 10 basis points.
    """

    class Meta:
        name = "SecuritiesTransactionPrice20Choice__1"

    mntry_val: None | AmountAndDirection1061 = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    dcml: None | Decimal = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )
    bsis_pt_sprd: None | Decimal = field(
        default=None,
        metadata={
            "name": "BsisPtSprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 5,
            "fraction_digits": 0,
        },
    )


@dataclass(kw_only=True)
class SecuritiesTransactionPrice23Choice1:
    """
    SecuritiesTransactionPrice23Choice__1 Choice to define the price of the
    securities transaction.

    :ivar mntry_val: MonetaryValue Indicates that price is expressed as
        a monetary value.
    :ivar dcml: Decimal
    """

    class Meta:
        name = "SecuritiesTransactionPrice23Choice__1"

    mntry_val: None | AmountAndDirection1061 = field(
        default=None,
        metadata={
            "name": "MntryVal",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    dcml: None | Decimal = field(
        default=None,
        metadata={
            "name": "Dcml",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 11,
            "fraction_digits": 10,
        },
    )


@dataclass(kw_only=True)
class SecurityIdentification461:
    """
    SecurityIdentification46__1 Choice between ISIN and an alternative
    format for the identification of a financial instrument.

    ISIN is the preferred format.

    :ivar unq_pdct_idr: UniqueProductIdentifier Identification through a
        unique product identifier.
    :ivar pdct_desc: ProductDescription Specifies a human readable
        description of the product.
    """

    class Meta:
        name = "SecurityIdentification46__1"

    unq_pdct_idr: None | UniqueProductIdentifier2Choice1 = field(
        default=None,
        metadata={
            "name": "UnqPdctIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    pdct_desc: None | str = field(
        default=None,
        metadata={
            "name": "PdctDesc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 255,
        },
    )


@dataclass(kw_only=True)
class TradeConfirmation4Choice1:
    """
    TradeConfirmation4Choice__1 Information regarding the confirmation of
    the contract.

    :ivar confd: Confirmed Indicates the type of contract confirmation.
    :ivar non_confd: NonConfirmed Indicates that contract was not
        confirmed.
    """

    class Meta:
        name = "TradeConfirmation4Choice__1"

    confd: None | TradeConfirmation51 = field(
        default=None,
        metadata={
            "name": "Confd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    non_confd: None | TradeNonConfirmation1 = field(
        default=None,
        metadata={
            "name": "NonConfd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeTransaction505:
    """
    TradeTransaction50__5 Provides details of the trade transaction.

    :ivar tx_id: TransactionIdentification Choice between a Unique
        Transaction Identifier (UTI) or a proprietary identifier as
        agreed with the counterparty.
    """

    class Meta:
        name = "TradeTransaction50__5"

    tx_id: UniqueTransactionIdentifier2Choice1 = field(
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class TradeTransaction506:
    """
    TradeTransaction50__6 Provides details of the trade transaction.

    :ivar tx_id: TransactionIdentification Choice between a Unique
        Transaction Identifier (UTI) or a proprietary identifier as
        agreed with the counterparty.
    :ivar deriv_evt: DerivativeEvent Indication of the derivative event
        of the transaction.
    """

    class Meta:
        name = "TradeTransaction50__6"

    tx_id: UniqueTransactionIdentifier2Choice1 = field(
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    deriv_evt: None | DerivativeEvent65 = field(
        default=None,
        metadata={
            "name": "DerivEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeTransaction507:
    """
    TradeTransaction50__7 Provides details of the trade transaction.

    :ivar tx_id: TransactionIdentification Choice between a Unique
        Transaction Identifier (UTI) or a proprietary identifier as
        agreed with the counterparty.
    :ivar deriv_evt: DerivativeEvent Indication of the derivative event
        of the transaction.
    """

    class Meta:
        name = "TradeTransaction50__7"

    tx_id: UniqueTransactionIdentifier2Choice1 = field(
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    deriv_evt: DerivativeEvent66 = field(
        metadata={
            "name": "DerivEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class AssetClassCommodity7Choice:
    """
    AssetClassCommodity7Choice Choice to define commodity specific
    attributes of a derivative.

    :ivar agrcltrl: Agricultural Agricultural commodities.
    :ivar nrgy: Energy Energy commodities.
    :ivar envttl: Environmental Environmental commodities.
    :ivar frtlzr: Fertilizer Fertilizer commodities.
    :ivar frght: Freight Freight commodities.
    :ivar indx: Index Indicates the index type of commodities.
    :ivar indstrl_pdct: IndustrialProduct Industrial Product
        commodities.
    :ivar infltn: Inflation Inflation commodities.
    :ivar metl: Metal Metal commodities.
    :ivar multi_cmmdty_extc: MultiCommodityExotic Multi Commodity Exotic
    :ivar offcl_ecnmc_sttstcs: OfficialEconomicStatistics Official
        Economic Statistics commodities.
    :ivar othr: Other Other commodities.
    :ivar othr_c10: OtherC10 Other C10 commodities.
    :ivar ppr: Paper Paper commodities.
    :ivar plprpln: Polypropylene Polypropylene commodities.
    """

    agrcltrl: None | AssetClassCommodityAgricultural6Choice = field(
        default=None,
        metadata={
            "name": "Agrcltrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    nrgy: None | AssetClassCommodityEnergy3Choice = field(
        default=None,
        metadata={
            "name": "Nrgy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    envttl: None | AssetClassCommodityEnvironmental3Choice = field(
        default=None,
        metadata={
            "name": "Envttl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    frtlzr: None | AssetClassCommodityFertilizer4Choice = field(
        default=None,
        metadata={
            "name": "Frtlzr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    frght: None | AssetClassCommodityFreight4Choice = field(
        default=None,
        metadata={
            "name": "Frght",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    indx: None | AssetClassCommodityIndex1 = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    indstrl_pdct: None | AssetClassCommodityIndustrialProduct2Choice = field(
        default=None,
        metadata={
            "name": "IndstrlPdct",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    infltn: None | AssetClassCommodityInflation1 = field(
        default=None,
        metadata={
            "name": "Infltn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    metl: None | AssetClassCommodityMetal2Choice = field(
        default=None,
        metadata={
            "name": "Metl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    multi_cmmdty_extc: None | AssetClassCommodityMultiCommodityExotic1 = field(
        default=None,
        metadata={
            "name": "MultiCmmdtyExtc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    offcl_ecnmc_sttstcs: (
        None | AssetClassCommodityOfficialEconomicStatistics1
    ) = field(
        default=None,
        metadata={
            "name": "OffclEcnmcSttstcs",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr: None | AssetClassCommodityOther1 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr_c10: None | AssetClassCommodityC10Other1 = field(
        default=None,
        metadata={
            "name": "OthrC10",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ppr: None | AssetClassCommodityPaper5Choice = field(
        default=None,
        metadata={
            "name": "Ppr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    plprpln: None | AssetClassCommodityPolypropylene4Choice = field(
        default=None,
        metadata={
            "name": "Plprpln",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class CollateralPortfolioCode6Choice1:
    """
    CollateralPortfolioCode6Choice__1 Specifies the unique codes
    identifying the portfolio.

    :ivar mrgn_prtfl_cd: MarginPortfolioCode Specifies the unique code
        assigned by the reporting counterparty to the margin portfolio
        if the collateral is posted on a margin portfolio basis.
    """

    class Meta:
        name = "CollateralPortfolioCode6Choice__1"

    mrgn_prtfl_cd: None | MarginPortfolio41 = field(
        default=None,
        metadata={
            "name": "MrgnPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class CommonTradeDataReport715:
    """
    CommonTradeDataReport71__5 Information related to contract and
    transaction details.

    :ivar tx_data: TransactionData Data related to a trade transaction.
    """

    class Meta:
        name = "CommonTradeDataReport71__5"

    tx_data: TradeTransaction505 = field(
        metadata={
            "name": "TxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class CommonTradeDataReport716:
    """
    CommonTradeDataReport71__6 Information related to contract and
    transaction details.

    :ivar ctrct_data: ContractData Data related to a trade contract.
    :ivar tx_data: TransactionData Data related to a trade transaction.
    """

    class Meta:
        name = "CommonTradeDataReport71__6"

    ctrct_data: ContractType152 = field(
        metadata={
            "name": "CtrctData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tx_data: TradeTransaction506 = field(
        metadata={
            "name": "TxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class CommonTradeDataReport717:
    """
    CommonTradeDataReport71__7 Information related to contract and
    transaction details.

    :ivar ctrct_data: ContractData Data related to a trade contract.
    :ivar tx_data: TransactionData Data related to a trade transaction.
    """

    class Meta:
        name = "CommonTradeDataReport71__7"

    ctrct_data: ContractType152 = field(
        metadata={
            "name": "CtrctData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tx_data: TradeTransaction507 = field(
        metadata={
            "name": "TxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class Counterparty452:
    """
    Counterparty45__2 Information related to counterparty identification.

    :ivar id: Identification Unique code identifying the reporting
        counterparty of the contract.
    """

    class Meta:
        name = "Counterparty45__2"

    id: PartyIdentification248Choice1 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class CounterpartyTradeNature15Choice1:
    """
    CounterpartyTradeNature15Choice__1 Nature of the counterparty's company
    activities.

    :ivar fi: FinancialInstitution Indicates that counterparty is a
        financial institution.
    :ivar nfi: NonFinancialInstitution Indicates that counterparty is a
        non financial institution.
    :ivar cntrl_cntr_pty: CentralCounterParty Indicates that reporting
        party is a central counterparty.
    :ivar othr: Other Indicates that reporting party is other type of
        counterparty.
    """

    class Meta:
        name = "CounterpartyTradeNature15Choice__1"

    fi: None | FinancialInstitutionSector11 = field(
        default=None,
        metadata={
            "name": "FI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    nfi: None | NonFinancialInstitutionSector101 = field(
        default=None,
        metadata={
            "name": "NFI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    cntrl_cntr_pty: None | NoReasonCode = field(
        default=None,
        metadata={
            "name": "CntrlCntrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr: None | NoReasonCode = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class CustomBasket41:
    """
    CustomBasket4__1 Identification of constituents for a basket of
    indexes.

    :ivar strr: Structurer Identification of the structurer of the
        customer basket.
    :ivar id: Identification Identifier of the custom basket assigned by
        the structurer allowing to link the constituents of the basket
        of indexes.
    :ivar cnsttnts: Constituents Identifier of the underliers that
        represent the constituents of a custom basket.
    """

    class Meta:
        name = "CustomBasket4__1"

    strr: None | str = field(
        default=None,
        metadata={
            "name": "Strr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 52,
        },
    )
    cnsttnts: list[BasketConstituents31] = field(
        default_factory=list,
        metadata={
            "name": "Cnsttnts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "max_occurs": 600,
        },
    )


@dataclass(kw_only=True)
class FixedRate101:
    """
    FixedRate10__1 Fixed rate related information.

    :ivar rate: Rate Indicates the per annum rate of the fixed leg(s) of
        an interest rate contract.
    :ivar day_cnt: DayCount Identifies the computation method that
        determines how interest payments are calculated. It is used to
        compute the year fraction of the calculation period, and
        indicates the number of days in the calculation period divided
        by the number of days in the year.
    :ivar pmt_frqcy: PaymentFrequency Specifies the time unit associated
        with the frequency of payments.
    """

    class Meta:
        name = "FixedRate10__1"

    rate: None | SecuritiesTransactionPrice14Choice1 = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    day_cnt: None | InterestComputationMethodFormat71 = field(
        default=None,
        metadata={
            "name": "DayCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    pmt_frqcy: None | InterestRateFrequency3Choice1 = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class FloatingRate131:
    """
    FloatingRate13__1 Floating rate related information.

    :ivar id: Identification Identifier of the security subject of the
        transaction
    :ivar nm: Name The full name of the interest rate as assigned by the
        index provider.
    :ivar rate: Rate Indication of the floating rate used.
    :ivar ref_prd: ReferencePeriod Information related to reference
        period.
    :ivar sprd: Spread Indicates a margin, over or under an index, which
        determines a price or a rate for each leg of a derivative
        transaction with periodic payments; or a difference between two
        floating leg indexes.
    :ivar day_cnt: DayCount Identifies the computation method that
        determines how interest payments are calculated. It is used to
        compute the year fraction of the calculation period, and
        indicates the number of days in the calculation period divided
        by the number of days in the year.
    :ivar pmt_frqcy: PaymentFrequency Specifies the time unit associated
        with the frequency of payments.
    """

    class Meta:
        name = "FloatingRate13__1"

    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    nm: None | str = field(
        default=None,
        metadata={
            "name": "Nm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 350,
        },
    )
    rate: None | FloatingRateIdentification8Choice1 = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ref_prd: None | InterestRateContractTerm41 = field(
        default=None,
        metadata={
            "name": "RefPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    sprd: None | SecuritiesTransactionPrice20Choice1 = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    day_cnt: None | InterestComputationMethodFormat71 = field(
        default=None,
        metadata={
            "name": "DayCnt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    pmt_frqcy: None | InterestRateFrequency3Choice1 = field(
        default=None,
        metadata={
            "name": "PmtFrqcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class LegalPersonIdentification14:
    """
    LegalPersonIdentification1__4 Provides the identification of the
    organisation which is a legal person.

    :ivar id: Identification Unique and unambiguous identification of
        the legal person.
    """

    class Meta:
        name = "LegalPersonIdentification1__4"

    id: OrganisationIdentification15Choice5 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class NotionalAmount51:
    """
    NotionalAmount5__1 Indicates the reference amount from which
    contractual payments are determined and the schedule applicable to the
    payments.

    :ivar amt: Amount Reference amount from which contractual payments
        are determined.&#13; &#13; Usage: In case of partial
        terminations, and amortisations and in case of contracts where
        the notional, due to the characteristics of the contract, varies
        over time, it shall reflect the remaining notional after the
        change took place.
    :ivar schdl_prd: SchedulePeriod Specifies the effective date and end
        date of the schedule for derivative transactions negotiated in
        monetary amounts varying throughout the life of the transaction.
    """

    class Meta:
        name = "NotionalAmount5__1"

    amt: AmountAndDirection1062 = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    schdl_prd: list[Schedule111] = field(
        default_factory=list,
        metadata={
            "name": "SchdlPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "max_occurs": 600,
        },
    )


@dataclass(kw_only=True)
class NotionalAmount61:
    """
    NotionalAmount6__1 Indicates the reference amount from which
    contractual payments are determined and the schedule applicable to the
    payments.

    :ivar amt: Amount Reference amount from which contractual payments
        are determined.&#13; &#13; Usage: In case of partial
        terminations, and amortisations and in case of contracts where
        the notional, due to the characteristics of the contract, varies
        over time, it shall reflect the remaining notional after the
        change took place.
    :ivar schdl_prd: SchedulePeriod Specifies the effective date and end
        date of the schedule for derivative transactions negotiated in
        monetary amounts varying throughout the life of the transaction.
    """

    class Meta:
        name = "NotionalAmount6__1"

    amt: AmountAndDirection1062 = field(
        metadata={
            "name": "Amt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    schdl_prd: list[Schedule111] = field(
        default_factory=list,
        metadata={
            "name": "SchdlPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "max_occurs": 600,
        },
    )


@dataclass(kw_only=True)
class NotionalQuantity91:
    """
    NotionalQuantity9__1 Indicates the reference quantity of the
    transaction and the schedule applicable to the quantity computation.

    :ivar ttl_qty: TotalQuantity Number of units of the financial
        instrument, that is, the nominal value.
    :ivar unit_of_measr: UnitOfMeasure Indicates the unit of measure in
        which the total notional quantity and notional quantity
        schedules are expressed.
    :ivar dtls: Details Indicates the schedule or frequency of the
        derivative transactions.
    """

    class Meta:
        name = "NotionalQuantity9__1"

    ttl_qty: None | Decimal = field(
        default=None,
        metadata={
            "name": "TtlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "total_digits": 25,
            "fraction_digits": 5,
        },
    )
    unit_of_measr: None | UnitOfMeasure8Choice1 = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    dtls: None | QuantityOrTerm1Choice1 = field(
        default=None,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class OptionMultipleBarrierLevels11:
    """
    OptionMultipleBarrierLevels1__1 Specifies the lower and upper barrier
    levels for an option.

    :ivar lwr_lvl: LowerLevel Specifies the lower of the two barrier
        levels as a predetermined price.
    :ivar upper_lvl: UpperLevel Specifies the higher of the two barrier
        levels as a predetermined price.
    """

    class Meta:
        name = "OptionMultipleBarrierLevels1__1"

    lwr_lvl: SecuritiesTransactionPrice23Choice1 = field(
        metadata={
            "name": "LwrLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    upper_lvl: SecuritiesTransactionPrice23Choice1 = field(
        metadata={
            "name": "UpperLvl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class OrganisationIdentification15Choice2:
    """
    OrganisationIdentification15Choice__2 Provides the identification of
    the organisation.

    :ivar lei: LEI Identification is done through the use of legal
        entity identifier code.
    :ivar othr: Other Unique identification of an organisation, using a
        client code or a business identification code.
    :ivar any_bic: AnyBIC Business identifier code used to identify the
        organisation.
    """

    class Meta:
        name = "OrganisationIdentification15Choice__2"

    lei: None | str = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: None | OrganisationIdentification381 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    any_bic: None | str = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass(kw_only=True)
class OrganisationIdentification15Choice3:
    """
    OrganisationIdentification15Choice__3 Provides the identification of
    the organisation.

    :ivar lei: LEI Identification is done through the use of legal
        entity identifier code.
    :ivar othr: Other Unique identification of an organisation, using a
        client code or a business identification code.
    :ivar any_bic: AnyBIC Business identifier code used to identify the
        organisation.
    """

    class Meta:
        name = "OrganisationIdentification15Choice__3"

    lei: None | str = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: None | OrganisationIdentification382 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    any_bic: None | str = field(
        default=None,
        metadata={
            "name": "AnyBIC",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}",
        },
    )


@dataclass(kw_only=True)
class OrganisationIdentification15Choice6:
    """
    OrganisationIdentification15Choice__6 Provides the identification of
    the organisation.

    :ivar lei: LEI Identification is done through the use of legal
        entity identifier code.
    :ivar othr: Other Unique identification of an organisation, using a
        client code or a business identification code.
    """

    class Meta:
        name = "OrganisationIdentification15Choice__6"

    lei: None | str = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: None | OrganisationIdentification382 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class Package41:
    """
    Package4__1 Combination of two or more transactions that are reported
    separately but that are negotiated together as the product of a single
    economic agreement.

    :ivar cmplx_trad_id: ComplexTradeIdentification Specifies the
        identifier determined by the reporting counterparty to connect:
        - two or more transactions that are reported separately but that
        are negotiated together as the product of a single economic
        agreement, - or two or more reports pertaining to the same
        transaction whenever jurisdictional reporting requirement does
        not allow the transaction to be reported with a single report to
        TRs. Usage: Where the package identifier is not known when a new
        transaction is reported, the package identifier is updated as it
        becomes available.&#13; &#13;&#13;
    :ivar fx_swp_lk_id: FXSwapLinkIdentification Identifier which is
        used to link the near leg and far leg of an FX swap per current
        industry practice. This identifier could distingish FX swap from
        other packaged transactions identified by
        ComplexTradeIdentification.
    :ivar pric: Price Indicates the traded price of the entire package
        in which the reported derivative transaction is a component.
    :ivar sprd: Spread Indicates the traded price (expressed as a
        difference between two reference prices) of the entire package
        in which the reported derivative transaction is a component.
    """

    class Meta:
        name = "Package4__1"

    cmplx_trad_id: None | str = field(
        default=None,
        metadata={
            "name": "CmplxTradId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fx_swp_lk_id: None | str = field(
        default=None,
        metadata={
            "name": "FxSwpLkId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 100,
        },
    )
    pric: None | SecuritiesTransactionPrice17Choice1 = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    sprd: None | SecuritiesTransactionPrice20Choice1 = field(
        default=None,
        metadata={
            "name": "Sprd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class Schedule11:
    """
    Schedule1__1 Indicates the unadjusted effective and end date of the
    schedule.

    :ivar uadjstd_fctv_dt: UnadjustedEffectiveDate Indicates the
        unadjusted date at which obligations under the  derivative
        transaction come into effect, as included in the confirmation.
    :ivar uadjstd_end_dt: UnadjustedEndDate Indicates the end date
        agreed in the derivative transaction without adjustment.
    :ivar pric: Price Indicates the price per derivative excluding,
        where applicable: fees, taxes or commissions.
    """

    class Meta:
        name = "Schedule1__1"

    uadjstd_fctv_dt: XmlDate = field(
        metadata={
            "name": "UadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    uadjstd_end_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "UadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    pric: SecuritiesTransactionPrice17Choice1 = field(
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class Schedule41:
    """
    Schedule4__1 Indicates the unadjusted effective and end date of the
    schedule.

    :ivar uadjstd_fctv_dt: UnadjustedEffectiveDate Indicates the
        unadjusted date at which obligations under the  derivative
        transaction come into effect, as included in the confirmation.
    :ivar uadjstd_end_dt: UnadjustedEndDate Indicates the end date
        agreed in the derivative transaction without adjustment.
    :ivar pric: Price Specifies the predetermined price at which the
        owner of the option can buy or sell the underlying
        instrument.&#13; &#13; Usage: For foreign exchange options,
        specifies the exchange rate at which the option can be exercised
        as the rate of exchange from converting the unit currency into
        the quoted currency.&#13; For volatility and variance swaps,
        specify the volatility strike price.
    """

    class Meta:
        name = "Schedule4__1"

    uadjstd_fctv_dt: XmlDate = field(
        metadata={
            "name": "UadjstdFctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    uadjstd_end_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "UadjstdEndDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    pric: SecuritiesTransactionPrice17Choice1 = field(
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class ClearingPartyAndTime221:
    """
    ClearingPartyAndTime22__1 Specifies the central counterparty clearing
    time.

    :ivar ccp: CCP Identifies the central counterparty (CCP) that
        cleared the transaction.
    :ivar clr_dt_tm: ClearingDateTime Time and date when clearing took
        place.
    """

    class Meta:
        name = "ClearingPartyAndTime22__1"

    ccp: OrganisationIdentification15Choice3 = field(
        metadata={
            "name": "CCP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    clr_dt_tm: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "ClrDtTm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class ClearingPartyAndTime231:
    """
    ClearingPartyAndTime23__1 Specifies the central counterparty intended
    clearing time.

    :ivar ccp: CCP Identifies the central counterparty (CCP) that
        cleared the transaction.
    """

    class Meta:
        name = "ClearingPartyAndTime23__1"

    ccp: None | OrganisationIdentification15Choice6 = field(
        default=None,
        metadata={
            "name": "CCP",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class Counterparty451:
    """
    Counterparty45__1 Information related to counterparty identification.

    :ivar id: Identification Unique code identifying the reporting
        counterparty of the contract.
    :ivar ntr: Nature Indicates if the reporting counterparty is a
        central counterparty, a financial, non-financial counterparty or
        other type of counterparty in accordance with regulation.
    :ivar tradg_cpcty: TradingCapacity Identifies the trading capacity
        of the seller.
    :ivar drctn_or_sd: DirectionOrSide Indicates the direction or side
        of the derivative transaction from the perspective of the
        reporting counterparty. &#13; &#13; Usage:&#13; CounterpartySide
        should be used for the instruments such as most forwards and
        forward-like contracts (except for foreign exchange forwards and
        foreign exchange non-deliverable forwards); most options and
        option-like contracts including swaptions, caps and floors;
        credit default swaps; variance, volatility and correlation
        swaps; contracts for difference and spreadbets.
    :ivar tradr_lctn: TraderLocation Location of the trading desk or
        trader responsible for the decision of entering into or
        execution of the transaction.
    :ivar bookg_lctn: BookingLocation Location of the trade party or the
        branch/office of the trade party to which the transaction is
        booked.
    """

    class Meta:
        name = "Counterparty45__1"

    id: PartyIdentification248Choice1 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    ntr: None | CounterpartyTradeNature15Choice1 = field(
        default=None,
        metadata={
            "name": "Ntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    tradg_cpcty: None | TradingCapacity7Code = field(
        default=None,
        metadata={
            "name": "TradgCpcty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    drctn_or_sd: Direction4Choice1 = field(
        metadata={
            "name": "DrctnOrSd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tradr_lctn: None | str = field(
        default=None,
        metadata={
            "name": "TradrLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    bookg_lctn: None | str = field(
        default=None,
        metadata={
            "name": "BookgLctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass(kw_only=True)
class InterestRate33Choice1:
    """
    InterestRate33Choice__1 Specifies the type of a rate, a fixed or a
    floating rate.

    :ivar fxd: Fixed Attributes related specifically to fixed rate of an
        interest rate contract.
    :ivar fltg: Floating Attributes related specifically to floating
        rate of an interest rate contract.
    """

    class Meta:
        name = "InterestRate33Choice__1"

    fxd: None | FixedRate101 = field(
        default=None,
        metadata={
            "name": "Fxd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    fltg: None | FloatingRate131 = field(
        default=None,
        metadata={
            "name": "Fltg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class LegalPersonIdentification12:
    """
    LegalPersonIdentification1__2 Provides the identification of the
    organisation which is a legal person.

    :ivar id: Identification Unique and unambiguous identification of
        the legal person.
    :ivar ctry: Country Code of country where the registered office of
        the organisation is located.
    """

    class Meta:
        name = "LegalPersonIdentification1__2"

    id: OrganisationIdentification15Choice2 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    ctry: None | str = field(
        default=None,
        metadata={
            "name": "Ctry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )


@dataclass(kw_only=True)
class LegalPersonIdentification13:
    """
    LegalPersonIdentification1__3 Provides the identification of the
    organisation which is a legal person.

    :ivar id: Identification Unique and unambiguous identification of
        the legal person.
    """

    class Meta:
        name = "LegalPersonIdentification1__3"

    id: OrganisationIdentification15Choice3 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class LegalPersonIdentification15:
    """
    LegalPersonIdentification1__5 Provides the identification of the
    organisation which is a legal person.

    :ivar id: Identification Unique and unambiguous identification of
        the legal person.
    """

    class Meta:
        name = "LegalPersonIdentification1__5"

    id: OrganisationIdentification15Choice2 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class NotionalAmountLegs51:
    """
    NotionalAmountLegs5__1 Indicates the monetary or converted amount for
    the derivatives transaction.

    :ivar frst_leg: FirstLeg Notional amount of leg 1 which indicates
        monetary or converted amount for the derivatives transaction.
    :ivar scnd_leg: SecondLeg Notional amount of leg 2 which indicates
        monetary or converted amount for the derivatives transaction.
    """

    class Meta:
        name = "NotionalAmountLegs5__1"

    frst_leg: NotionalAmount51 = field(
        metadata={
            "name": "FrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    scnd_leg: None | NotionalAmount61 = field(
        default=None,
        metadata={
            "name": "ScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class NotionalQuantityLegs51:
    """
    NotionalQuantityLegs5__1 Indicates the notional quantity of the
    underlying assets.

    :ivar frst_leg: FirstLeg Aggregate notional quantity of the
        underlying asset of leg 1 for the term of the transaction. Where
        the total notional quantity is not known when a new transaction
        is reported, the total notional quantity is updated as it
        becomes available.
    :ivar scnd_leg: SecondLeg Aggregate notional quantity of the
        underlying asset of leg 2 for the term of the transaction. Where
        the total notional quantity is not known when a new transaction
        is reported, the total notional quantity is updated as it
        becomes available.
    """

    class Meta:
        name = "NotionalQuantityLegs5__1"

    frst_leg: None | NotionalQuantity91 = field(
        default=None,
        metadata={
            "name": "FrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    scnd_leg: None | NotionalQuantity91 = field(
        default=None,
        metadata={
            "name": "ScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class OptionBarrierLevel1Choice1:
    """
    OptionBarrierLevel1Choice__1 Choice of barrier levels for an option.

    :ivar sngl: Single For a barrier option involving only one barrier
        level, specifies the predetermined price of an underlier at
        which the occurrence of a barrier event (e.g. knock-out) is
        determined.
    :ivar mltpl: Multiple For a barrier option involving two barrier
        levels, specifies the lower and upper levels as a predetermined
        price of an underlier at which the occurrence of a barrier event
        (such as a knock-out) is determined.
    """

    class Meta:
        name = "OptionBarrierLevel1Choice__1"

    sngl: None | SecuritiesTransactionPrice23Choice1 = field(
        default=None,
        metadata={
            "name": "Sngl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    mltpl: None | OptionMultipleBarrierLevels11 = field(
        default=None,
        metadata={
            "name": "Mltpl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PartyIdentification236Choice1:
    """
    PartyIdentification236Choice__1 Provides the identification of the
    organisation.

    :ivar lgl: Legal Party is a legal person.
    :ivar ntrl: Natural Party is a natural person.
    """

    class Meta:
        name = "PartyIdentification236Choice__1"

    lgl: None | OrganisationIdentification15Choice3 = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ntrl: None | NaturalPersonIdentification21 = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PartyIdentification248Choice4:
    """
    PartyIdentification248Choice__4 Provides the identification of the
    organisation.

    :ivar lgl: Legal Party is a legal person.
    """

    class Meta:
        name = "PartyIdentification248Choice__4"

    lgl: None | LegalPersonIdentification14 = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PriceData21:
    """
    PriceData2__1 Indicates the details of the price applicable to the
    derivative transaction.

    :ivar pric: Price Indicates the price per derivative excluding,
        where applicable: fees, taxes or commissions.
    :ivar schdl_prd: SchedulePeriod Specifies the effective date and end
        date of the schedule for derivative transactions with prices
        varying throughout the life of the transaction.
    :ivar unit_of_measr: UnitOfMeasure Specifies the unit of measure in
        which the price is expressed.
    """

    class Meta:
        name = "PriceData2__1"

    pric: None | SecuritiesTransactionPrice17Choice1 = field(
        default=None,
        metadata={
            "name": "Pric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    schdl_prd: list[Schedule11] = field(
        default_factory=list,
        metadata={
            "name": "SchdlPrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "max_occurs": 600,
        },
    )
    unit_of_measr: None | UnitOfMeasure8Choice1 = field(
        default=None,
        metadata={
            "name": "UnitOfMeasr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class SecurityIdentification41Choice1:
    """
    SecurityIdentification41Choice__1 Choice between ISIN and an
    alternative format for the identification of a financial instrument.

    ISIN is the preferred format.

    :ivar isin: ISIN International Securities Identification Number
        (ISIN). A numbering system designed by the United Nation's
        International Organisation for Standardisation (ISO). The ISIN
        is composed of a 2-character prefix representing the country of
        issue, followed by the national security number (if one exists),
        and a check digit. Each country has a national numbering agency
        that assigns ISIN numbers for securities in that country.
    :ivar bskt: Basket Identification of constituents for a basket of
        indexes.
    :ivar indx: Index Indicates the index upon which the financial
        instrument is based.
    :ivar othr: Other Other identification of an underlier.
    """

    class Meta:
        name = "SecurityIdentification41Choice__1"

    isin: None | str = field(
        default=None,
        metadata={
            "name": "ISIN",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}",
        },
    )
    bskt: None | CustomBasket41 = field(
        default=None,
        metadata={
            "name": "Bskt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    indx: None | IndexIdentification11 = field(
        default=None,
        metadata={
            "name": "Indx",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr: None | GenericIdentification184 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class ClearingPartyAndTime21Choice1:
    """
    ClearingPartyAndTime21Choice__1 Specifies the central counterparty
    clearing time.

    :ivar dtls: Details Indicates that the contract is cleared and
        provides detailes of such clearing.
    """

    class Meta:
        name = "ClearingPartyAndTime21Choice__1"

    dtls: None | ClearingPartyAndTime221 = field(
        default=None,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class ClearingPartyAndTime22Choice1:
    """
    ClearingPartyAndTime22Choice__1 Specifies the central counterparty
    intended clearing time.

    :ivar dtls: Details Indicates that the contract is intended to be
        cleared and provides detailes of such clearing.
    """

    class Meta:
        name = "ClearingPartyAndTime22Choice__1"

    dtls: None | ClearingPartyAndTime231 = field(
        default=None,
        metadata={
            "name": "Dtls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class ContractType151:
    """
    ContractType15__1 Information related to contract attributes.

    :ivar ctrct_tp: ContractType Classification of information according
        to contract type.
    :ivar asst_clss: AssetClass Specifies the classification according
        to the asset class of the contract.
    :ivar pdct_id: ProductIdentification Specifies the identification of
        the derivative product.
    :ivar undrlyg_instrm: UnderlyingInstrument Unique identification to
        identify the direct underlying instrument based on its type.
    :ivar undrlyg_asst_tradg_pltfm_idr:
        UnderlyingAssetTradingPlatformIdentifier For a platform (e.g.
        exchange) traded underlying asset, the platform on which the
        asset is traded. This data element is not applicable to OTC
        derivative transactions with custom basket constituents.
    :ivar undrlyg_asst_pric_src: UnderlyingAssetPriceSource For an
        underlying asset or benchmark not traded on a platform, the
        source of the price used to determine the value or level of the
        asset or benchmark. This data element is not applicable to OTC
        derivative transactions with custom basket constituents.
    :ivar sttlm_ccy: SettlementCurrency Specifies the currency to be
        used for cash settlement of the transaction. &#13; &#13; Usage:
        For multicurrency transactions that do not net,
        SettlementCurrency is to be considered as the first leg.
    :ivar sttlm_ccy_scnd_leg: SettlementCurrencySecondLeg Specifies the
        currency second leg to be used for cash settlement of the
        transaction.
    :ivar plc_of_sttlm: PlaceOfSettlement Specifies the place where
        settlement of the transaction occurs as stipulated in the
        contract.
    :ivar deriv_based_on_crpt_asst: DerivativeBasedOnCryptoAsset
        Indicator whether the derivative is based on crypto-asset.&#13;
        &#13; Usage: If the element is not present, the
        DerivativeBasedOnCryptoAsset is False.
    """

    class Meta:
        name = "ContractType15__1"

    ctrct_tp: FinancialInstrumentContractType2Code = field(
        metadata={
            "name": "CtrctTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    asst_clss: ProductType4Code1 = field(
        metadata={
            "name": "AsstClss",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    pdct_id: None | SecurityIdentification461 = field(
        default=None,
        metadata={
            "name": "PdctId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    undrlyg_instrm: None | SecurityIdentification41Choice1 = field(
        default=None,
        metadata={
            "name": "UndrlygInstrm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    undrlyg_asst_tradg_pltfm_idr: None | str = field(
        default=None,
        metadata={
            "name": "UndrlygAsstTradgPltfmIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    undrlyg_asst_pric_src: None | str = field(
        default=None,
        metadata={
            "name": "UndrlygAsstPricSrc",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 50,
        },
    )
    sttlm_ccy: None | CurrencyExchange231 = field(
        default=None,
        metadata={
            "name": "SttlmCcy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    sttlm_ccy_scnd_leg: None | CurrencyExchange231 = field(
        default=None,
        metadata={
            "name": "SttlmCcyScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    plc_of_sttlm: None | str = field(
        default=None,
        metadata={
            "name": "PlcOfSttlm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z]{2,2}",
        },
    )
    deriv_based_on_crpt_asst: None | bool = field(
        default=None,
        metadata={
            "name": "DerivBasedOnCrptAsst",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class InterestRateLegs141:
    """
    InterestRateLegs14__1 Details related to interest rate attributes.

    :ivar frst_leg: FirstLeg Details concerning the rate in the first
        leg of an interest rate contract.
    :ivar scnd_leg: SecondLeg Details concerning the rate in the second
        leg of an interest rate contract.
    """

    class Meta:
        name = "InterestRateLegs14__1"

    frst_leg: None | InterestRate33Choice1 = field(
        default=None,
        metadata={
            "name": "FrstLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    scnd_leg: None | InterestRate33Choice1 = field(
        default=None,
        metadata={
            "name": "ScndLeg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class OptionOrSwaption111:
    """
    OptionOrSwaption11__1 Option or swaption related attributes.

    :ivar tp: Type Specifies the type of the Option whether it is a call
        option (right to purchase a specific underlying asset) or a put
        option (right to sell a specific underlying asset).&#13;
    :ivar mbdd_tp: EmbeddedType Specifies the type of the Option when an
        optional provision is embedded in the contract.
    :ivar exrc_style: ExerciseStyle Indication as to whether the option
        may be exercised only at a fixed date (European, and Asian
        style), a series of pre-specified dates (Bermudan) or at any
        time during the life of the contract (American style). This
        field does not have to be populated for ISIN instruments.
    :ivar exrc_dt: ExerciseDate Specifies the earliest unadjusted date
        during the exercise period on which an option can be exercised.
    :ivar strk_pric: StrikePrice Specifies the predetermined price at
        which the owner of the option can buy or sell the underlying
        instrument.&#13; &#13; Usage: For foreign exchange options,
        specifies the exchange rate at which the option can be exercised
        as the rate of exchange from converting the unit currency into
        the quoted currency.&#13; For volatility and variance swaps,
        specify the volatility strike price.
    :ivar strk_pric_schdl: StrikePriceSchedule Specifies the effective
        date and end date of the schedule for derivative transactions
        with strike prices varying throughout the life of the
        transaction.
    :ivar call_amt: CallAmount Indicates the amount and currency of a
        foreign exchange option that the option holder has the right to
        buy.
    :ivar put_amt: PutAmount Indicates the amount and currency of a
        foreign exchange option that the option holder has the right to
        sell.
    :ivar prm_amt: PremiumAmount Specifies the monetary amount of the
        premium paid by the buyer of the option.
    :ivar prm_pmt_dt: PremiumPaymentDate Specifies the date on which the
        option premium is paid.
    :ivar mtrty_dt_of_undrlyg: MaturityDateOfUnderlying In case of
        swaptions, maturity date of the underlying swap.
    :ivar brrr_lvls: BarrierLevels For a barrier option, specifies one
        or more barrier levels.
    """

    class Meta:
        name = "OptionOrSwaption11__1"

    tp: None | OptionType2Code = field(
        default=None,
        metadata={
            "name": "Tp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    mbdd_tp: None | EmbeddedType1Code = field(
        default=None,
        metadata={
            "name": "MbddTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    exrc_style: None | OptionStyle6Code = field(
        default=None,
        metadata={
            "name": "ExrcStyle",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    exrc_dt: None | ExerciseDate1Choice1 = field(
        default=None,
        metadata={
            "name": "ExrcDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    strk_pric: None | SecuritiesTransactionPrice17Choice1 = field(
        default=None,
        metadata={
            "name": "StrkPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    strk_pric_schdl: list[Schedule41] = field(
        default_factory=list,
        metadata={
            "name": "StrkPricSchdl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "max_occurs": 600,
        },
    )
    call_amt: None | ActiveOrHistoricCurrencyAnd5DecimalAmount = field(
        default=None,
        metadata={
            "name": "CallAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    put_amt: None | ActiveOrHistoricCurrencyAnd5DecimalAmount = field(
        default=None,
        metadata={
            "name": "PutAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    prm_amt: None | ActiveOrHistoricCurrencyAnd5DecimalAmount = field(
        default=None,
        metadata={
            "name": "PrmAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    prm_pmt_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "PrmPmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    mtrty_dt_of_undrlyg: None | XmlDate = field(
        default=None,
        metadata={
            "name": "MtrtyDtOfUndrlyg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    brrr_lvls: None | OptionBarrierLevel1Choice1 = field(
        default=None,
        metadata={
            "name": "BrrrLvls",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class OtherPayment51:
    """
    OtherPayment5__1 Payment related to elements not reported in dedicated
    fields.

    :ivar pmt_amt: PaymentAmount Amount of money of any payment the
        reporting counterparty made or received.&#13; &#13; Usage: The
        negative symbol to be used to indicate that the payment was
        made, not received.&#13; &#13;
    :ivar pmt_tp: PaymentType Indicates the type of other payment.
    :ivar pmt_dt: PaymentDate Indicates the unadjusted date on which the
        other payment is paid.
    :ivar pmt_pyer: PaymentPayer Identifies the payer of the other
        payment amount.
    :ivar pmt_rcvr: PaymentReceiver Identifies the receiver of the other
        payment amount.
    """

    class Meta:
        name = "OtherPayment5__1"

    pmt_amt: None | AmountAndDirection1063 = field(
        default=None,
        metadata={
            "name": "PmtAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    pmt_tp: PaymentType5Choice1 = field(
        metadata={
            "name": "PmtTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    pmt_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "PmtDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    pmt_pyer: None | PartyIdentification236Choice1 = field(
        default=None,
        metadata={
            "name": "PmtPyer",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    pmt_rcvr: None | PartyIdentification236Choice1 = field(
        default=None,
        metadata={
            "name": "PmtRcvr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PartyIdentification248Choice2:
    """
    PartyIdentification248Choice__2 Provides the identification of the
    organisation.

    :ivar lgl: Legal Party is a legal person.
    :ivar ntrl: Natural Party is a natural person.
    """

    class Meta:
        name = "PartyIdentification248Choice__2"

    lgl: None | LegalPersonIdentification12 = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ntrl: None | NaturalPersonIdentification31 = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PartyIdentification248Choice3:
    """
    PartyIdentification248Choice__3 Provides the identification of the
    organisation.

    :ivar lgl: Legal Party is a legal person.
    """

    class Meta:
        name = "PartyIdentification248Choice__3"

    lgl: None | LegalPersonIdentification13 = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class PartyIdentification248Choice5:
    """
    PartyIdentification248Choice__5 Provides the identification of the
    organisation.

    :ivar lgl: Legal Party is a legal person.
    :ivar ntrl: Natural Party is a natural person.
    """

    class Meta:
        name = "PartyIdentification248Choice__5"

    lgl: None | LegalPersonIdentification15 = field(
        default=None,
        metadata={
            "name": "Lgl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ntrl: None | NaturalPersonIdentification32 = field(
        default=None,
        metadata={
            "name": "Ntrl",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class Cleared23Choice1:
    """
    Cleared23Choice__1 Indicates whether the contract was cleared, not
    cleared or if the contract is intended to be cleared.

    :ivar clrd: Cleared Indicates that the contract has been cleared.
    :ivar intnd_to_clear: IntendToClear Indicates that the contract is
        intended to be cleared.
    :ivar non_clrd: NonCleared Indicates that the contract has not been
        cleared.
    """

    class Meta:
        name = "Cleared23Choice__1"

    clrd: None | ClearingPartyAndTime21Choice1 = field(
        default=None,
        metadata={
            "name": "Clrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    intnd_to_clear: None | ClearingPartyAndTime22Choice1 = field(
        default=None,
        metadata={
            "name": "IntndToClear",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    non_clrd: None | ClearingExceptionOrExemption3Choice1 = field(
        default=None,
        metadata={
            "name": "NonClrd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class Counterparty461:
    """
    Counterparty46__1 Information related to counterparty identification.

    :ivar id_tp: IdentificationType Indicates if the counterparty is a
        legal entity or a natural person.
    :ivar ntr: Nature Indicates if the counterparty is a central
        counterparty, a financial, non-financial counterparty or other
        type of counterparty in accordance with regulation.
    """

    class Meta:
        name = "Counterparty46__1"

    id_tp: PartyIdentification248Choice2 = field(
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    ntr: None | CounterpartyTradeNature15Choice1 = field(
        default=None,
        metadata={
            "name": "Ntr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class Counterparty462:
    """
    Counterparty46__2 Information related to counterparty identification.

    :ivar id_tp: IdentificationType Indicates if the counterparty is a
        legal entity or a natural person.
    """

    class Meta:
        name = "Counterparty46__2"

    id_tp: PartyIdentification248Choice5 = field(
        metadata={
            "name": "IdTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class TradeTransaction504:
    """
    TradeTransaction50__4 Provides details of the trade transaction.

    :ivar tx_id: TransactionIdentification Choice between a Unique
        Transaction Identifier (UTI) or a proprietary identifier as
        agreed with the counterparty.
    :ivar early_termntn_dt: EarlyTerminationDate Indicates the effective
        date of the early termination of the reported derivative
        transaction.
    :ivar deriv_evt: DerivativeEvent Indication of the derivative event
        of the transaction.
    :ivar othr_pmt: OtherPayment Payment related to elements not
        reported in dedicated fields.
    """

    class Meta:
        name = "TradeTransaction50__4"

    tx_id: UniqueTransactionIdentifier2Choice1 = field(
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    early_termntn_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EarlyTermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    deriv_evt: DerivativeEvent64 = field(
        metadata={
            "name": "DerivEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    othr_pmt: list[OtherPayment51] = field(
        default_factory=list,
        metadata={
            "name": "OthrPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "max_occurs": 600,
        },
    )


@dataclass(kw_only=True)
class CommonTradeDataReport714:
    """
    CommonTradeDataReport71__4 Information related to contract and
    transaction details.

    :ivar ctrct_data: ContractData Data related to a trade contract.
    :ivar tx_data: TransactionData Data related to a trade transaction.
    """

    class Meta:
        name = "CommonTradeDataReport71__4"

    ctrct_data: ContractType152 = field(
        metadata={
            "name": "CtrctData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tx_data: TradeTransaction504 = field(
        metadata={
            "name": "TxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class TradeClearing111:
    """
    TradeClearing11__1 Information related to the clearing of the contract.

    :ivar clr_sts: ClearingStatus Indicator of whether the transaction
        has been cleared, or is intended to be cleared, by a central
        counterparty.
    :ivar intra_grp: IntraGroup Indicates whether the contract was
        entered into as an intragroup transaction.&#13; &#13; Usage:
        When absent, default value is false.
    """

    class Meta:
        name = "TradeClearing11__1"

    clr_sts: Cleared23Choice1 = field(
        metadata={
            "name": "ClrSts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    intra_grp: None | bool = field(
        default=None,
        metadata={
            "name": "IntraGrp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeCounterpartyReport201:
    """
    TradeCounterpartyReport20__1 Information related to parties in the
    contract.

    :ivar rptg_ctr_pty: ReportingCounterparty Identification of the
        counterparty to a derivative transaction who is fulfilling its
        reporting obligation in the present report.
    :ivar othr_ctr_pty: OtherCounterparty Identification of the other
        counterparty to a derivative transaction.
    :ivar brkr: Broker Identification of the entity [party] acting as an
        intermediary which [who] arranges the transaction for the
        reporting counterparty (“arranging broker”).
    :ivar submitg_agt: SubmittingAgent Identification of the party that
        ultimately submits the report to the trade repository.
    :ivar clr_mmb: ClearingMember Identifies the clearing member through
        which a derivative transaction is cleared at a central
        counterparty (CCP).  The element applies to transactions under
        the agency clearing model and the principal clearing model.
    :ivar bnfcry: Beneficiary Identification of the beneficiary of a
        derivative transaction, that is a party that is subject to the
        rights and obligations arising from the contract.&#13; &#13;
        Usage: In case of two occurances of beneficiary, the first
        iteration should always be the beneficiary 1 of the counterparty
        1 and the second iteration is the beneficiary 2 of the
        counterparty 2. In case of single occurance of Beneficiary,
        RelationshipRecord should be provided.
    :ivar ntty_rspnsbl_for_rpt: EntityResponsibleForReport According to
        jurisdictional requirements, identification of the entity with
        the legal obligation or responsibility to report.
    """

    class Meta:
        name = "TradeCounterpartyReport20__1"

    rptg_ctr_pty: Counterparty451 = field(
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    othr_ctr_pty: Counterparty461 = field(
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    brkr: None | OrganisationIdentification15Choice3 = field(
        default=None,
        metadata={
            "name": "Brkr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    submitg_agt: OrganisationIdentification15Choice4 = field(
        metadata={
            "name": "SubmitgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    clr_mmb: None | PartyIdentification248Choice3 = field(
        default=None,
        metadata={
            "name": "ClrMmb",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    bnfcry: None | PartyIdentification248Choice4 = field(
        default=None,
        metadata={
            "name": "Bnfcry",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ntty_rspnsbl_for_rpt: OrganisationIdentification15Choice1 = field(
        metadata={
            "name": "NttyRspnsblForRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class TradeCounterpartyReport202:
    """
    TradeCounterpartyReport20__2 Information related to parties in the
    contract.

    :ivar rptg_ctr_pty: ReportingCounterparty Identification of the
        counterparty to a derivative transaction who is fulfilling its
        reporting obligation in the present report.
    :ivar othr_ctr_pty: OtherCounterparty Identification of the other
        counterparty to a derivative transaction.
    :ivar submitg_agt: SubmittingAgent Identification of the party that
        ultimately submits the report to the trade repository.
    :ivar ntty_rspnsbl_for_rpt: EntityResponsibleForReport According to
        jurisdictional requirements, identification of the entity with
        the legal obligation or responsibility to report.
    """

    class Meta:
        name = "TradeCounterpartyReport20__2"

    rptg_ctr_pty: Counterparty452 = field(
        metadata={
            "name": "RptgCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    othr_ctr_pty: Counterparty462 = field(
        metadata={
            "name": "OthrCtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    submitg_agt: OrganisationIdentification15Choice4 = field(
        metadata={
            "name": "SubmitgAgt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    ntty_rspnsbl_for_rpt: OrganisationIdentification15Choice1 = field(
        metadata={
            "name": "NttyRspnsblForRpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class CounterpartySpecificData361:
    """
    CounterpartySpecificData36__1 Data related specifically to
    counterparties.

    :ivar ctr_pty: Counterparty Data specific to counterparties of the
        reported transaction/position.
    :ivar rptg_tm_stmp: ReportingTimeStamp Indicates the date and time
        of the submission of the report to the trade repository.
    """

    class Meta:
        name = "CounterpartySpecificData36__1"

    ctr_pty: TradeCounterpartyReport201 = field(
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    rptg_tm_stmp: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "RptgTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class CounterpartySpecificData362:
    """
    CounterpartySpecificData36__2 Data related specifically to
    counterparties.

    :ivar ctr_pty: Counterparty Data specific to counterparties of the
        reported transaction/position.
    :ivar rptg_tm_stmp: ReportingTimeStamp Indicates the date and time
        of the submission of the report to the trade repository.
    """

    class Meta:
        name = "CounterpartySpecificData36__2"

    ctr_pty: TradeCounterpartyReport202 = field(
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    rptg_tm_stmp: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "RptgTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class CounterpartySpecificData363:
    """
    CounterpartySpecificData36__3 Data related specifically to
    counterparties.

    :ivar ctr_pty: Counterparty Data specific to counterparties of the
        reported transaction/position.
    :ivar valtn: Valuation Data specific to the valuation of the
        transaction.
    :ivar rptg_tm_stmp: ReportingTimeStamp Indicates the date and time
        of the submission of the report to the trade repository.
    """

    class Meta:
        name = "CounterpartySpecificData36__3"

    ctr_pty: TradeCounterpartyReport202 = field(
        metadata={
            "name": "CtrPty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    valtn: ContractValuationData81 = field(
        metadata={
            "name": "Valtn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    rptg_tm_stmp: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "RptgTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeTransaction501:
    """
    TradeTransaction50__1 Provides details of the trade transaction.

    :ivar tx_id: TransactionIdentification Choice between a Unique
        Transaction Identifier (UTI) or a proprietary identifier as
        agreed with the counterparty.
    :ivar scndry_tx_id: SecondaryTransactionIdentification A proprietary
        internal trade identifier, as determined by the Reporting
        Counterparty. It enables internal tracing of Trade Repository
        records with the Reporting Counterparty records.&#13; &#13;
        Usage: SecondaryTransactionIdentification element is optional
        and is not intended to be used in any data handling to link a
        report to any previous report. For data handling,
        TransactionIdentification element shall be primarily used in
        case of linking reports, while the TechnicalRecordId element may
        also be used for technical tracing of records in each report,
        provided that this element is allowed for usage in a specific
        implementation of this message definition.
    :ivar prr_tx_id: PriorTransactionIdentification Choice between a
        Unique Transaction Identifier (UTI) or a proprietary identifier
        assigned to the predecessor transaction that has given rise to
        the reported transaction due to a lifecycle event.&#13;
        &#13;&#13; Usage: This data element is not applicable when
        reporting many-to-one and many-to-many relations between
        transactions (for example, in the case of a compression).&#13;
        &#13; This data element may be applicable when reporting one-to-
        one and one-to-many relations between transactions (for example,
        in the case of a clearing).&#13;&#13;
    :ivar coll_prtfl_cd: CollateralPortfolioCode Specifies the unique
        code assigned by the reporting counterparty to the portfolio if
        the collateral is posted on a portfolio basis.
    :ivar pltfm_idr: PlatformIdentifier Identifies the trading platform
        on which the derivative transaction was executed (for example,
        exchange, multilateral trading facility, swap execution
        facility). &#13; &#13; Usage: For transactions where no trading
        facility was involved, specific predefined codes have to be
        used.
    :ivar tx_pric: TransactionPrice Indicates the price per derivative
        excluding, where applicable, commission and accrued interest.
    :ivar ntnl_amt: NotionalAmount Indicates monetary or converted
        amount for the derivatives transaction.&#13; &#13; Usage: In
        case of partial terminations, and amortisations and in case of
        contracts where the notional, due to the characteristics of the
        contract, varies over time, it shall reflect the remaining
        notional after the change took place.&#13;
    :ivar ntnl_qty: NotionalQuantity Indicates for each leg of the
        transaction the total notional quantity of the underlying asset
        for the term of the transaction.
    :ivar dlvry_tp: DeliveryType Indicates whether the financial
        instrument is settled physically or in cash or decided at
        expiration time by counterparty.
    :ivar exctn_tm_stmp: ExecutionTimeStamp Indicates the date and time
        of the execution of the derivative transaction.
    :ivar fctv_dt: EffectiveDate Indicates the date when obligations
        under the contract come into effect.
    :ivar xprtn_dt: ExpirationDate Indicates the unadjusted date at
        which obligations under the derivative transaction stop being
        effective, as included in the confirmation.&#13; &#13;&#13; For
        European style options, date on which the holder can exercise
        the right or let it lapse.&#13;&#13; For American style options,
        the holder can exercise the right up to the expiry date.&#13;
        &#13;&#13; Usage: &#13; An early termination shall not be
        reported in this field.
    :ivar sttlm_dt: SettlementDate Indicates the unadjusted date, as per
        the contract, by which all transfer of cash or assets should
        take place and the counterparties should no longer have any
        outstanding obligations to each other. &#13; For products that
        may not have a final contractual settlement date (eg American
        options), this data element reflects the date by which the
        transfer of cash or asset would take place if termination were
        to occur on the expiration date.
    :ivar deriv_evt: DerivativeEvent Indication of the derivative event
        of the transaction.
    :ivar trad_conf: TradeConfirmation Specifies whether the contract
        was electronically confirmed, non-electronically confirmed or
        remains unconfirmed.
    :ivar non_stdsd_term: NonStandardisedTerm Indicates whether the
        derivative transaction has one or more additional terms or
        provisions that materially affect the price of the
        transaction.&#13; &#13; Usage: If the element is not present,
        the NonStandardisedTerm is False.
    :ivar trad_clr: TradeClearing Information related to clearing of the
        reported contract.
    :ivar intrst_rate: InterestRate Information related to interest rate
        asset class type.
    :ivar ccy: Currency Information related to currency asset class
        type.
    :ivar cmmdty: Commodity Information related to commodity asset class
        type.
    :ivar optn: Option Information related to credit derivative asset
        class type.
    :ivar cdt: Credit Information related to credit derivative asset
        class type.
    :ivar othr_pmt: OtherPayment Payment related to elements not
        reported in dedicated fields.
    :ivar packg: Package A combination of two or more transactions that
        are reported separately but that are negotiated together as the
        product of a single economic agreement.
    """

    class Meta:
        name = "TradeTransaction50__1"

    tx_id: UniqueTransactionIdentifier2Choice1 = field(
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    scndry_tx_id: None | str = field(
        default=None,
        metadata={
            "name": "ScndryTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 72,
        },
    )
    prr_tx_id: None | UniqueTransactionIdentifier3Choice1 = field(
        default=None,
        metadata={
            "name": "PrrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    coll_prtfl_cd: CollateralPortfolioCode6Choice1 = field(
        metadata={
            "name": "CollPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    pltfm_idr: None | str = field(
        default=None,
        metadata={
            "name": "PltfmIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    tx_pric: None | PriceData21 = field(
        default=None,
        metadata={
            "name": "TxPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ntnl_amt: NotionalAmountLegs51 = field(
        metadata={
            "name": "NtnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    ntnl_qty: None | NotionalQuantityLegs51 = field(
        default=None,
        metadata={
            "name": "NtnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    dlvry_tp: None | PhysicalTransferType4Code = field(
        default=None,
        metadata={
            "name": "DlvryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    exctn_tm_stmp: XmlDateTime = field(
        metadata={
            "name": "ExctnTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    fctv_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    xprtn_dt: XmlDate = field(
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sttlm_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    deriv_evt: DerivativeEvent61 = field(
        metadata={
            "name": "DerivEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    trad_conf: None | TradeConfirmation4Choice1 = field(
        default=None,
        metadata={
            "name": "TradConf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    non_stdsd_term: None | bool = field(
        default=None,
        metadata={
            "name": "NonStdsdTerm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    trad_clr: TradeClearing111 = field(
        metadata={
            "name": "TradClr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    intrst_rate: None | InterestRateLegs141 = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ccy: None | CurrencyExchange221 = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    cmmdty: None | AssetClassCommodity7Choice = field(
        default=None,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    optn: None | OptionOrSwaption111 = field(
        default=None,
        metadata={
            "name": "Optn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    cdt: None | CreditDerivative41 = field(
        default=None,
        metadata={
            "name": "Cdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr_pmt: list[OtherPayment51] = field(
        default_factory=list,
        metadata={
            "name": "OthrPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "max_occurs": 600,
        },
    )
    packg: None | Package41 = field(
        default=None,
        metadata={
            "name": "Packg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeTransaction502:
    """
    TradeTransaction50__2 Provides details of the trade transaction.

    :ivar tx_id: TransactionIdentification Choice between a Unique
        Transaction Identifier (UTI) or a proprietary identifier as
        agreed with the counterparty.
    :ivar scndry_tx_id: SecondaryTransactionIdentification A proprietary
        internal trade identifier, as determined by the Reporting
        Counterparty. It enables internal tracing of Trade Repository
        records with the Reporting Counterparty records.&#13; &#13;
        Usage: SecondaryTransactionIdentification element is optional
        and is not intended to be used in any data handling to link a
        report to any previous report. For data handling,
        TransactionIdentification element shall be primarily used in
        case of linking reports, while the TechnicalRecordId element may
        also be used for technical tracing of records in each report,
        provided that this element is allowed for usage in a specific
        implementation of this message definition.
    :ivar prr_tx_id: PriorTransactionIdentification Choice between a
        Unique Transaction Identifier (UTI) or a proprietary identifier
        assigned to the predecessor transaction that has given rise to
        the reported transaction due to a lifecycle event.&#13;
        &#13;&#13; Usage: This data element is not applicable when
        reporting many-to-one and many-to-many relations between
        transactions (for example, in the case of a compression).&#13;
        &#13; This data element may be applicable when reporting one-to-
        one and one-to-many relations between transactions (for example,
        in the case of a clearing).&#13;&#13;
    :ivar coll_prtfl_cd: CollateralPortfolioCode Specifies the unique
        code assigned by the reporting counterparty to the portfolio if
        the collateral is posted on a portfolio basis.
    :ivar pltfm_idr: PlatformIdentifier Identifies the trading platform
        on which the derivative transaction was executed (for example,
        exchange, multilateral trading facility, swap execution
        facility). &#13; &#13; Usage: For transactions where no trading
        facility was involved, specific predefined codes have to be
        used.
    :ivar tx_pric: TransactionPrice Indicates the price per derivative
        excluding, where applicable, commission and accrued interest.
    :ivar ntnl_amt: NotionalAmount Indicates monetary or converted
        amount for the derivatives transaction.&#13; &#13; Usage: In
        case of partial terminations, and amortisations and in case of
        contracts where the notional, due to the characteristics of the
        contract, varies over time, it shall reflect the remaining
        notional after the change took place.&#13;
    :ivar ntnl_qty: NotionalQuantity Indicates for each leg of the
        transaction the total notional quantity of the underlying asset
        for the term of the transaction.
    :ivar dlvry_tp: DeliveryType Indicates whether the financial
        instrument is settled physically or in cash or decided at
        expiration time by counterparty.
    :ivar exctn_tm_stmp: ExecutionTimeStamp Indicates the date and time
        of the execution of the derivative transaction.
    :ivar fctv_dt: EffectiveDate Indicates the date when obligations
        under the contract come into effect.
    :ivar xprtn_dt: ExpirationDate Indicates the unadjusted date at
        which obligations under the derivative transaction stop being
        effective, as included in the confirmation.&#13; &#13;&#13; For
        European style options, date on which the holder can exercise
        the right or let it lapse.&#13;&#13; For American style options,
        the holder can exercise the right up to the expiry date.&#13;
        &#13;&#13; Usage: &#13; An early termination shall not be
        reported in this field.
    :ivar sttlm_dt: SettlementDate Indicates the unadjusted date, as per
        the contract, by which all transfer of cash or assets should
        take place and the counterparties should no longer have any
        outstanding obligations to each other. &#13; For products that
        may not have a final contractual settlement date (eg American
        options), this data element reflects the date by which the
        transfer of cash or asset would take place if termination were
        to occur on the expiration date.
    :ivar deriv_evt: DerivativeEvent Indication of the derivative event
        of the transaction.
    :ivar trad_conf: TradeConfirmation Specifies whether the contract
        was electronically confirmed, non-electronically confirmed or
        remains unconfirmed.
    :ivar non_stdsd_term: NonStandardisedTerm Indicates whether the
        derivative transaction has one or more additional terms or
        provisions that materially affect the price of the
        transaction.&#13; &#13; Usage: If the element is not present,
        the NonStandardisedTerm is False.
    :ivar trad_clr: TradeClearing Information related to clearing of the
        reported contract.
    :ivar intrst_rate: InterestRate Information related to interest rate
        asset class type.
    :ivar ccy: Currency Information related to currency asset class
        type.
    :ivar cmmdty: Commodity Information related to commodity asset class
        type.
    :ivar optn: Option Information related to credit derivative asset
        class type.
    :ivar cdt: Credit Information related to credit derivative asset
        class type.
    :ivar othr_pmt: OtherPayment Payment related to elements not
        reported in dedicated fields.
    :ivar packg: Package A combination of two or more transactions that
        are reported separately but that are negotiated together as the
        product of a single economic agreement.
    """

    class Meta:
        name = "TradeTransaction50__2"

    tx_id: UniqueTransactionIdentifier2Choice1 = field(
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    scndry_tx_id: None | str = field(
        default=None,
        metadata={
            "name": "ScndryTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 72,
        },
    )
    prr_tx_id: None | UniqueTransactionIdentifier3Choice1 = field(
        default=None,
        metadata={
            "name": "PrrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    coll_prtfl_cd: CollateralPortfolioCode6Choice1 = field(
        metadata={
            "name": "CollPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    pltfm_idr: None | str = field(
        default=None,
        metadata={
            "name": "PltfmIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    tx_pric: None | PriceData21 = field(
        default=None,
        metadata={
            "name": "TxPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ntnl_amt: NotionalAmountLegs51 = field(
        metadata={
            "name": "NtnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    ntnl_qty: None | NotionalQuantityLegs51 = field(
        default=None,
        metadata={
            "name": "NtnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    dlvry_tp: None | PhysicalTransferType4Code = field(
        default=None,
        metadata={
            "name": "DlvryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    exctn_tm_stmp: XmlDateTime = field(
        metadata={
            "name": "ExctnTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    fctv_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    xprtn_dt: XmlDate = field(
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    sttlm_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    deriv_evt: DerivativeEvent62 = field(
        metadata={
            "name": "DerivEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    trad_conf: None | TradeConfirmation4Choice1 = field(
        default=None,
        metadata={
            "name": "TradConf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    non_stdsd_term: None | bool = field(
        default=None,
        metadata={
            "name": "NonStdsdTerm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    trad_clr: TradeClearing111 = field(
        metadata={
            "name": "TradClr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    intrst_rate: None | InterestRateLegs141 = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ccy: None | CurrencyExchange221 = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    cmmdty: None | AssetClassCommodity7Choice = field(
        default=None,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    optn: None | OptionOrSwaption111 = field(
        default=None,
        metadata={
            "name": "Optn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    cdt: None | CreditDerivative41 = field(
        default=None,
        metadata={
            "name": "Cdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr_pmt: list[OtherPayment51] = field(
        default_factory=list,
        metadata={
            "name": "OthrPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "max_occurs": 600,
        },
    )
    packg: None | Package41 = field(
        default=None,
        metadata={
            "name": "Packg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeTransaction503:
    """
    TradeTransaction50__3 Provides details of the trade transaction.

    :ivar tx_id: TransactionIdentification Choice between a Unique
        Transaction Identifier (UTI) or a proprietary identifier as
        agreed with the counterparty.
    :ivar scndry_tx_id: SecondaryTransactionIdentification A proprietary
        internal trade identifier, as determined by the Reporting
        Counterparty. It enables internal tracing of Trade Repository
        records with the Reporting Counterparty records.&#13; &#13;
        Usage: SecondaryTransactionIdentification element is optional
        and is not intended to be used in any data handling to link a
        report to any previous report. For data handling,
        TransactionIdentification element shall be primarily used in
        case of linking reports, while the TechnicalRecordId element may
        also be used for technical tracing of records in each report,
        provided that this element is allowed for usage in a specific
        implementation of this message definition.
    :ivar prr_tx_id: PriorTransactionIdentification Choice between a
        Unique Transaction Identifier (UTI) or a proprietary identifier
        assigned to the predecessor transaction that has given rise to
        the reported transaction due to a lifecycle event.&#13;
        &#13;&#13; Usage: This data element is not applicable when
        reporting many-to-one and many-to-many relations between
        transactions (for example, in the case of a compression).&#13;
        &#13; This data element may be applicable when reporting one-to-
        one and one-to-many relations between transactions (for example,
        in the case of a clearing).&#13;&#13;
    :ivar coll_prtfl_cd: CollateralPortfolioCode Specifies the unique
        code assigned by the reporting counterparty to the portfolio if
        the collateral is posted on a portfolio basis.
    :ivar pltfm_idr: PlatformIdentifier Identifies the trading platform
        on which the derivative transaction was executed (for example,
        exchange, multilateral trading facility, swap execution
        facility). &#13; &#13; Usage: For transactions where no trading
        facility was involved, specific predefined codes have to be
        used.
    :ivar tx_pric: TransactionPrice Indicates the price per derivative
        excluding, where applicable, commission and accrued interest.
    :ivar ntnl_amt: NotionalAmount Indicates monetary or converted
        amount for the derivatives transaction.&#13; &#13; Usage: In
        case of partial terminations, and amortisations and in case of
        contracts where the notional, due to the characteristics of the
        contract, varies over time, it shall reflect the remaining
        notional after the change took place.&#13;
    :ivar ntnl_qty: NotionalQuantity Indicates for each leg of the
        transaction the total notional quantity of the underlying asset
        for the term of the transaction.
    :ivar dlvry_tp: DeliveryType Indicates whether the financial
        instrument is settled physically or in cash or decided at
        expiration time by counterparty.
    :ivar exctn_tm_stmp: ExecutionTimeStamp Indicates the date and time
        of the execution of the derivative transaction.
    :ivar fctv_dt: EffectiveDate Indicates the date when obligations
        under the contract come into effect.
    :ivar xprtn_dt: ExpirationDate Indicates the unadjusted date at
        which obligations under the derivative transaction stop being
        effective, as included in the confirmation.&#13; &#13;&#13; For
        European style options, date on which the holder can exercise
        the right or let it lapse.&#13;&#13; For American style options,
        the holder can exercise the right up to the expiry date.&#13;
        &#13;&#13; Usage: &#13; An early termination shall not be
        reported in this field.
    :ivar early_termntn_dt: EarlyTerminationDate Indicates the effective
        date of the early termination of the reported derivative
        transaction.
    :ivar sttlm_dt: SettlementDate Indicates the unadjusted date, as per
        the contract, by which all transfer of cash or assets should
        take place and the counterparties should no longer have any
        outstanding obligations to each other. &#13; For products that
        may not have a final contractual settlement date (eg American
        options), this data element reflects the date by which the
        transfer of cash or asset would take place if termination were
        to occur on the expiration date.
    :ivar deriv_evt: DerivativeEvent Indication of the derivative event
        of the transaction.
    :ivar trad_conf: TradeConfirmation Specifies whether the contract
        was electronically confirmed, non-electronically confirmed or
        remains unconfirmed.
    :ivar non_stdsd_term: NonStandardisedTerm Indicates whether the
        derivative transaction has one or more additional terms or
        provisions that materially affect the price of the
        transaction.&#13; &#13; Usage: If the element is not present,
        the NonStandardisedTerm is False.
    :ivar trad_clr: TradeClearing Information related to clearing of the
        reported contract.
    :ivar intrst_rate: InterestRate Information related to interest rate
        asset class type.
    :ivar ccy: Currency Information related to currency asset class
        type.
    :ivar cmmdty: Commodity Information related to commodity asset class
        type.
    :ivar optn: Option Information related to credit derivative asset
        class type.
    :ivar cdt: Credit Information related to credit derivative asset
        class type.
    :ivar othr_pmt: OtherPayment Payment related to elements not
        reported in dedicated fields.
    :ivar packg: Package A combination of two or more transactions that
        are reported separately but that are negotiated together as the
        product of a single economic agreement.
    """

    class Meta:
        name = "TradeTransaction50__3"

    tx_id: UniqueTransactionIdentifier2Choice1 = field(
        metadata={
            "name": "TxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    scndry_tx_id: None | str = field(
        default=None,
        metadata={
            "name": "ScndryTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "min_length": 1,
            "max_length": 72,
        },
    )
    prr_tx_id: None | UniqueTransactionIdentifier3Choice1 = field(
        default=None,
        metadata={
            "name": "PrrTxId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    coll_prtfl_cd: CollateralPortfolioCode6Choice1 = field(
        metadata={
            "name": "CollPrtflCd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    pltfm_idr: None | str = field(
        default=None,
        metadata={
            "name": "PltfmIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "pattern": r"[A-Z0-9]{4,4}",
        },
    )
    tx_pric: None | PriceData21 = field(
        default=None,
        metadata={
            "name": "TxPric",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ntnl_amt: NotionalAmountLegs51 = field(
        metadata={
            "name": "NtnlAmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    ntnl_qty: None | NotionalQuantityLegs51 = field(
        default=None,
        metadata={
            "name": "NtnlQty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    dlvry_tp: None | PhysicalTransferType4Code = field(
        default=None,
        metadata={
            "name": "DlvryTp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    exctn_tm_stmp: XmlDateTime = field(
        metadata={
            "name": "ExctnTmStmp",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    fctv_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "FctvDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    xprtn_dt: XmlDate = field(
        metadata={
            "name": "XprtnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    early_termntn_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EarlyTermntnDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    sttlm_dt: None | XmlDate = field(
        default=None,
        metadata={
            "name": "SttlmDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    deriv_evt: DerivativeEvent63 = field(
        metadata={
            "name": "DerivEvt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    trad_conf: None | TradeConfirmation4Choice1 = field(
        default=None,
        metadata={
            "name": "TradConf",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    non_stdsd_term: None | bool = field(
        default=None,
        metadata={
            "name": "NonStdsdTerm",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    trad_clr: TradeClearing111 = field(
        metadata={
            "name": "TradClr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    intrst_rate: None | InterestRateLegs141 = field(
        default=None,
        metadata={
            "name": "IntrstRate",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    ccy: None | CurrencyExchange221 = field(
        default=None,
        metadata={
            "name": "Ccy",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    cmmdty: None | AssetClassCommodity7Choice = field(
        default=None,
        metadata={
            "name": "Cmmdty",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    optn: None | OptionOrSwaption111 = field(
        default=None,
        metadata={
            "name": "Optn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    cdt: None | CreditDerivative41 = field(
        default=None,
        metadata={
            "name": "Cdt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    othr_pmt: list[OtherPayment51] = field(
        default_factory=list,
        metadata={
            "name": "OthrPmt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "max_occurs": 600,
        },
    )
    packg: None | Package41 = field(
        default=None,
        metadata={
            "name": "Packg",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class CommonTradeDataReport711:
    """
    CommonTradeDataReport71__1 Information related to contract and
    transaction details.

    :ivar ctrct_data: ContractData Data related to a trade contract.
    :ivar tx_data: TransactionData Data related to a trade transaction.
    """

    class Meta:
        name = "CommonTradeDataReport71__1"

    ctrct_data: ContractType151 = field(
        metadata={
            "name": "CtrctData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tx_data: TradeTransaction501 = field(
        metadata={
            "name": "TxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class CommonTradeDataReport712:
    """
    CommonTradeDataReport71__2 Information related to contract and
    transaction details.

    :ivar ctrct_data: ContractData Data related to a trade contract.
    :ivar tx_data: TransactionData Data related to a trade transaction.
    """

    class Meta:
        name = "CommonTradeDataReport71__2"

    ctrct_data: ContractType151 = field(
        metadata={
            "name": "CtrctData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tx_data: TradeTransaction502 = field(
        metadata={
            "name": "TxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class CommonTradeDataReport713:
    """
    CommonTradeDataReport71__3 Information related to contract and
    transaction details.

    :ivar ctrct_data: ContractData Data related to a trade contract.
    :ivar tx_data: TransactionData Data related to a trade transaction.
    """

    class Meta:
        name = "CommonTradeDataReport71__3"

    ctrct_data: ContractType151 = field(
        metadata={
            "name": "CtrctData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tx_data: TradeTransaction503 = field(
        metadata={
            "name": "TxData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class TradeData434:
    """
    TradeData43__4 Provides details of a new trade transaction report.

    :ivar ctr_pty_spcfc_data: CounterpartySpecificData Data specific to
        counterparties and related fields.
    :ivar cmon_trad_data: CommonTradeData Data specifically related to
        transaction.
    :ivar tech_attrbts: TechnicalAttributes Specifies technical
        attributes of the message.
    :ivar splmtry_data: SupplementaryData Additional information that
        can not be captured in the structured fields and/or any other
        specific block.
    """

    class Meta:
        name = "TradeData43__4"

    ctr_pty_spcfc_data: CounterpartySpecificData362 = field(
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    cmon_trad_data: CommonTradeDataReport714 = field(
        metadata={
            "name": "CmonTradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tech_attrbts: TechnicalAttributes51 = field(
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    splmtry_data: None | SupplementaryData1 = field(
        default=None,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeData435:
    """
    TradeData43__5 Provides details of a new trade transaction report.

    :ivar ctr_pty_spcfc_data: CounterpartySpecificData Data specific to
        counterparties and related fields.
    :ivar cmon_trad_data: CommonTradeData Data specifically related to
        transaction.
    :ivar tech_attrbts: TechnicalAttributes Specifies technical
        attributes of the message.
    :ivar splmtry_data: SupplementaryData Additional information that
        can not be captured in the structured fields and/or any other
        specific block.
    """

    class Meta:
        name = "TradeData43__5"

    ctr_pty_spcfc_data: CounterpartySpecificData363 = field(
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    cmon_trad_data: CommonTradeDataReport715 = field(
        metadata={
            "name": "CmonTradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tech_attrbts: TechnicalAttributes51 = field(
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    splmtry_data: None | SupplementaryData1 = field(
        default=None,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeData436:
    """
    TradeData43__6 Provides details of a new trade transaction report.

    :ivar ctr_pty_spcfc_data: CounterpartySpecificData Data specific to
        counterparties and related fields.
    :ivar cmon_trad_data: CommonTradeData Data specifically related to
        transaction.
    :ivar tech_attrbts: TechnicalAttributes Specifies technical
        attributes of the message.
    :ivar splmtry_data: SupplementaryData Additional information that
        can not be captured in the structured fields and/or any other
        specific block.
    """

    class Meta:
        name = "TradeData43__6"

    ctr_pty_spcfc_data: CounterpartySpecificData362 = field(
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    cmon_trad_data: CommonTradeDataReport716 = field(
        metadata={
            "name": "CmonTradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tech_attrbts: TechnicalAttributes51 = field(
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    splmtry_data: None | SupplementaryData1 = field(
        default=None,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeData437:
    """
    TradeData43__7 Provides details of a new trade transaction report.

    :ivar ctr_pty_spcfc_data: CounterpartySpecificData Data specific to
        counterparties and related fields.
    :ivar cmon_trad_data: CommonTradeData Data specifically related to
        transaction.
    :ivar tech_attrbts: TechnicalAttributes Specifies technical
        attributes of the message.
    :ivar splmtry_data: SupplementaryData Additional information that
        can not be captured in the structured fields and/or any other
        specific block.
    """

    class Meta:
        name = "TradeData43__7"

    ctr_pty_spcfc_data: CounterpartySpecificData362 = field(
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    cmon_trad_data: CommonTradeDataReport717 = field(
        metadata={
            "name": "CmonTradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tech_attrbts: TechnicalAttributes51 = field(
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    splmtry_data: None | SupplementaryData1 = field(
        default=None,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeData431:
    """
    TradeData43__1 Provides details of a new trade transaction report.

    :ivar ctr_pty_spcfc_data: CounterpartySpecificData Data specific to
        counterparties and related fields.
    :ivar cmon_trad_data: CommonTradeData Data specifically related to
        transaction.
    :ivar tech_attrbts: TechnicalAttributes Specifies technical
        attributes of the message.
    :ivar splmtry_data: SupplementaryData Additional information that
        can not be captured in the structured fields and/or any other
        specific block.
    """

    class Meta:
        name = "TradeData43__1"

    ctr_pty_spcfc_data: CounterpartySpecificData361 = field(
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    cmon_trad_data: CommonTradeDataReport711 = field(
        metadata={
            "name": "CmonTradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tech_attrbts: TechnicalAttributes51 = field(
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    splmtry_data: None | SupplementaryData1 = field(
        default=None,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeData432:
    """
    TradeData43__2 Provides details of a new trade transaction report.

    :ivar ctr_pty_spcfc_data: CounterpartySpecificData Data specific to
        counterparties and related fields.
    :ivar cmon_trad_data: CommonTradeData Data specifically related to
        transaction.
    :ivar tech_attrbts: TechnicalAttributes Specifies technical
        attributes of the message.
    :ivar splmtry_data: SupplementaryData Additional information that
        can not be captured in the structured fields and/or any other
        specific block.
    """

    class Meta:
        name = "TradeData43__2"

    ctr_pty_spcfc_data: CounterpartySpecificData361 = field(
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    cmon_trad_data: CommonTradeDataReport712 = field(
        metadata={
            "name": "CmonTradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tech_attrbts: TechnicalAttributes51 = field(
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    splmtry_data: None | SupplementaryData1 = field(
        default=None,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeData433:
    """
    TradeData43__3 Provides details of a new trade transaction report.

    :ivar ctr_pty_spcfc_data: CounterpartySpecificData Data specific to
        counterparties and related fields.
    :ivar cmon_trad_data: CommonTradeData Data specifically related to
        transaction.
    :ivar tech_attrbts: TechnicalAttributes Specifies technical
        attributes of the message.
    :ivar splmtry_data: SupplementaryData Additional information that
        can not be captured in the structured fields and/or any other
        specific block.
    """

    class Meta:
        name = "TradeData43__3"

    ctr_pty_spcfc_data: CounterpartySpecificData361 = field(
        metadata={
            "name": "CtrPtySpcfcData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    cmon_trad_data: CommonTradeDataReport713 = field(
        metadata={
            "name": "CmonTradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    tech_attrbts: TechnicalAttributes51 = field(
        metadata={
            "name": "TechAttrbts",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    splmtry_data: None | SupplementaryData1 = field(
        default=None,
        metadata={
            "name": "SplmtryData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeReport33Choice1:
    """
    TradeReport33Choice__1 Position/transaction reporting under the local
    regulation.

    :ivar new: New Indicates whether transaction is reported for the
        first time.
    :ivar mod: Modification Indicates a modification to the terms or
        details of a previously reported transaction, but not a
        correction.
    :ivar crrctn: Correction Indicates that the report is correcting the
        erroneous data fields of a previously submitted report.
    :ivar termntn: Termination Indicates that reported transaction is a
        termination or an early termination of an existing contract.
    :ivar valtn_upd: ValuationUpdate Indicates an update of a contract
        valuation or collateral.
    :ivar err: Error Indicates a cancellation of a wrongly submitted
        entire report in case the contract never came into existence or
        was not subject to reporting requirements but was reported to a
        trade repository by mistake or a cancellation of duplicate
        report.
    :ivar port_out: PortOut Indicates transfers swap transaction from
        one SDR to another SDR (change of swap data repository).
    :ivar rvv: Revive Re-opening of a derivative, at a trade or position
        level, that was cancelled with action type ‘Error’ or terminated
        by mistake.
    """

    class Meta:
        name = "TradeReport33Choice__1"

    new: None | TradeData431 = field(
        default=None,
        metadata={
            "name": "New",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    mod: None | TradeData432 = field(
        default=None,
        metadata={
            "name": "Mod",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    crrctn: None | TradeData433 = field(
        default=None,
        metadata={
            "name": "Crrctn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    termntn: None | TradeData434 = field(
        default=None,
        metadata={
            "name": "Termntn",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    valtn_upd: None | TradeData435 = field(
        default=None,
        metadata={
            "name": "ValtnUpd",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    err: None | TradeData436 = field(
        default=None,
        metadata={
            "name": "Err",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    port_out: None | TradeData437 = field(
        default=None,
        metadata={
            "name": "PortOut",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )
    rvv: None | TradeData433 = field(
        default=None,
        metadata={
            "name": "Rvv",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        },
    )


@dataclass(kw_only=True)
class TradeData59Choice1:
    """
    TradeData59Choice__1 Reporting of position or transaction for trade
    lifecycle events.

    :ivar rpt: Report Reporting of position or transaction for trade
        lifecycle events.
    """

    class Meta:
        name = "TradeData59Choice__1"

    rpt: list[TradeReport33Choice1] = field(
        default_factory=list,
        metadata={
            "name": "Rpt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
            "max_occurs": 2500,
        },
    )


@dataclass(kw_only=True)
class DerivativesTradeReportV04:
    """
    DerivativesTradeReportV04 The DerivativesTradeReport message is sent by
    the report submitting entity to the trade repository (TR) to report on
    the derivative transactions or sent by the trade repository (TR) to the
    authority or made available by the trade repository (TR) to the report
    submitting entity and the reporting counterparty as well as the entity
    responsible for reporting, if applicable.

    :ivar rpt_hdr: ReportHeader Header information related to metadata
        of report message.
    :ivar trad_data: TradeData Data concerning the reporting trade.
    """

    rpt_hdr: TradeReportHeader41 = field(
        metadata={
            "name": "RptHdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )
    trad_data: TradeData59Choice1 = field(
        metadata={
            "name": "TradData",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04",
        }
    )


@dataclass(kw_only=True)
class Document:
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:auth.030.001.04"

    derivs_trad_rpt: DerivativesTradeReportV04 = field(
        metadata={
            "name": "DerivsTradRpt",
            "type": "Element",
        }
    )
