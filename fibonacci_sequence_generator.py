```python
# python-mini-projects/fibonacci_sequence_generator.py

"""
Generates a Fibonacci sequence up to a specified number of terms or a maximum value.

This script allows users to generate a Fibonacci sequence either by specifying the 
number of terms they want or by specifying a maximum value the sequence should not exceed.
It includes error handling to ensure the input is valid.
"""

def generate_fibonacci(num_terms=None, max_value=None):
    """
    Generates a Fibonacci sequence.

    Args:
        num_terms: The desired number of terms in the sequence (integer). If provided, max_value is ignored.
        max_value: The maximum value the sequence should reach (integer). If provided, num_terms is ignored.

    Returns:
        A list containing the Fibonacci sequence, or None if invalid input is provided.  
    """

    if (num_terms is None and max_value is None) or (num_terms is not None and max_value is not None):
        raise ValueError("Please provide either num_terms OR max_value, not both or neither.")

    if num_terms is not None:
        if not isinstance(num_terms, int) or num_terms <= 0:
            raise ValueError("num_terms must be a positive integer.")
        
        fib_sequence = []
        a, b = 0, 1
        for _ in range(num_terms):
            fib_sequence.append(a)
            a, b = b, a + b
        return fib_sequence

    elif max_value is not None:
        if not isinstance(max_value, int) or max_value <=0:
            raise ValueError("max_value must be a positive integer.")

        fib_sequence = []
        a, b = 0, 1
        while a <= max_value:
            fib_sequence.append(a)
            a, b = b, a + b
        return fib_sequence


if __name__ == "__main__":
    try:
        # Get user input.  Could be improved with argparse for more robust command-line handling.
        choice = input("Generate Fibonacci sequence by (n)umber of terms or (m)aximum value? (n/m): ").lower()

        if choice == 'n':
            num_terms = int(input("Enter the desired number of terms: "))
            sequence = generate_fibonacci(num_terms=num_terms)
        elif choice == 'm':
            max_value = int(input("Enter the maximum value: "))
            sequence = generate_fibonacci(max_value=max_value)
        else:
            raise ValueError("Invalid choice. Please enter 'n' or 'm'.")

        print("Fibonacci sequence:", sequence)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

```