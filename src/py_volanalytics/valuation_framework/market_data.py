""" 
Framework for market data objects such as curves, volatility surface, valuation date.
"""

from typing import Optional, Any
from abc import ABC, abstractmethod
import attrs
from attrs import define, field
from py_volanalytics.types.enums import MarketDataServiceId

@define(kw_only=True)    
class MarketObject:
    
    @abstractmethod
    def get_market_object_id(self) -> dict:
        pass

@define(kw_only=True)
class MarketDataService:
    """ Abstract base class for all market data services """
    _id: MarketDataServiceId = field(alias=id)
    _market_data_dict: dict = field(alias="market_data_dict")
    
    def get_keys(self):
        """ Get all market data keys inside this service """
        return self._market_data_dict.keys();
    
    def get_values(self):
        """ Get all market objects inside this service """
        return self._market_data_dict.values();
    
    def get_value(self, key) -> MarketObject:
        """ Get market data object for the user-supplied key """
        
        return self._market_data_dict[key]
        
    def try_find_key(self, key) -> Optional[MarketObject]:
        """ Try to find the market data object for the user-supplied key """
        
        if(not(key in self._market_data_dict)):
            return None
        
        return self._market_data_dict[key]
        
    def get_service_id(self) -> MarketDataServiceId:
        return self._id
    
    
@define(kw_only=True)
class MarketEnvironment:    
    """ Class representing a collection of Market data services """
    _market_data_services : dict[Any,MarketObject] = field(validator=attrs.validators.instance_of(dict[Any,MarketObject]))
    
    def get_keys(self):
        """ Get all market data keys inside this service """
        return self._market_data_services.keys();
    
    def get_values(self):
        """ Get all market objects inside this service """
        return self._market_data_services.values();
    
    def get_value(self, key) -> MarketDataService:
        """ Get market data object for the user-supplied key """
        
        return self._market_data_services[key]
        
    def try_find_key(self, key) -> Optional[MarketDataService]:
        """ Try to find the market data object for the user-supplied key """
        
        if(not(key in self._market_data_services)):
            return None
        
        return self._market_data_services[key]
        