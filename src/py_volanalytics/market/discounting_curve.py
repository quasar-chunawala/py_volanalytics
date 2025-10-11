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
from py_volanalytics.math.interpolator import (
    InterpolationType,
    interpolator_map,
    Interpolator,
)

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
        default=InterpolationType.LOG_LINEAR_INTERPOLATION,
        validator=attrs.validators.instance_of(InterpolationType),
        alias="interapolation_type",
    )
    _interpolator: Optional[Interpolator] = field(default=None)

    @_times.validator
    def validate_times(self, attributes, values):
        """Validate array of times."""
        if len(values) <= 1:
            raise ValueError("array of time values must be of length >= 2")

        if not isinstance(self._times, np.ndarray):
            raise TypeError("times must be a numpy ndarray")

        if self._times.dtype not in [np.float64, np.float32]:
            raise TypeError("times must be float or date dtype")

        zero_point = dt.timedelta(0) if isinstance(values[0], dt.date) else 0
        for i in range(len(values) - 1):
            if values[i + 1] - values[i] < zero_point:
                raise ValueError("array of time values is not sorted")

    def __attrs_post_init__(self):
        if len(self._discount_factors) != len(self._times):
            raise ValueError(
                "length of _discount_factors array must equal length of _times array"
            )

        if not isinstance(self._discount_factors, np.ndarray):
            raise ValueError("_discount_factors must be of type float array")

        if self._discount_factors.dtype not in [np.float64, np.float32]:
            raise TypeError("_discount factors must be of type float")

        # Get the interpolator class based on the interpolation type
        interpolator_class: Interpolator = interpolator_map.get(
            self._interpolation_type
        )

        if interpolator_class is None:
            raise ValueError(f"Invalid interpolator type: {self._interpolation_type}")

        # Initialize the interpolator
        self._interpolator = interpolator_class(
            x_values=self._times, y_values=self._discount_factors, extrapolate=True
        )

    def df(self, t: float, T: float) -> float:
        """Returns the discount factor P(t,T)"""
        disc_fact_t = self._interpolator(t)  # df(0,t) = e^{-rt}
        disc_fact_T = self._interpolator(T)  # df(0,T) = e^{-rT}

        disc_fact = disc_fact_T / disc_fact_t  # df(t,T) = e^{-r(T-t)}

        return disc_fact

    @staticmethod
    def rate_curve(
        trade_ccy: Currency,
        collateral_ccy: Currency,
        times: np.ndarray[Union[dt.date, float]],
        rates: np.ndarray[float],
        anchor_date: Optional[dt.date],
    ):
        """Creates a discounting curve given an array of times
        and annually compounded spot interest rates, assuming Act/365 basis

        Args:
            trade_ccy (Currency): The trade currency.
            collateral_ccy (Currency): The collateral currency.
            times (np.ndarray[Union[dt.date, float]]): An array of dates/times.
            rates (np.ndarray[float]): An array of spot interest rates
            anchor_date (Optional[dt.date]): The anchor date (time 0)
        """
        if isinstance(times, np.ndarray[dt.date]):
            times = (times - anchor_date).days() / 365.0

        dfs = 1 / ((1.0 + rates) ** times)
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

    @staticmethod
    def flat(trade_ccy: Currency, collateral_ccy: Currency, rate: float):
        """Creates a flat rate curve

        Args:
            trade_ccy (Currency): The trade currency.
            collateral_ccy (Currency): The collateral currency.
            rate (float): The flat annual compounded spot interest rate
        """
        times = np.array(np.linspace(start=0.0, stop=50.0, num=51, endpoint=True))
        dfs = 1 / np.power(1.0 + rate, times)
        return DiscountingCurve(
            id=DiscountingCurveId(
                friendly_name=MarketObjects.DISCOUNTING_CURVE,
                currency=trade_ccy,
                collateral=collateral_ccy,
            ),
            times=times,
            discount_factors=dfs,
        )
