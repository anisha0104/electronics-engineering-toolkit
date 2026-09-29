import math


def calculate_cutoff_frequency(resistance, capacitance):
    if resistance <= 0:
        raise ValueError("Resistance must be greater than zero.")

    if capacitance <= 0:
        raise ValueError("Capacitance must be greater than zero.")

    return 1 / (2 * math.pi * resistance * capacitance)