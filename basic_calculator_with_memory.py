```python
"""
Basic Calculator with Memory

This program implements a simple calculator with memory functionality.  
Users can perform basic arithmetic operations (+, -, *, /) and store the result in memory.
"""

import operator

class Calculator:
    """Represents a calculator with memory."""

    def __init__(self):
        """Initializes the calculator with memory set to 0."""
        self.memory = 0

    def perform_operation(self, num1, num2, operator_func):
        """Performs an arithmetic operation.

        Args:
            num1: The first number.
            num2: The second number.
            operator_func: The operator function (e.g., operator.add, operator.sub).

        Returns:
            The result of the operation.  Returns None if an error occurs.
        """
        try:
            result = operator_func(num1, num2)
            return result
        except ZeroDivisionError:
            print("Error: Division by zero!")
            return None
        except TypeError:
            print("Error: Invalid input. Please enter numbers only.")
            return None

    def get_input(self, prompt):
        """Gets numerical input from the user with error handling."""
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Invalid input. Please enter a number.")

    def run(self):
        """Runs the calculator's main loop."""
        while True:
            print("\nSelect operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Memory Recall (M)")
            print("6. Memory Clear (MC)")
            print("7. Exit")

            choice = input("Enter choice(1/2/3/4/5/6/7): ")

            if choice in ('1', '2', '3', '4'):
                num1 = self.get_input("Enter first number: ")
                num2 = self.get_input("Enter second number: ")

                if choice == '1':
                    result = self.perform_operation(num1, num2, operator.add)
                elif choice == '2':
                    result = self.perform_operation(num1, num2, operator.sub)
                elif choice == '3':
                    result = self.perform_operation(num1, num2, operator.mul)
                elif choice == '4':
                    result = self.perform_operation(num1, num2, operator.truediv)

                if result is not None:
                    print("Result:", result)
                    self.memory = result  #Store result in memory

            elif choice == '5':
                print("Memory:", self.memory)
            elif choice == '6':
                self.memory = 0
                print("Memory cleared.")
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid input")


if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()

```