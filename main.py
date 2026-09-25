from calculators.ohms_law import (
    calculate_voltage,
    calculate_current,
    calculate_resistance
)

print("Electronics Engineering Toolkit")
print("==============================")
print("Ohm's Law Calculator")
print()

voltage = float(input("Enter voltage (V): "))
current = float(input("Enter current (A): "))

resistance = calculate_resistance(voltage, current)

print()
print(f"Resistance: {resistance} ohms")