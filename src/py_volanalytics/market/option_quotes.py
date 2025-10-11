"""Quote for a European Vanilla Option"""

from typing import Optional, List, Any
import attrs
from attrs import define, field
from py_volanalytics.valuation_framework.market_data import (
    MarketObjectId,
    MarketObject,
    MarketObjects,
)
from py_volanalytics.types.enums import (
    StrikeConvention,
    OptionQuoteConvention,
    OptionType,
)


@define(kw_only=True)
class OptionQuotesId(MarketObjectId):
    """Class to represent a European Vanilla Option quote identifier"""

    _symbol: str = field(validator=attrs.validators.instance_of(str), alias="symbol")

    @property
    def symbol(self):
        return self._symbol


@define(kw_only=True)
class OptionQuote:
    """Quote for European-style vanilla options"""

    _strike_convention: StrikeConvention = field(
        default=StrikeConvention.SIMPLE,
        validator=attrs.validators.instance_of(StrikeConvention),
        alias="strike_convention",
    )

    _option_type: OptionType = field(
        validator=attrs.validators.instance_of(OptionType), alias="option_type"
    )
    _strike_point: float = field(
        validator=attrs.validators.instance_of(float), alias="strike_point"
    )
    _time_to_expiry: float = field(
        default=1.0, validator=attrs.validators.ge(0.0), alias="time_to_expiry"
    )

    _quote_convention: OptionQuoteConvention = field(
        default=OptionQuoteConvention.PRICE,
        validator=attrs.validators.instance_of(OptionQuoteConvention),
        alias="quote_convention",
    )
    _quote: float = field(validator=attrs.validators.instance_of(float), alias="quote")

    @property
    def option_type(self):
        return self._option_type

    @property
    def strike_point(self):
        return self._strike_point

    @property
    def time_to_expiry(self):
        return self._time_to_expiry

    @property
    def strike_convention(self):
        return self._strike_convention

    @property
    def quote_convention(self):
        return self._quote_convention

    @property
    def quote(self):
        return self._quote


@define(kw_only=True)
class OptionQuotes(MarketObject):

    _option_quotes: List[OptionQuote] = field(
        validator=attrs.validators.instance_of(list), alias="option_quotes"
    )

    @property
    def option_quotes(self):
        return self._option_quotes

    @staticmethod
    def create(symbol: str, option_quotes: List[OptionQuote]):
        return OptionQuotes(
            id=OptionQuotesId(friendly_name=MarketObjects.OPTION_QUOTES, symbol=symbol),
            option_quotes=option_quotes,
        )
