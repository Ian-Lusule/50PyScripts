```python
"""
simple_calculator.py

A simple calculator that performs basic arithmetic operations.
"""

def add(x, y):
    """Adds two numbers together.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """Subtracts two numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The difference between x and y.
    """
    return x - y

def multiply(x, y):
    """Multiplies two numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The product of x and y.
    """
    return x * y

def divide(x, y):
    """Divides two numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The quotient of x and y.
        Raises a ZeroDivisionError if y is 0.
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def main():
    """Main function to run the calculator."""
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice = int(input("Enter choice(1/2/3/4/5): "))

            if choice in (1, 2, 3, 4):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == 1:
                    print(num1, "+", num2, "=", add(num1, num2))
                elif choice == 2:
                    print(num1, "-", num2, "=", subtract(num1, num2))
                elif choice == 3:
                    print(num1, "*", num2, "=", multiply(num1, num2))
                elif choice == 4:
                    print(num1, "/", num2, "=", divide(num1, num2))

            elif choice == 5:
                break

            else:
                print("Invalid input")

        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

```