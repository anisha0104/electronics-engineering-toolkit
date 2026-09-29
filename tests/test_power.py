from calculators.power import calculate_power


def test_calculate_power():
    assert calculate_power(12, 2) == 24


def test_calculate_power_with_fraction():
    assert calculate_power(5, 0.5) == 2.5


def test_calculate_power_zero_current():
    assert calculate_power(230, 0) == 0


def test_calculate_power_zero_voltage():
    assert calculate_power(0, 10) == 0