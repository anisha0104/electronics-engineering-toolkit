def calculate_led_resistor(supply_voltage, forward_voltage, led_current):
    if led_current <= 0:
        raise ValueError("LED current must be greater than zero.")

    if supply_voltage <= forward_voltage:
        raise ValueError("Supply voltage must be greater than forward voltage.")

    return (supply_voltage - forward_voltage) / led_current