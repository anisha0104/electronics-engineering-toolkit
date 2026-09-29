from calculators.opamp import calculate_inverting_gain


def test_inverting_gain():
    assert calculate_inverting_gain(10000, 2000) == -5


def test_inverting_gain_equal_resistors():
    assert calculate_inverting_gain(1000, 1000) == -1


def test_feedback_resistance_cannot_be_zero():
    try:
        calculate_inverting_gain(0, 1000)
        assert False
    except ValueError:
        assert True


def test_input_resistance_cannot_be_zero():
    try:
        calculate_inverting_gain(10000, 0)
        assert False
    except ValueError:
        assert True