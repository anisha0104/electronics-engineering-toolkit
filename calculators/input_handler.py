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