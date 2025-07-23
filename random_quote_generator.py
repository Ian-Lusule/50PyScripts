```python
# python-mini-projects/random_quote_generator.py

"""
A simple random quote generator.

This program reads quotes from a text file, randomly selects one, and prints it to the console.  
The quotes file should have one quote per line.  Error handling is included for file I/O and empty quote files.
"""

import random
import os

def get_quotes_from_file(filepath="quotes.txt"):
    """Reads quotes from a file.

    Args:
        filepath: Path to the file containing quotes (one quote per line). Defaults to "quotes.txt".

    Returns:
        A list of strings, where each string is a quote. Returns an empty list if the file is empty or contains only whitespace.
        Raises FileNotFoundError if the file does not exist.
    """
    try:
        with open(filepath, 'r') as f:
            quotes = [line.strip() for line in f if line.strip()]  #Remove empty lines and whitespace
        return quotes
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Quotes file '{filepath}' not found. Please create it with one quote per line.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the quotes file: {e}")


def generate_random_quote(quotes):
    """Selects and returns a random quote from the list.

    Args:
        quotes: A list of strings (quotes).

    Returns:
        A randomly selected quote (string). Returns None if the quotes list is empty.
    """
    if not quotes:
        return None
    return random.choice(quotes)


def main():
    """Main function to run the quote generator."""
    try:
        quotes = get_quotes_from_file()
        random_quote = generate_random_quote(quotes)

        if random_quote:
            print("Your random quote:\n", random_quote)
        else:
            print("Error: No quotes found in the file.")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

```

To use this:

1.  **Create a file named `quotes.txt`** in the same directory as `random_quote_generator.py`.
2.  **Add your quotes to `quotes.txt`, one quote per line.** For example:

```
The only way to do great work is to love what you do. - Steve Jobs
The journey of a thousand miles begins with a single step. - Lao Tzu
```

3.  Run `random_quote_generator.py` from your terminal using `python random_quote_generator.py`.  It will print a random quote from your `quotes.txt` file.


This improved version includes:

*   **Error Handling:**  Handles `FileNotFoundError` and other potential exceptions during file reading.  It also checks for empty quote files.
*   **Clearer Function Separation:** The code is broken down into well-defined functions for better readability and maintainability.
*   **Docstrings:**  Comprehensive docstrings explain the purpose and usage of each function.
*   **Robustness:** The code gracefully handles cases where the quotes file is empty or missing.
*   **Best Practices:** Follows Python style guidelines for naming conventions and code structure.


This makes the code more production-ready and easier to understand and maintain.
