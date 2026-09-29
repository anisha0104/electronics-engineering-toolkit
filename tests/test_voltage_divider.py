from calculators.voltage_divider import calculate_voltage_divider


def test_voltage_divider():
    assert calculate_voltage_divider(12, 1000, 1000) == 6


def test_voltage_divider_different_resistors():
    assert calculate_voltage_divider(10, 1000, 2000) == 6.666666666666667


def test_voltage_divider_zero_resistance_sum():
    try:
        calculate_voltage_divider(12, 100, -100)
        assert False
    except ValueError:
        assert True