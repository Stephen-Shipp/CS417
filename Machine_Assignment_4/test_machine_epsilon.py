"""
Test suite for machine_epsilon.py and plot_error.py

Tests cover:
  - Cleve Moler epsilon computation
  - sqrt(epsilon) computation
  - Data collection from finite difference
  - Minimum error finder
"""

import math

import pytest

from machine_epsilon import cleve_moler_epsilon, sqrt_epsilon
from plot_error import collect_data, find_minimum_error


# ──────────────────────────────────────────────
# TestCleveMolerEpsilon
# ──────────────────────────────────────────────
class TestCleveMolerEpsilon:
    def test_matches_ieee754_double(self):
        # IEEE 754 double precision epsilon is 2^-52
        expected = 2.0 ** -52
        assert cleve_moler_epsilon() == pytest.approx(expected, rel=1e-6)

    def test_is_positive(self):
        assert cleve_moler_epsilon() > 0.0

    def test_is_small(self):
        # Machine epsilon must be much smaller than 1
        assert cleve_moler_epsilon() < 1e-10

    def test_returns_float(self):
        assert isinstance(cleve_moler_epsilon(), float)

    def test_is_consistent(self):
        # Two calls should return the same value (deterministic)
        assert cleve_moler_epsilon() == cleve_moler_epsilon()


# ──────────────────────────────────────────────
# TestSqrtEpsilon
# ──────────────────────────────────────────────
class TestSqrtEpsilon:
    def test_known_value(self):
        eps = cleve_moler_epsilon()
        assert sqrt_epsilon(eps) == pytest.approx(math.sqrt(eps))

    def test_sqrt_of_one(self):
        assert sqrt_epsilon(1.0) == pytest.approx(1.0)

    def test_sqrt_of_four(self):
        assert sqrt_epsilon(4.0) == pytest.approx(2.0)

    def test_returns_float(self):
        assert isinstance(sqrt_epsilon(1.0), float)

    def test_larger_than_eps(self):
        eps = cleve_moler_epsilon()
        assert sqrt_epsilon(eps) > eps


# ──────────────────────────────────────────────
# TestCollectData
# ──────────────────────────────────────────────
class TestCollectData:
    def test_default_returns_30_points(self):
        h_values, errors = collect_data()
        assert len(h_values) == 30
        assert len(errors) == 30

    def test_custom_max_n(self):
        h_values, errors = collect_data(max_n=10)
        assert len(h_values) == 10
        assert len(errors) == 10

    def test_h_values_are_decreasing(self):
        h_values, _ = collect_data()
        for i in range(len(h_values) - 1):
            assert h_values[i] > h_values[i + 1]

    def test_first_h_is_half(self):
        h_values, _ = collect_data()
        assert h_values[0] == pytest.approx(0.5)

    def test_errors_are_positive(self):
        _, errors = collect_data()
        assert all(e >= 0.0 for e in errors)

    def test_large_h_has_large_error(self):
        h_values, errors = collect_data()
        # First row (h=0.5) should have the largest error
        assert errors[0] == pytest.approx(0.22825430, abs=1e-6)

    def test_error_initially_decreases(self):
        _, errors = collect_data()
        # Error should decrease for first several steps
        assert errors[0] > errors[1] > errors[2] > errors[3]


# ──────────────────────────────────────────────
# TestFindMinimumError
# ──────────────────────────────────────────────
class TestFindMinimumError:
    def test_returns_tuple(self):
        h_values, errors = collect_data()
        result = find_minimum_error(h_values, errors)
        assert len(result) == 2

    def test_minimum_error_is_smallest(self):
        h_values, errors = collect_data()
        _, err_min = find_minimum_error(h_values, errors)
        assert err_min == min(errors)

    def test_minimum_error_near_sqrt_eps(self):
        # The optimal h should be near sqrt(eps) ~ 1.49e-8
        h_values, errors = collect_data()
        h_min, _ = find_minimum_error(h_values, errors)
        sqrt_eps = sqrt_epsilon(cleve_moler_epsilon())
        # h_min should be within one order of magnitude of sqrt(eps)
        assert h_min == pytest.approx(sqrt_eps, rel=1.0)

    def test_trivial_case(self):
        h_vals = [0.5, 0.25, 0.125]
        errs = [0.3, 0.1, 0.2]
        h_min, err_min = find_minimum_error(h_vals, errs)
        assert err_min == pytest.approx(0.1)
        assert h_min == pytest.approx(0.25)