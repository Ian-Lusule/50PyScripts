```python
"""
text_based_adventure_game.py

A simple text-based adventure game.  The player explores a small world,
making choices that affect the outcome.
"""

import random

def show_intro():
    """Displays the game's introduction."""
    print("\nWelcome to the Lost City of Eldoria!\n")
    print("You are a brave adventurer, seeking fortune and glory.")
    print("Before you lies a path leading into the mysterious city...")
    print("Will you dare to enter?\n")


def choose_path():
    """Lets the player choose a path and handles invalid input."""
    while True:
        print("You encounter a fork in the road. Which path will you take?")
        print("1. The winding path through the forest")
        print("2. The steep, rocky path up the mountain")
        choice = input("> ")
        if choice in ["1", "2"]:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1 or 2.")


def forest_path():
    """Handles the forest path scenario."""
    print("\nYou choose the forest path.  The air is thick with mystery...")
    print("You encounter a talking squirrel!")
    while True:
        print("The squirrel asks for a nut. Will you give it one?")
        print("1. Yes")
        print("2. No")
        choice = input("> ")
        if choice == "1":
            print("\nThe squirrel rewards you with a magical key!")
            return "key"
        elif choice == "2":
            print("\nThe squirrel is angry and blocks your path.")
            return "blocked"
        else:
            print("Invalid choice. Please enter 1 or 2.")


def mountain_path():
    """Handles the mountain path scenario."""
    print("\nYou choose the steep mountain path. The climb is arduous...")
    print("You reach a cave.  Inside, you find a treasure chest!")
    print("But it's locked. Do you have a key?")
    has_key = input("Do you have a key? (yes/no): ").lower()
    if has_key == "yes":
        print("\nYou unlock the chest and find a priceless jewel!")
        return "jewel"
    else:
        print("\nYou can't open the chest. You leave empty-handed.")
        return "nothing"


def game_over(outcome):
    """Displays the game over message based on the outcome."""
    if outcome == "jewel":
        print("\nCongratulations! You found the priceless jewel and escaped Eldoria!")
    elif outcome == "key":
        print("\nYou obtained the magical key, but your adventure ends here for now.")
    elif outcome == "nothing":
        print("\nYou failed to find any treasure. Better luck next time!")
    elif outcome == "blocked":
        print("\nYou are blocked by an angry squirrel! Game Over.")
    else:
        print("\nUnexpected game over condition.")


def play_game():
    """Plays the main game loop."""
    show_intro()
    path_choice = choose_path()

    if path_choice == 1:
        outcome = forest_path()
    else:
        outcome = mountain_path()

    game_over(outcome)


if __name__ == "__main__":
    play_game()

```