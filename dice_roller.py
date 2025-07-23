```python
"""
Dice Roller Simulator

This script simulates rolling a specified number of dice with a specified number of sides.
"""
import random

def roll_dice(num_dice, num_sides):
    """
    Simulates rolling multiple dice.

    Args:
        num_dice: The number of dice to roll (must be a positive integer).
        num_sides: The number of sides on each die (must be a positive integer).

    Returns:
        A list of integers representing the results of each die roll, 
        or None if invalid input is provided.  Prints an error message if input is invalid.
    """
    if not isinstance(num_dice, int) or num_dice <= 0:
        print("Error: Number of dice must be a positive integer.")
        return None
    if not isinstance(num_sides, int) or num_sides <= 0:
        print("Error: Number of sides must be a positive integer.")
        return None

    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, num_sides))
    return results

def main():
    """
    Gets user input and runs the dice rolling simulation.
    """
    try:
        num_dice = int(input("Enter the number of dice to roll: "))
        num_sides = int(input("Enter the number of sides on each die: "))

        results = roll_dice(num_dice, num_sides)
        if results:
            print("Results:", results)
            print("Total:", sum(results))

    except ValueError:
        print("Error: Invalid input. Please enter integers only.")


if __name__ == "__main__":
    main()

```