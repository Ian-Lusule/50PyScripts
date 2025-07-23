```python
# python-mini-projects/prime_number_checker.py

"""
This module provides a function to check if a given number is a prime number.

A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.  A natural number greater than 1 that is not prime is called a composite number.

This implementation handles edge cases such as numbers less than 2 and efficiently checks for primality.
"""

def is_prime(number):
    """
    Checks if a given number is a prime number.

    Args:
        number: An integer.

    Returns:
        True if the number is prime, False otherwise.  Raises TypeError if input is not an integer.
    """

    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")

    if number < 2:
        return False

    # Optimization: Check divisibility only up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    """
    Gets user input and prints whether the number is prime or not.  Handles potential errors gracefully.
    """
    while True:
        try:
            num_str = input("Enter a number to check if it's prime (or 'q' to quit): ")
            if num_str.lower() == 'q':
                break
            number = int(num_str)
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        except ValueError:
            print("Invalid input. Please enter an integer or 'q' to quit.")
        except TypeError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

```