from calculators.ohms_law import (
    calculate_voltage,
    calculate_current,
    calculate_resistance
)

from calculators.units import (
    convert_current,
    convert_voltage,
    convert_resistance
)

from calculators.input_handler import get_value_with_unit


print("Electronics Engineering Toolkit")
print("==============================")
print("Ohm's Law Calculator")
print()

print("What do you want to calculate?")
print("1. Voltage")
print("2. Current")
print("3. Resistance")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    try:
        current, current_unit = get_value_with_unit("Enter current: ")
        resistance, resistance_unit = get_value_with_unit("Enter resistance: ")

        current = convert_current(current, current_unit)
        resistance = convert_resistance(resistance, resistance_unit)

        voltage = calculate_voltage(current, resistance)

        print(f"Voltage: {voltage} V")

    except ValueError as error:
        print(f"Invalid input: {error}")

elif choice == "2":
    try:
        voltage, voltage_unit = get_value_with_unit("Enter voltage: ")
        resistance, resistance_unit = get_value_with_unit("Enter resistance: ")

        voltage = convert_voltage(voltage, voltage_unit)
        resistance = convert_resistance(resistance, resistance_unit)

        current = calculate_current(voltage, resistance)

        print(f"Current: {current} A")

    except ValueError as error:
        print(f"Invalid input: {error}")


elif choice == "3":
    try:
        voltage, voltage_unit = get_value_with_unit("Enter voltage: ")
        current, current_unit = get_value_with_unit("Enter current: ")

        voltage = convert_voltage(voltage, voltage_unit)
        current = convert_current(current, current_unit)

        if current == 0:
            print("Invalid input: Current cannot be zero.")
        else:
            resistance = calculate_resistance(voltage, current)

            print(f"Resistance: {resistance} ohms")

    except ValueError as error:
        print(f"Invalid input: {error}")

else:
    print("Invalid choice.")