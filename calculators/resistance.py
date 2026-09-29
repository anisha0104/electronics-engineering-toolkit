def calculate_series_resistance(resistances):
    return sum(resistances)

def calculate_parallel_resistance(resistances):
    if any(resistance == 0 for resistance in resistances):
        raise ValueError("Resistance cannot be zero.")

    reciprocal_sum = sum(1 / resistance for resistance in resistances)
    return 1 / reciprocal_sum