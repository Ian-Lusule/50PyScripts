```python
"""
Number Guesser Game

This program generates a random number between 1 and 100 and asks the user to guess it.
It provides feedback on whether the guess is too high or too low.
"""

import random

def play_number_guesser():
    """Plays a number guessing game with the user."""

    number = random.randint(1, 100)
    guesses_left = 7
    print("Welcome to the Number Guesser Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guesses_left > 0:
        try:
            guess = int(input(f"You have {guesses_left} guesses left.  What's your guess? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {7 - guesses_left} tries!")
            return

        guesses_left -= 1

    print(f"You ran out of guesses. The number was {number}.")


if __name__ == "__main__":
    play_number_guesser()

```