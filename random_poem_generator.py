```python
"""
random_poem_generator.py

Generates a random poem using a predefined set of words and structures.
"""

import random

# Define word lists for different parts of speech
nouns = ["cat", "dog", "sun", "moon", "tree", "river", "mountain", "wind", "rain", "star"]
verbs = ["runs", "jumps", "sings", "flies", "swims", "sleeps", "dreams", "shines", "falls", "rises"]
adjectives = ["happy", "sad", "big", "small", "fast", "slow", "bright", "dark", "loud", "quiet"]
adverbs = ["quickly", "slowly", "happily", "sadly", "loudly", "quietly", "brightly", "darkly", "swiftly", "gently"]


def generate_line():
    """Generates a single line of the poem."""
    structure = random.choice([
        "A {adjective} {noun} {verb} {adverb}.",
        "{Noun} {verb} {adverb}, {adjective} and free.",
        "{Adjective} {noun}, {verb}ing {adverb} in the {noun}.",
        "The {adjective} {noun} {verb} {adverb} through the {noun}."
    ])

    line = structure.format(
        noun=random.choice(nouns).capitalize(),
        verb=random.choice(verbs),
        adjective=random.choice(adjectives),
        adverb=random.choice(adverbs)
    )
    return line


def generate_poem(num_lines=4):
    """Generates a poem with the specified number of lines."""
    try:
        if not isinstance(num_lines, int) or num_lines <= 0:
            raise ValueError("Number of lines must be a positive integer.")
        poem = [generate_line() for _ in range(num_lines)]
        return "\n".join(poem)
    except ValueError as e:
        return f"Error: {e}"


if __name__ == "__main__":
    num_lines = 4  # Default number of lines
    try:
        user_input = input("Enter the desired number of lines (leave blank for default 4): ")
        if user_input:
            num_lines = int(user_input)
        poem = generate_poem(num_lines)
        print(poem)
    except ValueError as e:
        print(f"Error: Invalid input. {e}")

```