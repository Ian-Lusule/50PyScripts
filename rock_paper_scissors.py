```python
"""
Rock, Paper, Scissors game.

This script implements a text-based Rock, Paper, Scissors game against the computer.
The computer's choice is randomly generated.  The game continues until the user chooses to quit.
"""
import random

def get_user_choice():
    """Gets the user's choice and validates it."""
    while True:
        choice = input("Enter your choice (rock, paper, scissors, or quit): ").lower()
        if choice in ["rock", "paper", "scissors", "quit"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def determine_winner(user_choice, computer_choice):
    """Determines the winner of a round."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Plays the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        if user_choice == "quit":
            break

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        print("-" * 20)

if __name__ == "__main__":
    try:
        play_game()
        print("Thanks for playing!")
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

```