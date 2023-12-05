def calculate_fuel(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        percentage = (x / y) * 100

        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return f'{round(percentage)}%'

    except ValueError:
        return "Please enter the fraction in the format X/Y, where X and Y are integers."
    except ZeroDivisionError:
        return "Cannot divide by zero. Please provide a valid denominator."

def main():
    while True:
        fraction = input("Enter the fraction (X/Y): ")
        result = calculate_fuel(fraction)
        print(result)
        if result in ['E', 'F']:
            break

if __name__ == "__main__":
    main()

