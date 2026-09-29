def calculate_inverting_gain(feedback_resistance, input_resistance):
    if feedback_resistance <= 0:
        raise ValueError("Feedback resistance must be greater than zero.")

    if input_resistance <= 0:
        raise ValueError("Input resistance must be greater than zero.")

    return -feedback_resistance / input_resistance