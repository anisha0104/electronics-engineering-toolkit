from calculators.resistance import calculate_series_resistance


def test_series_resistance():
    assert calculate_series_resistance([100, 220, 330]) == 650


def test_series_resistance_two_resistors():
    assert calculate_series_resistance([100, 200]) == 300


def test_series_resistance_single_resistor():
    assert calculate_series_resistance([470]) == 470

def test_series_resistance_with_decimals():
    assert calculate_series_resistance([4.7, 10.3, 15.0]) == 30.0