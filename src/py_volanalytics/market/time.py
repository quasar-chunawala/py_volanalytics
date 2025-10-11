"""Market service for TODAY date"""

import datetime
from typing import Optional, List
import attrs
from attrs import define, field

from py_volanalytics.valuation_framework.market_data import MarketObjectId, MarketObject
from py_volanalytics.types.enums import TimeInfo, MarketObjects


@define(kw_only=True)
class TimeObjectId(MarketObjectId):
    """Class to represent a Time object identifier"""

    _time_info: TimeInfo = field(
        validator=attrs.validators.instance_of(TimeInfo), alias="time_info"
    )

    @property
    def time_info(self):
        return self._time_info


@define(kw_only=True)
class Time(MarketObject):
    _date: datetime.date = field(
        validator=attrs.validators.instance_of(datetime.date), alias="date"
    )

    @property
    def date(self):
        return self._date

    @staticmethod
    def create(time_info: TimeInfo, date: datetime.date):
        return Time(
            id=TimeObjectId(friendly_name=MarketObjects.TIME, time_info=time_info),
            date=date,
        )
