```python
"""
Factorial Calculator

This script calculates the factorial of a non-negative integer.
"""

import argparse
import math

def calculate_factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n: The non-negative integer.

    Returns:
        The factorial of n.  Returns an error message if n is negative or not an integer.
    """
    if not isinstance(n, int):
        return "Error: Input must be an integer."
    if n < 0:
        return "Error: Input must be a non-negative integer."
    elif n == 0:
        return 1
    else:
        return math.factorial(n)


def main():
    """
    Parses command-line arguments and calculates the factorial.
    """
    parser = argparse.ArgumentParser(description="Calculate the factorial of a number.")
    parser.add_argument("number", type=int, help="The non-negative integer to calculate the factorial of.")
    args = parser.parse_args()

    result = calculate_factorial(args.number)
    print(f"The factorial of {args.number} is: {result}")


if __name__ == "__main__":
    main()

```