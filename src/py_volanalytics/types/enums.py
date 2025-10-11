"""This module contains globally accessible enums"""

from enum import Enum, StrEnum, IntEnum, auto


class OptionType(Enum):
    """The type of option contract."""

    CALL_OPTION = auto()
    PUT_OPTION = auto()


class Moneyness(Enum):
    """The moneyness of an option in Delta-convention"""

    TEN_DELTA_CALL = auto()
    TWENTY_FIVE_DELTA_CALL = auto()
    ATM = auto()
    TWENTY_FIVE_DELTA_PUT = auto()
    TEN_DELTA_PUT = auto()


class ExerciseStyle(Enum):
    """The exercise style of an option"""

    EUROPEAN = auto()
    AMERICAN = auto()
    BERMUDAN = auto()


class OptionQuoteConvention(Enum):
    """The exercise style of an option"""

    IMPLIED_VOLATILITY = auto()
    PRICE = auto()


class StrikeConvention(Enum):
    """The strike convention for an option"""

    SIMPLE = auto()
    DELTA = auto()
    FORWARD_MONEYNESS = auto()
    LOG_FORWARD_MONEYNESS = auto()


class Currency(StrEnum):
    AED = "AED"
    ARS = "ARS"
    AUD = "AUD"
    BGN = "BGN"
    BHD = "BHD"
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CLP = "CLP"
    CNH = "CNH"
    CNY = "CNY"
    COP = "COP"
    CZK = "CZK"
    DKK = "DKK"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    HKD = "HKD"
    HRK = "HRK"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    INR = "INR"
    ISK = "ISK"
    JPY = "JPY"
    KRW = "KRW"
    KZT = "KZT"
    MAD = "MAD"
    MXN = "MXN"
    MYR = "MYR"
    NOK = "NOK"
    NZD = "NZD"
    OMR = "OMR"
    PEN = "PEN"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    QAR = "QAR"
    RON = "RON"
    RUB = "RUB"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    THB = "THB"
    TRY = "TRY"
    TWD = "TWD"
    UAH = "UAH"
    USD = "USD"
    VND = "VND"
    XAG = "XAG"
    XAU = "XAU"
    XPD = "XPD"
    XPT = "XPT"
    XXX = "XXX"
    ZAR = "ZAR"


class MarketDataServiceId(Enum):
    """A list of all market data service ids"""

    DISCOUNTING_CURVE_SERVICE = "DISCOUNTING_CURVE_SERVICE"
    DEFAULT_CURVE_SERVICE = "DEFAULT_CURVE_SERVICE"
    IMPLIED_VOLATILITY_SURFACE_SERVICE = "IMPLIED_VOLATILITY_SERVICE"
    TIME_SERVICE = "TIME_SERVICE"
    LOCAL_VOLATILITY_SURFACE_SERVICE = "LOCAL_VOLATILITY_SERVICE"
    OPTION_QUOTES_SERVICE = "OPTION_QUOTES_SERVICE"
    FORWARD_QUOTES_SERVICE = "FORWARD_QUOTES_SERVICE"


class MarketObjects(Enum):
    """A list of market object names"""

    DISCOUNTING_CURVE = "DISCOUNTING_CURVE"
    DEFAULT_CURVE = "DEFAULT_CURVE"
    IMPLIED_VOLATILITY_SURFACE = "IMPLIED_VOLATILITY_SURFACE"
    TIME = "TIME"
    LOCAL_VOLATILITY_SURFACE = "LOCAL_VOLATILITY_SURFACE"
    OPTION_QUOTES = "OPTION_QUOTES"
    FORWARD_QUOTES = "FORWARD_QUOTES"


class GMOBState(Enum):
    """Various possible states for a MOB"""

    CREATED = auto()
    INITIALIZED = auto()
    REF_DATA_DISCOVERY_COMPLETE = auto()
    MARKET_DATA_DISCOVERY_COMPLETE = auto()
    EXECUTION_COMPLETE = auto()
    RESULTS_GEN_COMPLETE = auto()


class TimeInfo(Enum):
    """Info about a TimeObject"""

    PV_DATE = auto()
    TODAY = auto()
