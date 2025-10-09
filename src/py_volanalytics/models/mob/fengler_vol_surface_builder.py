"""Fengler's volatility smoothening algorithm"""

from typing import Any, List
import attrs
from attrs import define, field

from py_volanalytics.market.time import TimeInfo, TimeObjectId
from py_volanalytics.market.european_vanilla_option_quote import (
    EuropeanVanillaOptionQuotesId,
)
from py_volanalytics.valuation_framework.generic_market_object_builder import (
    GenericMarketObjectBuilder,
)
from py_volanalytics.valuation_framework.market_data import (
    MarketObjectId,
    MarketEnvironment,
    MarketObject,
)


@define(kw_only=True)
class FenglerVolSurfaceBuilder(GenericMarketObjectBuilder):
    _symbol: str = field(validator=attrs.validators.instance_of(str), alias="symbol")

    """ 
    An implementation of the Fengler(2009)'s volatility smoothening
    algorithm to construct an implied volatility surface.
    """

    def initialize(self):
        """Initialize the GMOB and return an InitializedState"""
        super().advance_state()

    def get_static_dependencies(self, initialized_state: Any) -> Any:
        """Get all the static data dependencies"""
        super().advance_state()

    def get_market_dependencies(
        self,
        initialized_state: Any,
        reference_data: Any,
    ) -> List[MarketObjectId]:
        """Get all market data dependencies"""
        deps = [
            TimeObjectId(time_info=TimeInfo.TODAY),
            TimeObjectId(time_info=TimeInfo.PV_DATE),
            EuropeanVanillaOptionQuotesId(underlying_symbol=self._symbol),
        ]
        super().advance_state()
        return deps

    def calculate(
        self,
        initialized_state: Any,
        reference_data: Any,
        market_data: MarketEnvironment,
    ) -> MarketObject:
        """Evaluates the Market Object Builder"""

        # Validation phase
        super().validate(initialized_state, reference_data, market_data)
