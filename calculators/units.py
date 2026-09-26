def normalize_unit(unit):
    unit = unit.strip()

    unit_aliases = {
        "A": "A",
        "a": "A",
        "mA": "mA",
        "ma": "mA",
        "uA": "uA",
        "ua": "uA",

        "V": "V",
        "v": "V",
        "mV": "mV",
        "mv": "mV",
        "kV": "kV",
        "kv": "kV",

        "ohm": "ohm",
        "ohms": "ohm",
        "Ω": "ohm",
        "k": "k",
        "kΩ": "k",
        "kohm": "k",
        "kohms": "k",
        "M": "M",
        "MΩ": "M",
        "Mohm": "M",
        "Mohms": "M"
    }

    if unit in unit_aliases:
        return unit_aliases[unit]

    raise ValueError("Unsupported unit")

def convert_current(value, unit):
    unit = normalize_unit(unit)
    if unit == "A":
        return value

    elif unit == "mA":
        return value / 1000

    elif unit == "uA":
        return value / 1000000

    else:
        raise ValueError("Unsupported current unit")


def convert_voltage(value, unit):
    unit = normalize_unit(unit)

    if unit == "V":
        return value

    elif unit == "mV":
        return value / 1000

    elif unit == "kV":
        return value * 1000

    else:
        raise ValueError("Unsupported voltage unit")


def convert_resistance(value, unit):
    unit = normalize_unit(unit)

    if unit == "ohm":
        return value

    elif unit == "k":
        return value * 1000

    elif unit == "M":
        return value * 1000000

    else:
        raise ValueError("Unsupported resistance unit")