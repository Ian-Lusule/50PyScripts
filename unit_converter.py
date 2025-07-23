```python
"""
Unit Converter: Converts between various units of measurement.

This script provides a command-line interface for converting between different units 
of length, weight, and temperature.  It handles invalid inputs and provides user-friendly 
messages.
"""

import sys

def convert_length(value, from_unit, to_unit):
    """Converts length measurements."""
    try:
        value = float(value)
    except ValueError:
        return "Invalid input: Value must be a number."

    conversions = {
        "mm": {"cm": 0.1, "m": 0.001, "km": 0.000001, "in": 0.0393701, "ft": 0.00328084, "yd": 0.00109361, "mi": 0.000000621371},
        "cm": {"mm": 10, "m": 0.01, "km": 0.00001, "in": 0.393701, "ft": 0.0328084, "yd": 0.0109361, "mi": 0.00000621371},
        "m": {"mm": 1000, "cm": 100, "km": 0.001, "in": 39.3701, "ft": 3.28084, "yd": 1.09361, "mi": 0.000621371},
        "km": {"mm": 1000000, "cm": 100000, "m": 1000, "in": 39370.1, "ft": 3280.84, "yd": 1093.61, "mi": 0.621371},
        "in": {"mm": 25.4, "cm": 2.54, "m": 0.0254, "km": 0.0000254, "ft": 0.0833333, "yd": 0.0277778, "mi": 0.0000157828},
        "ft": {"mm": 304.8, "cm": 30.48, "m": 0.3048, "km": 0.0003048, "in": 12, "yd": 0.333333, "mi": 0.000189394},
        "yd": {"mm": 914.4, "cm": 91.44, "m": 0.9144, "km": 0.0009144, "in": 36, "ft": 3, "mi": 0.000568182},
        "mi": {"mm": 1609340, "cm": 160934, "m": 1609.34, "km": 1.60934, "in": 63360, "ft": 5280, "yd": 1760}
    }

    if from_unit not in conversions or to_unit not in conversions[from_unit]:
        return "Invalid unit."

    converted_value = value * conversions[from_unit][to_unit]
    return converted_value


def convert_weight(value, from_unit, to_unit):
    """Converts weight measurements."""
    try:
        value = float(value)
    except ValueError:
        return "Invalid input: Value must be a number."

    conversions = {
        "g": {"kg": 0.001, "mg": 1000, "lb": 0.00220462, "oz": 0.035274},
        "kg": {"g": 1000, "mg": 1000000, "lb": 2.20462, "oz": 35.274},
        "mg": {"g": 0.001, "kg": 0.000001, "lb": 0.00000220462, "oz": 0.000035274},
        "lb": {"g": 453.592, "kg": 0.453592, "mg": 453592, "oz": 16},
        "oz": {"g": 28.3495, "kg": 0.0283495, "mg": 28349.5, "lb": 0.0625}
    }

    if from_unit not in conversions or to_unit not in conversions[from_unit]:
        return "Invalid unit."

    converted_value = value * conversions[from_unit][to_unit]
    return converted_value


def convert_temperature(value, from_unit, to_unit):
    """Converts temperature measurements."""
    try:
        value = float(value)
    except ValueError:
        return "Invalid input: Value must be a number."

    if from_unit == "celsius" and to_unit == "fahrenheit":
        converted_value = (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        converted_value = (value - 32) * 5/9
    elif from_unit == to_unit:
        converted_value = value
    else:
        return "Invalid temperature unit."
    return converted_value


def main():
    """Main function to handle user input and output."""
    if len(sys.argv) != 4:
        print("Usage: python unit_converter.py <value> <from_unit> <to_unit>")
        return

    value, from_unit, to_unit = sys.argv[1:]
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        print(f"{value} {from_unit} is equal to {value} {to_unit}")
        return

    if from_unit in ["mm", "cm", "m", "km", "in", "ft", "yd", "mi"]:
        result = convert_length(value, from_unit, to_unit)
    elif from_unit in ["g", "kg", "mg", "lb", "oz"]:
        result = convert_weight(value, from_unit, to_unit)
    elif from_unit in ["celsius", "fahrenheit"]:
        result = convert_temperature(value, from_unit, to_unit)
    else:
        print("Invalid unit type.")
        return

    if isinstance(result, str):  #Error message
        print(result)
    else:
        print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")


if __name__ == "__main__":
    main()

```