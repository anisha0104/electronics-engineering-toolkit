def calculate_voltage_divider(voltage_in, resistance_1, resistance_2):
    if resistance_1 + resistance_2 == 0:
        raise ValueError("Sum of resistances cannot be zero.")

    return voltage_in * resistance_2 / (resistance_1 + resistance_2)