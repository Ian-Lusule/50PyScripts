```python
# password_generator.py

import random
import string

def generate_password(length=12, include_lowercase=True, include_uppercase=True, 
                      include_digits=True, include_symbols=True):
    """Generates a random password based on specified criteria.

    Args:
        length: The desired length of the password (default is 12).
        include_lowercase: Whether to include lowercase letters (default is True).
        include_uppercase: Whether to include uppercase letters (default is True).
        include_digits: Whether to include digits (default is True).
        include_symbols: Whether to include symbols (default is True).

    Returns:
        A randomly generated password string, or None if invalid parameters are provided.  
        Raises ValueError if length is less than 1 or if no character sets are selected.
    """

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    character_sets = []
    if include_lowercase:
        character_sets.append(string.ascii_lowercase)
    if include_uppercase:
        character_sets.append(string.ascii_uppercase)
    if include_digits:
        character_sets.append(string.digits)
    if include_symbols:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character set must be selected.")

    combined_characters = "".join(character_sets)
    password = ''.join(random.choice(combined_characters) for i in range(length))
    return password


def main():
    """Gets user input and generates a password."""
    try:
        length = int(input("Enter desired password length (at least 1): "))
        include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, include_lowercase, include_uppercase, 
                                     include_digits, include_symbols)
        print("Generated password:", password)

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()

```