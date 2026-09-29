from calculators.led import calculate_led_resistor


def test_led_resistor():
    assert calculate_led_resistor(5, 2, 0.02) == 150


def test_led_resistor_different_values():
    assert calculate_led_resistor(9, 2, 0.02) == 350


def test_led_current_cannot_be_zero():
    try:
        calculate_led_resistor(5, 2, 0)
        assert False
    except ValueError:
        assert True


def test_supply_voltage_must_be_greater():
    try:
        calculate_led_resistor(2, 2, 0.02)
        assert False
    except ValueError:
        assert True