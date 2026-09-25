from calculators.ohms_law import (
    calculate_voltage,
    calculate_current,
    calculate_resistance
)
from calculators.input_handler import get_number, get_nonzero_number

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
    current = get_number("Enter current (A): ")
    resistance = get_number("Enter resistance (ohms): ")

    voltage = calculate_voltage(current, resistance)

    print(f"Voltage: {voltage} V")

elif choice == "2":
    voltage = get_number("Enter voltage (V): ")
    resistance = get_nonzero_number("Enter resistance (ohms): ")

    current = calculate_current(voltage, resistance)

    print(f"Current: {current} A")

elif choice == "3":
    voltage = get_number("Enter voltage (V): ")
    current = get_nonzero_number("Enter current (A): ")

    resistance = calculate_resistance(voltage, current)

    print(f"Resistance: {resistance} ohms")

else:
    print("Invalid choice.")