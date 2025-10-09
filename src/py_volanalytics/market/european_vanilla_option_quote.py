"""Quote for a European Vanilla Option"""

from typing import Optional, List
import attrs
from attrs import define, field
from py_volanalytics.valuation_framework.market_data import MarketObjectId, MarketObject
from py_volanalytics.types.enums import (
    StrikeConvention,
    OptionQuoteConvention,
    OptionType,
)


@define(kw_only=True)
class EuropeanVanillaOptionQuoteId(MarketObjectId):
    """Class to represent a European Vanilla Option quote identifier"""

    _option_type: OptionType = field(validator=attrs.validators.instance_of(OptionType))
    _strike_point: float = field(validator=attrs.validators.instance_of(float))
    _time_to_expiry: float = field(default=1.0, validator=attrs.validators.ge(0.0))
    _strike_convention: StrikeConvention = field(
        default=StrikeConvention.SIMPLE,
        validator=attrs.validators.instance_of(StrikeConvention),
    )

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


@define(kw_only=True)
class EuropeanVanillaOptionQuote(MarketObject):
    """Quote for European-style vanilla options"""

    _id: EuropeanVanillaOptionQuoteId = field(
        validator=attrs.validators.instance_of(EuropeanVanillaOptionQuoteId)
    )
    _quote_convention: OptionQuoteConvention = field(
        default=OptionQuoteConvention.PRICE,
        validator=attrs.validators.instance_of(OptionQuoteConvention),
    )
    _quote: float = field(validator=attrs.validators.ge(0.0))

    def get_market_object_id(self) -> EuropeanVanillaOptionQuoteId:
        """Return the DiscountCurveId"""
        return self._id


@define(kw_only=True)
class EuropeanVanillaOptionQuotesId:
    """Class to represent a collection of vanilla quotes Id"""

    _underlying_symbol: str = field(
        validator=attrs.validators.instance_of(str), alias="underlying_symbol"
    )

    @property
    def underlying_symbol(self):
        return self._underlying_symbol


@define(kw_only=True)
class EuropeanVanillaOptionQuotes(MarketObject):
    """Class to represent a collection vanilla option quotes data"""

    _id: EuropeanVanillaOptionQuotesId = field(
        validator=attrs.validators.instance_of(EuropeanVanillaOptionQuotesId)
    )
    _option_quotes: List[EuropeanVanillaOptionQuote] = field(
        validator=attrs.validators.instance_of(List[EuropeanVanillaOptionQuote])
    )

    def get_market_object_id(self) -> EuropeanVanillaOptionQuotesId:
        """Return the EuropeanVanillaOptionQuotesId"""
        return self._id
