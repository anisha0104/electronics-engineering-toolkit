import sys
import os

sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from flask import Flask, render_template, request, jsonify

from calculators.ohms_law import (
    calculate_voltage,
    calculate_current,
    calculate_resistance
)

from calculators.power import calculate_power

from calculators.resistance import (
    calculate_series_resistance,
    calculate_parallel_resistance
)

from calculators.voltage_divider import calculate_voltage_divider

from calculators.led import calculate_led_resistor

from calculators.rc_filter import calculate_cutoff_frequency

from calculators.opamp import calculate_inverting_gain

from calculators.units import (
    convert_resistance,
    convert_capacitance
)


app = Flask(__name__)


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# CALCULATOR API
# =========================================================

@app.route("/calculate", methods=["POST"])
def calculate():

    data = request.get_json()

    calculator = data.get("calculator")

    try:

        # -------------------------------------------------
        # OHM'S LAW
        # -------------------------------------------------

        if calculator == "ohms":

            voltage = data.get("voltage")
            current = data.get("current")
            resistance = data.get("resistance")

            if voltage is not None and current is not None:

                result = calculate_resistance(
                    float(voltage),
                    float(current)
                )

                return jsonify({
                    "result": f"Resistance = {result:.2f} Ω"
                })

            elif voltage is not None and resistance is not None:

                result = calculate_current(
                    float(voltage),
                    float(resistance)
                )

                return jsonify({
                    "result": f"Current = {result:.2f} A"
                })

            elif current is not None and resistance is not None:

                result = calculate_voltage(
                    float(current),
                    float(resistance)
                )

                return jsonify({
                    "result": f"Voltage = {result:.2f} V"
                })

            raise ValueError("Please enter any two values.")


        # -------------------------------------------------
        # POWER
        # -------------------------------------------------

        elif calculator == "power":

            voltage = float(data["voltage"])
            current = float(data["current"])

            result = calculate_power(
                voltage,
                current
            )

            return jsonify({
                "result": f"Power = {result:.2f} W"
            })


        # -------------------------------------------------
        # SERIES RESISTANCE
        # -------------------------------------------------

        elif calculator == "series":

            values = data.get("resistances", "")

            resistances = [
                float(value.strip())
                for value in values.split(",")
                if value.strip()
            ]

            if not resistances:
                raise ValueError(
                    "Enter at least two resistance values."
                )

            if len(resistances) < 2:
                raise ValueError(
                    "Enter at least two resistance values."
                )

            result = calculate_series_resistance(
                resistances
            )

            return jsonify({
                "result": f"Total Resistance = {result:.2f} Ω"
            })


        # -------------------------------------------------
        # PARALLEL RESISTANCE
        # -------------------------------------------------

        elif calculator == "parallel":

            values = data.get("resistances", "")

            resistances = [
                float(value.strip())
                for value in values.split(",")
                if value.strip()
            ]

            if len(resistances) < 2:
                raise ValueError(
                    "Enter at least two resistance values."
                )

            result = calculate_parallel_resistance(
                resistances
            )

            return jsonify({
                "result": f"Equivalent Resistance = {result:.2f} Ω"
            })


        # -------------------------------------------------
        # VOLTAGE DIVIDER
        # -------------------------------------------------

        elif calculator == "divider":

            voltage_in = float(data["voltage_in"])
            resistance_1 = float(data["resistance_1"])
            resistance_2 = float(data["resistance_2"])

            result = calculate_voltage_divider(
                voltage_in,
                resistance_1,
                resistance_2
            )

            return jsonify({
                "result": f"Output Voltage = {result:.2f} V"
            })


        # -------------------------------------------------
        # LED RESISTOR
        # -------------------------------------------------

        elif calculator == "led":

            supply_voltage = float(
                data["supply_voltage"]
            )

            forward_voltage = float(
                data["forward_voltage"]
            )

            led_current = float(
                data["led_current"]
            )

            result = calculate_led_resistor(
                supply_voltage,
                forward_voltage,
                led_current
            )

            return jsonify({
                "result": f"Required Resistor = {result:.2f} Ω"
            })


        # -------------------------------------------------
        # RC FILTER
        # -------------------------------------------------

        elif calculator == "rc":

            resistance = float(
                data["resistance"]
            )

            capacitance = float(
                data["capacitance"]
            )

            result = calculate_cutoff_frequency(
                resistance,
                capacitance
            )

            return jsonify({
                "result": f"Cutoff Frequency = {result:.2f} Hz"
            })


        # -------------------------------------------------
        # OP-AMP
        # -------------------------------------------------

        elif calculator == "opamp":

            feedback_resistance = float(
                data["feedback_resistance"]
            )

            input_resistance = float(
                data["input_resistance"]
            )

            result = calculate_inverting_gain(
                feedback_resistance,
                input_resistance
            )

            return jsonify({
                "result": f"Inverting Gain = {result:.2f}"
            })


        else:

            raise ValueError(
                "Unknown calculator."
            )


    except (ValueError, KeyError, TypeError) as error:

        return jsonify({
            "error": str(error)
        }), 400


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":
    app.run(debug=True)