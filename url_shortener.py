```python
"""
URL Shortener

This script provides a simple URL shortening functionality using a dictionary to store
shortened URLs and their corresponding long URLs.  It's for demonstration purposes and
doesn't include persistent storage (e.g., database).  For a production-ready system,
consider using a database and a unique short code generation algorithm.
"""
import random
import string

# In-memory storage for short URLs (replace with a database in a real application)
url_mapping = {}

def generate_short_code(length=6):
    """Generates a random short code of specified length."""
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def shorten_url(long_url):
    """Shortens a given long URL."""
    if not long_url:
        raise ValueError("Long URL cannot be empty.")

    # Check if URL already exists
    for short_code, url in url_mapping.items():
        if url == long_url:
            return short_code

    # Generate a unique short code
    while True:
        short_code = generate_short_code()
        if short_code not in url_mapping:
            break

    url_mapping[short_code] = long_url
    return short_code


def expand_url(short_code):
    """Expands a shortened URL to its original long URL."""
    if not short_code:
        raise ValueError("Short code cannot be empty.")

    if short_code in url_mapping:
        return url_mapping[short_code]
    else:
        raise ValueError(f"Short code '{short_code}' not found.")


def main():
    """Main function to interact with the URL shortener."""
    while True:
        print("\nURL Shortener Menu:")
        print("1. Shorten URL")
        print("2. Expand URL")
        print("3. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                long_url = input("Enter the long URL: ")
                short_code = shorten_url(long_url)
                print(f"Shortened URL: {short_code}")

            elif choice == '2':
                short_code = input("Enter the short code: ")
                long_url = expand_url(short_code)
                print(f"Long URL: {long_url}")

            elif choice == '3':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

```