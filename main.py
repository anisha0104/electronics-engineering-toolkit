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
from calculators.formatting import print_result
from calculators.power import calculate_power
from calculators.resistance import (
    calculate_series_resistance,
    calculate_parallel_resistance
)
from calculators.voltage_divider import calculate_voltage_divider
from calculators.led import calculate_led_resistor
from calculators.rc_filter import calculate_cutoff_frequency
from calculators.opamp import calculate_inverting_gain

print("Electronics Engineering Toolkit")
print("==============================")
print("Ohm's Law Calculator")
print()

print("What do you want to calculate?")
print("1. Voltage")
print("2. Current")
print("3. Resistance")
print("4. Power")
print("5. Series Resistance")
print("6. Parallel Resistance")
print("7. Voltage Divider")
print("8. LED Resistor")
print("9. RC Filter")
print("10. Op-Amp Gain")


choice = input("Enter your choice (1-10): ")

if choice == "1":
    try:
        current, current_unit = get_value_with_unit("Enter current: ")
        resistance, resistance_unit = get_value_with_unit("Enter resistance: ")

        current = convert_current(current, current_unit)
        resistance = convert_resistance(resistance, resistance_unit)

        voltage = calculate_voltage(current, resistance)

        print_result("Voltage", voltage, "V")

    except ValueError as error:
        print(f"Invalid input: {error}")

elif choice == "2":
    try:
        voltage, voltage_unit = get_value_with_unit("Enter voltage: ")
        resistance, resistance_unit = get_value_with_unit("Enter resistance: ")

        voltage = convert_voltage(voltage, voltage_unit)
        resistance = convert_resistance(resistance, resistance_unit)

        current = calculate_current(voltage, resistance)

        print_result("Current", current, "A")

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

            print_result("Resistance", resistance, "ohms")

    except ValueError as error:
        print(f"Invalid input: {error}")

elif choice == "4":
    try:
        voltage, voltage_unit = get_value_with_unit("Enter voltage: ")
        current, current_unit = get_value_with_unit("Enter current: ")

        voltage = convert_voltage(voltage, voltage_unit)
        current = convert_current(current, current_unit)

        power = calculate_power(voltage, current)

        print_result("Power", power, "W")

    except ValueError as error:
        print(f"Invalid input: {error}")

elif choice == "5":
    try:
        number_of_resistors = int(input("How many resistors? "))

        if number_of_resistors <= 0:
            print("Invalid input: Number of resistors must be greater than zero.")
        else:
            resistances = []

            for i in range(number_of_resistors):
                resistance, resistance_unit = get_value_with_unit(
                    f"Enter resistance {i + 1}: "
                )

                resistance = convert_resistance(
                    resistance,
                    resistance_unit
                )

                resistances.append(resistance)

            total_resistance = calculate_series_resistance(resistances)

            print_result(
                "Series R",
                total_resistance,
                "ohms"
            )

    except ValueError as error:
        print(f"Invalid input: {error}")

elif choice == "6":
    try:
        number_of_resistors = int(input("How many resistors? "))

        if number_of_resistors <= 0:
            print("Invalid input: Number of resistors must be greater than zero.")
        else:
            resistances = []

            for i in range(number_of_resistors):
                resistance, resistance_unit = get_value_with_unit(
                    f"Enter resistance {i + 1}: "
                )

                resistance = convert_resistance(
                    resistance,
                    resistance_unit
                )

                resistances.append(resistance)

            total_resistance = calculate_parallel_resistance(resistances)

            print_result(
                "Parallel R",
                total_resistance,
                "ohms"
            )

    except ValueError as error:
        print(f"Invalid input: {error}")

elif choice == "7":
    try:
        voltage_value, voltage_unit = get_value_with_unit(
            "Enter input voltage: "
        )

        resistance_1_value, resistance_1_unit = get_value_with_unit(
            "Enter R1: "
        )

        resistance_2_value, resistance_2_unit = get_value_with_unit(
            "Enter R2: "
        )

        voltage_in = convert_voltage(voltage_value, voltage_unit)
        resistance_1 = convert_resistance(
            resistance_1_value, resistance_1_unit
        )
        resistance_2 = convert_resistance(
            resistance_2_value, resistance_2_unit
        )

        output_voltage = calculate_voltage_divider(
            voltage_in,
            resistance_1,
            resistance_2
        )

        print_result("Output V", output_voltage, "V")

    except ValueError as error:
        print(f"Invalid input: {error}")

elif choice == "8":
    try:
        supply_value, supply_unit = get_value_with_unit(
            "Enter supply voltage: "
        )

        forward_value, forward_unit = get_value_with_unit(
            "Enter LED forward voltage: "
        )

        current_value, current_unit = get_value_with_unit(
            "Enter LED current: "
        )

        supply_voltage = convert_voltage(supply_value, supply_unit)
        forward_voltage = convert_voltage(forward_value, forward_unit)
        led_current = convert_current(current_value, current_unit)

        resistance = calculate_led_resistor(
            supply_voltage,
            forward_voltage,
            led_current
        )

        print_result("LED R", resistance, "ohms")

    except ValueError as error:
        print(f"Invalid input: {error}")

elif choice == "9":
    try:
        resistance_value, resistance_unit = get_value_with_unit(
            "Enter resistance: "
        )

        capacitance_value, capacitance_unit = get_value_with_unit(
            "Enter capacitance: "
        )

        resistance = convert_resistance(
            resistance_value,
            resistance_unit
        )

        capacitance_unit = capacitance_unit.strip()

        capacitance_aliases = {
            "F": 1,
            "mF": 1e-3,
            "uF": 1e-6,
            "µF": 1e-6,
            "nF": 1e-9,
            "pF": 1e-12
        }

        if capacitance_unit not in capacitance_aliases:
            raise ValueError("Unsupported capacitance unit")

        capacitance = (
            capacitance_value * capacitance_aliases[capacitance_unit]
        )

        cutoff_frequency = calculate_cutoff_frequency(
            resistance,
            capacitance
        )

        print_result("Cutoff F", cutoff_frequency, "Hz")

    except ValueError as error:
        print(f"Invalid input: {error}")

elif choice == "10":
    try:
        feedback_value, feedback_unit = get_value_with_unit(
            "Enter feedback resistance (Rf): "
        )

        input_value, input_unit = get_value_with_unit(
            "Enter input resistance (Rin): "
        )

        feedback_resistance = convert_resistance(
            feedback_value,
            feedback_unit
        )

        input_resistance = convert_resistance(
            input_value,
            input_unit
        )

        gain = calculate_inverting_gain(
            feedback_resistance,
            input_resistance
        )

        print_result("Op-Amp Gain", gain, "")

    except ValueError as error:
        print(f"Invalid input: {error}")

else:
    print("Invalid choice.")