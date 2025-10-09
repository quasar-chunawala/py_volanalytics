"""
This base class provides the ability to build market objects.
"""

from abc import abstractmethod
from attrs import field, define
from typing import List, Any
from py_volanalytics.valuation_framework.market_data import (
    MarketObjectId,
    MarketObject,
    MarketEnvironment,
)
from py_volanalytics.types.enums import GMOBState


@define(kw_only=True)
class GenericMarketObjectBuilder:
    """Component that is used in py_volanalytics to create market data"""

    _state: GMOBState = field(default=GMOBState.CREATED)

    @abstractmethod
    def initialize(self) -> Any:
        """Initialize the GMOB and return an InitializedState"""
        pass

    @abstractmethod
    def get_static_dependencies(self, initialized_state: Any) -> Any:
        """Get all the static data dependencies"""
        pass

    @abstractmethod
    def get_market_dependencies(
        self,
        initialized_state: Any,
        reference_data: Any,
    ) -> List[MarketObjectId]:
        """Get all market data dependencies"""
        pass

    @abstractmethod
    def calculate(
        self,
        initialized_state: Any,
        reference_data: Any,
        market_data: MarketEnvironment,
    ) -> MarketObject:
        """Evaluates the Market Object Builder"""
        pass

    def advance_state(self):
        if self._state == GMOBState.CREATED:
            self._state = GMOBState.INITIALIZED

        if self._state == GMOBState.INITIALIZED:
            self._state = GMOBState.REF_DATA_DISCOVERY_COMPLETE

        if self._state == GMOBState.REF_DATA_DISCOVERY_COMPLETE:
            self._state = GMOBState.MARKET_DATA_DISCOVERY_COMPLETE

        if self._state == GMOBState.MARKET_DATA_DISCOVERY_COMPLETE:
            self._state = GMOBState.EXECUTION_COMPLETE

    def validate(
        self,
        initialized_state: Any,
        reference_data: Any,
        market_data: MarketEnvironment,
    ):
        # Validation phase
        deps = self.get_market_dependencies(initialized_state, reference_data)
        market_objects: List[MarketObject] = [
            mkt_obj
            for service in market_data.get_values()
            for mkt_obj in service.get_values()
        ]
        market_keys = [mkt_obj.get_market_object_id() for mkt_obj in market_objects]

        for dep in deps:
            if dep not in market_keys:
                raise ValueError(f"{dep} not found in the market env!")
