import math

from calculators.rc_filter import calculate_cutoff_frequency


def test_cutoff_frequency():
    result = calculate_cutoff_frequency(1000, 0.000001)

    assert math.isclose(result, 159.154943, rel_tol=1e-6)


def test_cutoff_frequency_different_values():
    result = calculate_cutoff_frequency(10000, 0.0000001)

    assert math.isclose(result, 159.154943, rel_tol=1e-6)

    


def test_resistance_cannot_be_zero():
    try:
        calculate_cutoff_frequency(0, 0.000001)
        assert False
    except ValueError:
        assert True


def test_capacitance_cannot_be_zero():
    try:
        calculate_cutoff_frequency(1000, 0)
        assert False
    except ValueError:
        assert True