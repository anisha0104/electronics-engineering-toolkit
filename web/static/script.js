/* =========================================================
   ELECTRONICS ENGINEERING TOOLKIT
   Calculator Interface
   ========================================================= */


let currentCalculator = null;


/* =========================================================
   CALCULATOR CONFIGURATION
   ========================================================= */

const calculators = {

    ohms: {

        title: "Ohm's Law",

        description:
            "Enter any two values to calculate the third.",

        fields: [

            {
                id: "voltage",
                label: "Voltage",
                unit: "V",
                placeholder: "e.g. 230"
            },

            {
                id: "current",
                label: "Current",
                unit: "A",
                placeholder: "e.g. 10"
            },

            {
                id: "resistance",
                label: "Resistance",
                unit: "Ω",
                placeholder: "e.g. 23"
            }

        ]

    },


    power: {

        title: "Power",

        description:
            "Calculate electrical power using voltage and current.",

        fields: [

            {
                id: "voltage",
                label: "Voltage",
                unit: "V",
                placeholder: "e.g. 230"
            },

            {
                id: "current",
                label: "Current",
                unit: "A",
                placeholder: "e.g. 2"
            }

        ]

    },


    series: {

        title: "Series Resistance",

        description:
            "Enter resistor values separated by commas.",

        fields: [

            {
                id: "resistances",
                label: "Resistances",
                unit: "Ω",
                placeholder: "e.g. 100, 220, 330"
            }

        ]

    },


    parallel: {

        title: "Parallel Resistance",

        description:
            "Enter resistor values separated by commas.",

        fields: [

            {
                id: "resistances",
                label: "Resistances",
                unit: "Ω",
                placeholder: "e.g. 100, 220, 330"
            }

        ]

    },


    divider: {

        title: "Voltage Divider",

        description:
            "Calculate the output voltage of a resistor divider.",

        fields: [

            {
                id: "voltage_in",
                label: "Input Voltage",
                unit: "V",
                placeholder: "e.g. 12"
            },

            {
                id: "resistance_1",
                label: "R₁",
                unit: "Ω",
                placeholder: "e.g. 1000"
            },

            {
                id: "resistance_2",
                label: "R₂",
                unit: "Ω",
                placeholder: "e.g. 2000"
            }

        ]

    },


    led: {

        title: "LED Resistor",

        description:
            "Calculate the resistor required to limit LED current.",

        fields: [

            {
                id: "supply_voltage",
                label: "Supply Voltage",
                unit: "V",
                placeholder: "e.g. 5"
            },

            {
                id: "forward_voltage",
                label: "LED Forward Voltage",
                unit: "V",
                placeholder: "e.g. 2"
            },

            {
                id: "led_current",
                label: "LED Current",
                unit: "A",
                placeholder: "e.g. 0.02"
            }

        ]

    },


    rc: {

        title: "RC Filter",

        description:
            "Calculate the cutoff frequency of an RC filter.",

        fields: [

            {
                id: "resistance",
                label: "Resistance",
                unit: "Ω",
                placeholder: "e.g. 1000"
            },

            {
                id: "capacitance",
                label: "Capacitance",
                unit: "F",
                placeholder: "e.g. 0.000001"
            }

        ]

    },


    opamp: {

        title: "Inverting Op-Amp Gain",

        description:
            "Calculate the gain of an inverting amplifier.",

        fields: [

            {
                id: "feedback_resistance",
                label: "Feedback Resistance (Rf)",
                unit: "Ω",
                placeholder: "e.g. 10000"
            },

            {
                id: "input_resistance",
                label: "Input Resistance (Rin)",
                unit: "Ω",
                placeholder: "e.g. 1000"
            }

        ]

    }

};


/* =========================================================
   OPEN CALCULATOR
   ========================================================= */

function openCalculator(type) {

    currentCalculator = type;

    const calculator =
        calculators[type];

    document.getElementById(
        "modal-title"
    ).textContent = calculator.title;


    document.getElementById(
        "modal-description"
    ).textContent = calculator.description;


    const inputContainer =
        document.getElementById(
            "calculator-inputs"
        );


    inputContainer.innerHTML = "";


    calculator.fields.forEach(field => {

        const group =
            document.createElement("div");

        group.className = "input-group";


        group.innerHTML = `

            <label for="${field.id}">

                ${field.label}

                <span>${field.unit}</span>

            </label>

            <input
                type="text"
                id="${field.id}"
                placeholder="${field.placeholder}"
                autocomplete="off"
            >

        `;


        inputContainer.appendChild(group);

    });


    document.getElementById(
        "calculator-result"
    ).textContent =
        "Enter your values to begin.";


    const panel =
        document.getElementById(
            "calculator-panel"
        );


    panel.classList.add("active");


    document.body.style.overflow = "hidden";

}


/* =========================================================
   CLOSE CALCULATOR
   ========================================================= */

function closeCalculator() {

    const panel =
        document.getElementById(
            "calculator-panel"
        );


    panel.classList.remove("active");


    document.body.style.overflow = "";

}


/* =========================================================
   PERFORM CALCULATION
   ========================================================= */

async function performCalculation() {

    const calculator =
        calculators[currentCalculator];


    const data = {

        calculator: currentCalculator

    };


    calculator.fields.forEach(field => {

        const input =
            document.getElementById(field.id);

        const value =
            input.value.trim();


        data[field.id] =
            value === ""
                ? null
                : value;

    });


    const result =
        document.getElementById(
            "calculator-result"
        );


    result.textContent =
        "Calculating...";


    try {

        const response =
            await fetch(
                "/calculate",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify(data)

                }
            );


        const resultData =
            await response.json();


        if (response.ok) {

            result.textContent =
                resultData.result;

            result.classList.add(
                "success-result"
            );

        } else {

            result.textContent =
                resultData.error;

            result.classList.remove(
                "success-result"
            );

        }


    } catch (error) {

        result.textContent =
            "Unable to connect to the calculator.";

        result.classList.remove(
            "success-result"
        );

    }

}


/* =========================================================
   ESC KEY CLOSE
   ========================================================= */

document.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Escape" &&
            currentCalculator
        ) {

            closeCalculator();

        }

    }
);