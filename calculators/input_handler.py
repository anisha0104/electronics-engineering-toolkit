def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_nonzero_number(prompt):
    while True:
        value = get_number(prompt)

        if value != 0:
            return value

        print("Invalid input. Value cannot be zero.")

def get_value_with_unit(prompt):
    while True:
        try:
            user_input = input(prompt).strip()

            parts = user_input.split()

            if len(parts) == 2:
                value = float(parts[0])
                unit = parts[1]
                return value, unit

            if len(parts) == 1:
                text = parts[0]

                index = 0

                while index < len(text) and (
                    text[index].isdigit() or text[index] in ".-"
                ):
                    index += 1

                if index == 0 or index == len(text):
                    raise ValueError

                value = float(text[:index])
                unit = text[index:]

                return value, unit

            print("Invalid input. Example: 20 mA or 20mA.")

        except ValueError:
            print("Invalid input. Example: 20 mA or 20mA.")