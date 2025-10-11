"""Discounting Curve.

The ``DiscountingCurve`` object stores a vector of dates(times) and discount factors.
This allows us to value all instruments consistently within a single valuation framework.

"""

import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

import attrs
from attrs import define, field
from typing import Union, Optional
from py_volanalytics.types.enums import Currency
from py_volanalytics.valuation_framework.market_data import (
    MarketObjectId,
    MarketObject,
    MarketObjects,
)
from py_volanalytics.math.interpolator import InterpolationType, interpolator_map

plt.style.use("science")


@define(kw_only=True)
class DiscountingCurveId(MarketObjectId):
    """Class to represent a Discounting Curve identifier"""

    _currency: Currency = field(
        default=Currency.USD,
        validator=attrs.validators.instance_of(Currency),
        alias="currency",
    )
    _collateral: Currency = field(
        default=Currency.USD,
        validator=attrs.validators.instance_of(Currency),
        alias="collateral",
    )

    @property
    def currency(self):
        return self._currency

    @property
    def collateral(self):
        return self._collateral


@define(kw_only=True)
class DiscountingCurve(MarketObject):
    """Class to represent a discounting curve object."""

    _times: np.ndarray[Union[dt.date, float]] = field(alias="times")
    _discount_factors: np.ndarray[float] = field(alias="discount_factors")
    _interpolation_type: InterpolationType = field(
        default=InterpolationType.LINEAR_INTERPOLATION,
        validator=attrs.validators.instance_of(InterpolationType),
        alias="interapolation_type",
    )

    @_times.validator
    def validate_times(self, attributes, values):
        """Validate array of times."""
        if not values:
            raise ValueError("array of time values is empty.")
        if len(values) == 1:
            raise ValueError("array of time values must be of length >= 2")

        if not isinstance(self._times, np.ndarray[Union[dt.date, float]]):
            raise ValueError("times must be dates or float array")

        zero_point = dt.timedelta(0) if isinstance(values[0], dt.date) else 0
        for i in range(len(values) - 1):
            if values[i + 1] - values[i] < zero_point:
                raise ValueError("array of time values is not sorted")

    def __attrs_post_init__(self):
        if len(self._discount_factors) != len(self._times):
            raise ValueError(
                "length of _discount_factors array must equal length of _times array"
            )

        if not isinstance(self._discount_factors, np.ndarray[float]):
            raise ValueError("_discount_factors must be of type float array")

        # Get the interpolator class based on the interpolation type
        interpolator_class = interpolator_map.get(self._interpolation_type)

        if interpolator_class is None:
            raise ValueError(f"Invalid interpolator type: {self._interpolation_type}")

        # Initialize the interpolator
        self._interpolator = interpolator_class(self._times, self._discount_factors)

    def df(self, t: float, T: float) -> float:
        disc_fact_t = self._interpolator(t)  # df(0,t) = e^{-rt}
        disc_fact_T = self._interpolator(T)  # df(0,T) = e^{-rT}

        disc_fact = disc_fact_T / disc_fact_t  # df(t,T) = e^{-r(T-t)}

        return disc_fact

    @staticmethod
    def create_from_rate_curve(
        trade_ccy: Currency,
        collateral_ccy: Currency,
        times: np.ndarray[Union[dt.date, float]],
        rates: np.ndarray[float],
        anchor_date: Optional[dt.date],
    ):
        """
        Creates a discounting curve given an array of times
        and annually compounded spot interest rates, assuming Act/365 basis
        """
        if isinstance(times, np.ndarray[dt.date]):
            times = (times - anchor_date).days() / 365.0

        dfs = 1 / (1.0 + rates) ** times
        times = np.concat([[0.0], times])
        dfs = np.concat([[1.0], dfs])

        return DiscountingCurve(
            id=DiscountingCurveId(
                friendly_name=MarketObjects.DISCOUNTING_CURVE,
                currency=trade_ccy,
                collateral=collateral_ccy,
            ),
            times=times,
            discount_factors=dfs,
        )
