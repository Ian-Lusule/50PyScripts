```python
"""
temperature_converter.py

This script converts temperatures between Celsius, Fahrenheit, and Kelvin.
"""

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit.

    Args:
        celsius: The temperature in Celsius.

    Returns:
        The temperature in Fahrenheit.  Returns None if input is invalid.
    """
    try:
        celsius = float(celsius)
        return (celsius * 9/5) + 32
    except ValueError:
        print("Invalid input. Please enter a numeric value for Celsius.")
        return None

def celsius_to_kelvin(celsius):
    """Converts Celsius to Kelvin.

    Args:
        celsius: The temperature in Celsius.

    Returns:
        The temperature in Kelvin. Returns None if input is invalid.
    """
    try:
        celsius = float(celsius)
        return celsius + 273.15
    except ValueError:
        print("Invalid input. Please enter a numeric value for Celsius.")
        return None

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius.

    Args:
        fahrenheit: The temperature in Fahrenheit.

    Returns:
        The temperature in Celsius. Returns None if input is invalid.
    """
    try:
        fahrenheit = float(fahrenheit)
        return (fahrenheit - 32) * 5/9
    except ValueError:
        print("Invalid input. Please enter a numeric value for Fahrenheit.")
        return None

def fahrenheit_to_kelvin(fahrenheit):
    """Converts Fahrenheit to Kelvin.

    Args:
        fahrenheit: The temperature in Fahrenheit.

    Returns:
        The temperature in Kelvin. Returns None if input is invalid.
    """
    celsius = fahrenheit_to_celsius(fahrenheit)
    if celsius is not None:
        return celsius_to_kelvin(celsius)
    else:
        return None

def kelvin_to_celsius(kelvin):
    """Converts Kelvin to Celsius.

    Args:
        kelvin: The temperature in Kelvin.

    Returns:
        The temperature in Celsius. Returns None if input is invalid.
    """
    try:
        kelvin = float(kelvin)
        return kelvin - 273.15
    except ValueError:
        print("Invalid input. Please enter a numeric value for Kelvin.")
        return None

def kelvin_to_fahrenheit(kelvin):
    """Converts Kelvin to Fahrenheit.

    Args:
        kelvin: The temperature in Kelvin.

    Returns:
        The temperature in Fahrenheit. Returns None if input is invalid.
    """
    celsius = kelvin_to_celsius(kelvin)
    if celsius is not None:
        return celsius_to_fahrenheit(celsius)
    else:
        return None


def main():
    """Main function to handle user interaction."""
    print("Temperature Converter")
    while True:
        print("\nSelect conversion:")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '7':
            break

        try:
            temp = float(input("Enter temperature: "))
        except ValueError:
            print("Invalid temperature input. Please enter a number.")
            continue

        if choice == '1':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {result}°F")
        elif choice == '2':
            result = celsius_to_kelvin(temp)
            print(f"{temp}°C is equal to {result}K")
        elif choice == '3':
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F is equal to {result}°C")
        elif choice == '4':
            result = fahrenheit_to_kelvin(temp)
            print(f"{temp}°F is equal to {result}K")
        elif choice == '5':
            result = kelvin_to_celsius(temp)
            print(f"{temp}K is equal to {result}°C")
        elif choice == '6':
            result = kelvin_to_fahrenheit(temp)
            print(f"{temp}K is equal to {result}°F")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

```