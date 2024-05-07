# install units with pip
from tabulate import tabulate
import sys


def main():
    try:
        table = [[1, "Length"], [2, "Weight"], [3, "Temperature"]]
        a = int(
            input(
                f"Choose a system of unit \n{tabulate(table, headers=['Choose','Unit'], tablefmt='fancy_outline',)}\n: "
            )
        )
        if a == 1:  # length
            length_table = [
                [1, "Metre"],
                [2, "Kilometre"],
                [3, "Centimetre"],
                [4, "Millimetre"],
                [5, "Mile"],
                [6, "Yard"],
                [7, "Foot"],
                [8, "Inch"],
            ]
            from_length = int(
                input(
                    f"What unit length would you like to convert from? \n{tabulate(length_table, headers=['Choose','Unit'], tablefmt='rounded_grid',)}\n: "
                )
            )
            to_length = int(
                input(
                    f"What unit length would you like to convert to? \n{tabulate(length_table, headers=['Choose','Unit'], tablefmt='pretty',)}\n: "
                )
            )
            length = float(input("Enter a length: "))
            if length < 0:
                sys.exit("Invalid Input: length cannot be negative")
            print(length_conv(from_length, to_length, length))

        elif a == 2:  # weight
            weight_table = [[1, "Kilogram"], [2, "Gram"], [3, "Pound"], [4, "Ounce"]]
            from_weight = int(
                input(
                    f"What unit weight would you like to convert from? \n{tabulate(weight_table, headers=['Choose','Unit'], tablefmt='rounded_grid')}\n: "
                )
            )
            to_weight = int(
                input(
                    f"What unit weight would you like to convert to? \n{tabulate(weight_table, headers=['Choose','Unit'], tablefmt='pretty')}\n: "
                )
            )
            weight = float(input("Enter a weight: "))
            if weight < 0:
                sys.exit("Invalid Input: weight cannot be negative")
            print(weight_conv(from_weight, to_weight, weight))

        elif a == 3:  # temperature
            temperature_table = [[1, "Celsius"], [2, "Fahrenheit"]]
            unit = int(
                input(
                    f"Enter '1' to convert from Celsius to Fahrenheit, or '2' to convert from Fahrenheit to Celsius \n{tabulate(temperature_table, headers=['Choose','Unit'], tablefmt='rounded_grid')}\n: "
                )
            )
            temp = float(input("Enter a temperature: "))
            print(temperature_conv(unit, temp))
        else:
            return f"Invalid Input: Not a valid input"
    except ValueError:
        sys.exit("Invalid Input: Not a number")


# Converting lengths
def length_conv(from_length, to_length, length):
    try:
        # From Metre
        if from_length == 1 and to_length == 2:
            return f"{length} metres is equal to {length * 0.001:.2f} kilometres"
        elif from_length == 1 and to_length == 3:
            return f"{length} metres is equal to {length * 100:.2f} centimetres"
        elif from_length == 1 and to_length == 4:
            return f"{length} metres is equal to {length * 1000:.2f} millimetres"
        elif from_length == 1 and to_length == 5:
            return f"{length} metres is equal to {length * 0.0006213689:.2f} miles"
        elif from_length == 1 and to_length == 6:
            return f"{length} metres is equal to {length * 1.0936132983:.2f} yards"
        elif from_length == 1 and to_length == 7:
            return f"{length} metres is equal to {length * 3.280839895:.2f} feet"
        elif from_length == 1 and to_length == 8:
            return f"{length} metres is equal to {length * 39.37007874:.2f} inches"

        # From Kilometres
        elif from_length == 2 and to_length == 1:
            return f"{length} kilometres is equal to {length * 1000:.2f} metres"
        elif from_length == 2 and to_length == 3:
            return f"{length} kilometres is equal to {length * 100000:.2f} centimetres"
        elif from_length == 2 and to_length == 4:
            return f"{length} kilometres is equal to {length * 1000000:.2f} millimetres"
        elif from_length == 2 and to_length == 5:
            return f"{length} kilometres is equal to {length * 0.6213688756:.2f} miles"
        elif from_length == 2 and to_length == 6:
            return f"{length} kilometres is equal to {length * 1093.6132983:.2f} yards"
        elif from_length == 2 and to_length == 7:
            return f"{length} kilometres is equal to {length * 3280.839895:.2f} feet"
        elif from_length == 2 and to_length == 8:
            return f"{length} kilometres is equal to {length * 39370.07874:.2f} inches"

        # From Centimetres
        elif from_length == 3 and to_length == 1:
            return f"{length} centimetres is equal to {length * 0.01:.2f} metres"
        elif from_length == 3 and to_length == 2:
            return f"{length} centimetres is equal to {length * 0.00001:.2f} kilometres"
        elif from_length == 3 and to_length == 4:
            return f"{length} centimetres is equal to {length * 10:.2f} millimetres"
        elif from_length == 3 and to_length == 5:
            return f"{length} centimetres is equal to {length * 0.0000062137:.2f} miles"
        elif from_length == 3 and to_length == 6:
            return f"{length} centimetres is equal to {length * 0.010936133:.2f} yards"
        elif from_length == 3 and to_length == 7:
            return f"{length} centimetres is equal to {length * 0.032808399:.2f} feet"
        elif from_length == 3 and to_length == 8:
            return (
                f"{length} centimetres is equal to {length * 0.3937007874:.2f} inches"
            )

        # From Millimetres
        elif from_length == 4 and to_length == 1:
            return f"{length} millimetres is equal to {length * 0.001:.2f} metres"
        elif from_length == 4 and to_length == 2:
            return (
                f"{length} millimetres is equal to {length * 0.000001:.2f} kilometres"
            )
        elif from_length == 4 and to_length == 3:
            return f"{length} millimetres is equal to {length * 0.1:.2f} centimetres"
        elif from_length == 4 and to_length == 5:
            return (
                f"{length} millimetres is equal to {length * 6.213688756E-7:.2f} miles"
            )
        elif from_length == 4 and to_length == 6:
            return f"{length} millimetres is equal to {length * 0.0010936133:.2f} yards"
        elif from_length == 4 and to_length == 7:
            return f"{length} millimetres is equal to {length * 0.0032808399:.2f} feet"
        elif from_length == 4 and to_length == 8:
            return (
                f"{length} millimetres is equal to {length * 0.0393700787:.2f} inches"
            )

        # From Miles
        elif from_length == 5 and to_length == 1:
            return f"{length} miles is equal to {length * 1609.35:.2f} metres"
        elif from_length == 5 and to_length == 2:
            return f"{length} miles is equal to {length * 1.60935:.2f} kilometres"
        elif from_length == 5 and to_length == 3:
            return f"{length} miles is equal to {length * 160935:.2f} centimetres"
        elif from_length == 5 and to_length == 4:
            return f"{length} miles is equal to {length * 1609350:.2f} millimetres"
        elif from_length == 5 and to_length == 6:
            return f"{length} miles is equal to {length * 1760.0065617:.2f} yards"
        elif from_length == 5 and to_length == 7:
            return f"{length} miles is equal to {length * 5280.019685:.2f} feet"
        elif from_length == 5 and to_length == 8:
            return f"{length} miles is equal to {length * 63360.23622:.2f} inches"

        # From Yards
        elif from_length == 6 and to_length == 1:
            return f"{length} yards is equal to {length * 0.9144:.2f} metres"
        elif from_length == 6 and to_length == 2:
            return f"{length} yards is equal to {length * 0.0009144:.2f} kilometres"
        elif from_length == 6 and to_length == 3:
            return f"{length} yards is equal to {length * 91.44:.2f} centimetres"
        elif from_length == 6 and to_length == 4:
            return f"{length} yards is equal to {length * 914.4:.2f} millimetres"
        elif from_length == 6 and to_length == 5:
            return f"{length} yards is equal to {length * 0.0005681797:.2f} miles"
        elif from_length == 6 and to_length == 7:
            return f"{length} yards is equal to {length * 3:.2f} feet"
        elif from_length == 6 and to_length == 8:
            return f"{length} yards is equal to {length * 36:.2f} inches"

        # From Feet
        elif from_length == 7 and to_length == 1:
            return f"{length} feet is equal to {length * 0.3048:.2f} metres"
        elif from_length == 7 and to_length == 2:
            return f"{length} feet is equal to {length * 0.0003048:.2f} kilometres"
        elif from_length == 7 and to_length == 3:
            return f"{length} feet is equal to {length * 30.48:.2f} centimetres"
        elif from_length == 7 and to_length == 4:
            return f"{length} feet is equal to {length * 304.8:.2f} millimetres"
        elif from_length == 7 and to_length == 5:
            return f"{length} feet is equal to {length * 0.0001893932:.2f} miles"
        elif from_length == 7 and to_length == 6:
            return f"{length} feet is equal to {length * 0.3333333333:.2f} yards"
        elif from_length == 7 and to_length == 8:
            return f"{length} feet is equal to {length * 12:.2f} inches"

        # From Inches
        elif from_length == 8 and to_length == 1:
            return f"{length} inches is equal to {length * 0.0254:.2f} metres"
        elif from_length == 8 and to_length == 2:
            return f"{length} inches is equal to {length * 0.0000254:.2f} kilometres"
        elif from_length == 8 and to_length == 3:
            return f"{length} inches is equal to {length * 2.54:.2f} centiimetres"
        elif from_length == 8 and to_length == 4:
            return f"{length} inches is equal to {length * 25.4:.2f} millimetres"
        elif from_length == 8 and to_length == 5:
            return f"{length} inches is equal to {length * 0.0000157828:.2f} miles"
        elif from_length == 8 and to_length == 6:
            return f"{length} inches is equal to {length * 0.0277777778:.2f} yards"
        elif from_length == 8 and to_length == 7:
            return f"{length} inches is equal to {length * 0.0833333333:.2f} feet"

        # From equals to to
        elif from_length == to_length:
            return f"Invalid Input: Cannot convert same units"

        else:
            return f"Invalid Input: Not a valid input"

    except ValueError:
        sys.exit("Invalid Input: Not a number")


# Converting Weights
def weight_conv(from_weight, to_weight, weight):
    try:
        # From kilograms
        if from_weight == 1 and to_weight == 2:
            return f"{weight} kilograms is equal to {weight * 1000:.2f} grams"
        elif from_weight == 1 and to_weight == 3:
            return f"{weight} kilograms is equal to {weight * 2.2046244202:.2f} pounds"
        elif from_weight == 1 and to_weight == 4:
            return f"{weight} kilograms is equal to {weight * 35.273990723:.2f} ounces"

        # From grams
        elif from_weight == 2 and to_weight == 1:
            return f"{weight} grams is equal to {weight/1000:.2f} kilograms"
        elif from_weight == 2 and to_weight == 3:
            return f"{weight} grams is equal to {weight * 0.0022046244:.2f} pounds"
        elif from_weight == 2 and to_weight == 4:
            return f"{weight} grams is equal to {weight * 0.0352739907:.2f} ounces"

        # From pounds
        elif from_weight == 3 and to_weight == 1:
            return f"{weight} pounds is equal to {weight * 0.453592:.2f} kilograms"
        elif from_weight == 3 and to_weight == 2:
            return f"{weight} pounds is equal to {weight * 453.592:.2f} grams"
        elif from_weight == 3 and to_weight == 4:
            return f"{weight} pounds is equal to {weight * 16:.2f} ounces"

        # From Ounces
        elif from_weight == 4 and to_weight == 1:
            return f"{weight} ounces is equal to {weight * 0.0283495:.2f} kilograms"
        elif from_weight == 4 and to_weight == 2:
            return f"{weight} ounces is equal to {weight * 28.3495:.2f} grams"
        elif from_weight == 4 and to_weight == 4:
            return f"{weight} ounces is equal to {weight * 0.0625:.2f} pounds"

        # From equals to to
        elif from_weight == to_weight:
            return f"Invalid Input: Cannot convert same units"

        else:
            return f"Invalid Input: Not a valid input"
    except ValueError:
        sys.exit("Invalid Input: Not a number")


# Converting temperature
def temperature_conv(unit, temp):
    try:
        if unit == 1:
            # fahrenheit = (temp * 9/5) + 32
            return f"{temp} degrees Celsius is equal to {(temp * 9/5) + 32:.2f} degrees Fahrenheit."
        elif unit == 2:
            # celsius = (temp - 32) * 5/9
            return f"{temp} degrees Fahrenheit is equal to {(temp - 32) * 5/9:.2f} degrees Celsius."
        else:
            return f"Invalid choice. Please enter 1 or 2."
    except ValueError:
        sys.exit("Invalid Input: Not a number")


if __name__ == "__main__":
    main()
