"""Quote for a European Vanilla Option"""

from typing import Optional, List
import attrs
from attrs import define, field
from py_volanalytics.valuation_framework.market_data import (
    MarketObjectId,
    MarketObject,
    MarketObjects,
)


@define(kw_only=True)
class ForwardQuotesId(MarketObjectId):
    """Class to represent a European Vanilla Option quote identifier"""

    _symbol: str = field(validator=attrs.validators.instance_of(str), alias="symbol")

    @property
    def symbol(self):
        return self._symbol


@define(kw_only=True)
class ForwardQuote:
    """Quote for ATM forwards expiring at maturity T"""

    _time_to_expiry: float = field(
        default=1.0, validator=attrs.validators.ge(0.0), alias="time_to_expiry"
    )

    _quote: float = field(validator=attrs.validators.instance_of(float), alias="quote")

    @property
    def time_to_expiry(self):
        return self._time_to_expiry

    @property
    def quote(self):
        return self._quote


@define(kw_only=True)
class ForwardQuotes(MarketObject):

    _forward_quotes: List[ForwardQuote] = field(
        validator=attrs.validators.instance_of(list),
        alias="forward_quotes",
    )

    @property
    def forward_quotes(self):
        return self._forward_quotes

    @staticmethod
    def create(symbol: str, forward_quotes: List[ForwardQuote]):
        return ForwardQuotes(
            id=ForwardQuotesId(
                friendly_name=MarketObjects.FORWARD_QUOTES, symbol=symbol
            ),
            forward_quotes=forward_quotes,
        )
