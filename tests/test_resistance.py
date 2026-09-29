from calculators.resistance import (
    calculate_series_resistance,
    calculate_parallel_resistance
)


def test_series_resistance():
    assert calculate_series_resistance([100, 220, 330]) == 650


def test_series_resistance_two_resistors():
    assert calculate_series_resistance([100, 200]) == 300


def test_series_resistance_single_resistor():
    assert calculate_series_resistance([470]) == 470

def test_series_resistance_with_decimals():
    assert calculate_series_resistance([4.7, 10.3, 15.0]) == 30.0

def test_parallel_resistance():
    assert calculate_parallel_resistance([100, 100]) == 50


def test_parallel_resistance_different_values():
    assert calculate_parallel_resistance([100, 200]) == 66.66666666666667

import pytest


def test_parallel_resistance_zero():
    with pytest.raises(ValueError):
        calculate_parallel_resistance([100, 0])