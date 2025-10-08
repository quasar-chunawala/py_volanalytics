""" This module contains globally accessible enums """

from enum import Enum, StrEnum, IntEnum, auto

class OptionType(Enum):
    """The type of option contract."""

    CALL_OPTION = auto()
    PUT_OPTION = auto()

class Moneyness(Enum):
    """ The moneyness of an option in Delta-convention """
    TEN_DELTA_CALL = auto()
    TWENTY_FIVE_DELTA_CALL = auto()
    ATM = auto()
    TWENTY_FIVE_DELTA_PUT = auto()
    TEN_DELTA_PUT = auto()

class ExerciseStyle(Enum):
    """ The exercise style of an option"""
    EUROPEAN = auto()
    AMERICAN = auto()
    BERMUDAN = auto()
    
class OptionQuoteConvention(Enum):
    """ The exercise style of an option"""
    IMPLIED_VOLATILITY = auto()
    PRICE = auto()
    
class StrikeConvention(Enum):
    """ The strike convention for an option """
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
    """ A list of all market data service ids """
    DISCOUNTING_CURVE = auto()
    DEFAULT_CURVE = auto()
    VOLATILITY_SURFACE = auto()