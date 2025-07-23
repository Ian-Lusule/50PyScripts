```python
"""
File: basic_word_counter.py
Project: python-mini-projects

This script counts the occurrences of each word in a given text file.
It handles various edge cases, including empty files and files with non-alphanumeric characters.
"""

import re
import argparse

def count_words(filepath):
    """
    Counts the occurrences of each word in a text file.

    Args:
        filepath: The path to the text file.

    Returns:
        A dictionary where keys are words (lowercase, alphanumeric only) and values are their counts.
        Returns an empty dictionary if the file is empty or contains only whitespace.  
        Raises FileNotFoundError if the file does not exist.
    """

    try:
        with open(filepath, 'r', encoding='utf-8') as file:  #Handle potential encoding issues
            text = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File not found at '{filepath}'")

    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()

    words = text.split()
    if not words: #Handle empty files or files with only whitespace
        return {}

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def main():
    """
    Parses command-line arguments and runs the word counter.
    """
    parser = argparse.ArgumentParser(description="Count words in a text file.")
    parser.add_argument("filepath", help="Path to the text file")
    args = parser.parse_args()

    try:
        word_counts = count_words(args.filepath)
        if word_counts:
            print("Word counts:")
            for word, count in word_counts.items():
                print(f"{word}: {count}")
        else:
            print("The file is empty or contains only whitespace.")
    except FileNotFoundError as e:
        print(e)
    except Exception as e: #Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

```