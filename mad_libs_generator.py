```python
"""
Mad Libs Generator

This program generates a Mad Libs story based on user input.  The user provides various words
(nouns, verbs, adjectives, etc.), which are then inserted into a pre-defined story template.
"""

import random

# Story templates.  Add more for variety!
story_templates = [
    """Once upon a time, in a land filled with {adjective} {plural_noun}, lived a brave {noun}.
This {noun} loved to {verb} {adverb} and dream of {plural_noun}. One day, the {noun} met a {adjective} {animal}.
Together, they embarked on a quest to find the legendary {adjective} {noun}, which was said to grant wishes.
After many {adjective} adventures, they finally found the {adjective} {noun} and made a wish for {plural_noun}!""",

    """A {adjective} {noun} sat on a {adjective} {noun}.  The {noun} was very {adjective} and {verb}ed {adverb}.
Suddenly, a {adjective} {animal} appeared and {verb}ed the {noun}!  The {noun} was very {adjective} and {verb}ed {adverb} in response.
The end."""
]


def get_user_input(word_type):
    """Gets user input for a specific word type."""
    while True:
        try:
            word = input(f"Enter a {word_type}: ").strip()
            if not word:
                raise ValueError("Input cannot be empty.")
            return word
        except ValueError as e:
            print(f"Error: {e}. Please try again.")


def generate_mad_libs():
    """Generates and prints the Mad Libs story."""
    template = random.choice(story_templates)
    #  Extract placeholders using regular expressions for flexibility
    import re
    placeholders = re.findall(r'\{(.*?)\}', template)

    #  Handle missing placeholders gracefully
    if not placeholders:
        print("Error: Story template is missing placeholders.")
        return

    filled_template = template
    for placeholder in placeholders:
        word = get_user_input(placeholder)
        filled_template = filled_template.replace(f"{{{placeholder}}}", word)

    print("\nYour Mad Libs story:\n")
    print(filled_template)


def main():
    """Main function to run the Mad Libs generator."""
    print("Welcome to the Mad Libs Generator!")
    generate_mad_libs()
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()

```