from calculators.units import (
    convert_current,
    convert_voltage,
    convert_resistance
)


def test_convert_current_ma():
    assert convert_current(20, "mA") == 0.02


def test_convert_current_ua():
    assert convert_current(500, "uA") == 0.0005


def test_convert_voltage_mv():
    assert convert_voltage(500, "mV") == 0.5


def test_convert_voltage_kv():
    assert convert_voltage(2, "kV") == 2000


def test_convert_resistance_kohm():
    assert convert_resistance(4.7, "k") == 4700


def test_convert_resistance_mohm():
    assert convert_resistance(2.2, "M") == 2200000

def test_current_unit_aliases():
    assert convert_current(20, "ma") == 0.02
    assert convert_current(20, "a") == 20


def test_voltage_unit_aliases():
    assert convert_voltage(500, "mv") == 0.5
    assert convert_voltage(2, "kv") == 2000


def test_resistance_unit_aliases():
    assert convert_resistance(4.7, "kΩ") == 4700
    assert convert_resistance(4.7, "kohm") == 4700
    assert convert_resistance(2.2, "Mohm") == 2200000


import pytest


def test_invalid_current_unit():
    with pytest.raises(ValueError):
        convert_current(20, "banana")


def test_invalid_voltage_unit():
    with pytest.raises(ValueError):
        convert_voltage(5, "banana")


def test_invalid_resistance_unit():
    with pytest.raises(ValueError):
        convert_resistance(100, "banana")