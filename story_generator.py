```python
"""
story_generator.py: A simple story generator using templates.

This program allows users to create stories by filling in blanks in pre-defined templates.
"""

import random

TEMPLATES = [
    """Once upon a time, in a land filled with {adjective} {nouns}, lived a {adjective} {noun}.  This {noun} loved to {verb} {adverb}.  One day, they encountered a {adjective} {noun} who {verb} {adverb}! The end.""",
    """Deep in the {adjective} forest, there lived a {adjective} {animal}. This {animal} was known for its {adjective} {noun}. One day, while {verb}ing near a {adjective} {noun}, it discovered a {adjective} {noun}!  What will it do? The end.""",
    """A {adjective} {noun} and a {adjective} {noun} were {verb}ing together when suddenly, a {adjective} {noun} appeared!  This caused a great {adjective} {noun}!  The story concludes with a {adjective} {noun}. The end."""
]

WORDS = {
    "adjective": ["brave", "silly", "clever", "magical", "tiny", "giant", "fierce", "gentle"],
    "noun": ["dragon", "princess", "wizard", "castle", "forest", "mountain", "river", "tree"],
    "verb": ["ran", "jumped", "flew", "sang", "danced", "laughed", "cried", "slept"],
    "adverb": ["quickly", "slowly", "happily", "sadly", "angrily", "excitedly", "carefully", "loudly"],
    "animal": ["cat", "dog", "bird", "fox", "bear", "lion", "elephant", "monkey"]
}


def get_word(word_type):
    """Gets a random word of the specified type."""
    try:
        return random.choice(WORDS[word_type])
    except KeyError:
        return "Error: Invalid word type"


def generate_story():
    """Generates a story using a random template and words."""
    template = random.choice(TEMPLATES)
    story = template
    for word_type in WORDS:
        story = story.replace("{" + word_type + "}", get_word(word_type))
    return story


def main():
    """Main function to run the story generator."""
    print("Welcome to the Story Generator!\n")
    try:
        num_stories = int(input("How many stories would you like to generate? "))
        if num_stories <= 0:
            print("Please enter a positive number of stories.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    for _ in range(num_stories):
        print(generate_story())
        print("-" * 20)


if __name__ == "__main__":
    main()

```