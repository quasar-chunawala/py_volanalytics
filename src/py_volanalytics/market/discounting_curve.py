"""Discounting Curve.

The ``DiscountingCurve`` object stores a vector of dates(times) and discount factors. We want to value all instruments consistently within a single valuation framework. For this we need a risk-free discounting curve. We establish a few important results:

**Risk-free asset**. Consider an asset with the price process :math:`M(t)` which has the dynamics:

.. math::

    dM(t) = r(t) M(t) dt

where :math:`M(t)` is any adapted process. Such an asset is said to be a risk-free asset.
"""

import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import scienceplots
import attrs
from attrs import define, field
from typing import Union

from py_volanalytics.math.interpolator import Interpolator, LinearInterpolator, CubicSplineInterpolator, HermiteCubicSplineInterpolator, InterpolationType, interpolator_map

plt.style.use('science')

@define(kw_only=True)
class DiscountingCurve:
    """ Class to represent a discounting curve object. """

    _times : np.ndarray[Union[dt.date, float]] = field()
    _discount_factors : np.ndarray[float] = field()
    _interpolation_type : InterpolationType = field(default=InterpolationType.LINEAR_INTERPOLATION, 
                                         validator=attrs.validators.instance_of(InterpolationType))

    @_times.validator
    def validate_times(self, attributes, values):
        """ Validate array of times. """
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
            raise ValueError("length of _discount_factors array must equal length of _times array")
        
        if not isinstance(self._discount_factors, np.ndarray[float]):\
            raise ValueError("_discount_factors must be of type float array")
        
        # Get the interpolator class based on the interpolation type
        interpolator_class = interpolator_map.get(self._interpolation_type)

        if interpolator_class is None:
            raise ValueError(f"Invalid interpolator type: {self._interpolation_type}")

        # Initialize the interpolator
        self._interpolator = interpolator_class(self._times, self._discount_factors)

    def zero(self, t : float, T: float) -> float:
        disc_fact_t = self._interpolator(t)
        disc_fact_T = self._interpolator(T)

        disc_fact = disc_fact_T / disc_fact_t

        return disc_fact
