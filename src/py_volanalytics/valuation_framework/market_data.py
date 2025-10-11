"""
Framework for market data objects such as curves, volatility surface, valuation date.
"""

from typing import Optional, Any, List
from abc import ABC, abstractmethod
import attrs
from attrs import define, field
from py_volanalytics.types.enums import MarketDataServiceId, MarketObjects


@define(kw_only=True)
class MarketObjectId:
    """Base class for all market object identifiers"""

    _friendly_name: MarketObjects = field(
        validator=attrs.validators.instance_of(MarketObjects), alias="friendly_name"
    )

    def get_id(self) -> dict:
        return attrs.asdict(self)

    @property
    def friendly_name(self):
        return self._friendly_name


@define(kw_only=True)
class MarketObject:

    _id: MarketObjectId = field(
        validator=attrs.validators.instance_of(MarketObjectId), alias="id"
    )

    @abstractmethod
    def get_market_object_id(self) -> MarketObjectId:
        return self._id


@define(kw_only=True)
class MarketDataService:
    """Base class for all market data services"""

    _id: MarketDataServiceId = field(
        alias="id", validator=attrs.validators.instance_of(MarketDataServiceId)
    )
    _market_data_dict: dict = field(alias="market_data_dict")

    def get_keys(self):
        """Get all market data keys inside this service"""
        return self._market_data_dict.keys()

    def get_values(self):
        """Get all market objects inside this service"""
        return self._market_data_dict.values()

    def get_value(self, key: dict) -> MarketObject:
        """Get market data object for the user-supplied key"""
        key = tuple(key.values())
        return self._market_data_dict[key]

    def try_find_key(self, key: dict) -> Optional[MarketObject]:
        """Try to find the market data object for the user-supplied key"""
        key = tuple(key.values())
        if key not in self._market_data_dict:
            return None

        return self._market_data_dict[key]

    def get_service_id(self) -> Any:
        return self._id

    @property
    def market_data_dict(self):
        return self._market_data_dict

    @property
    def id(self):
        return self._id

    @staticmethod
    def create(service_id: MarketDataServiceId, market_objects: List[MarketObject]):
        keys = [obj.get_market_object_id() for obj in market_objects]
        market_data_dict = {}

        for k, v in list(zip(keys, market_objects)):
            k = tuple(k.get_id().values())
            market_data_dict[k] = v

        return MarketDataService(id=service_id, market_data_dict=market_data_dict)


@define(kw_only=True)
class MarketEnvironment:
    """Class representing a collection of Market data services"""

    _market_data_services: dict[MarketDataServiceId, MarketDataService] = field(
        validator=attrs.validators.instance_of(dict),
        alias="market_data_services",
    )

    def get_keys(self):
        """Get all market data keys inside this service"""
        return self._market_data_services.keys()

    def get_values(self):
        """Get all market objects inside this service"""
        return self._market_data_services.values()

    def get_value(self, key: MarketDataServiceId) -> MarketDataService:
        """Get market data object for the user-supplied key"""

        return self._market_data_services[key]

    def try_find_key(self, key: MarketDataServiceId) -> Optional[MarketDataService]:
        """Try to find the market data object for the user-supplied key"""

        if key not in self._market_data_services:
            return None

        return self._market_data_services[key]

    @staticmethod
    def create(services: List[MarketDataService]):
        market_data_services_dict = {}
        service_ids = [sv.get_service_id() for sv in services]

        for k, v in list(zip(service_ids, services)):
            market_data_services_dict[k] = v

        return MarketEnvironment(market_data_services=market_data_services_dict)
