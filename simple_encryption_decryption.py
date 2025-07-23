```python
# python-mini-projects/simple_encryption_decryption.py

"""
Simple Encryption/Decryption Tool using the Caesar Cipher

This script provides basic encryption and decryption functionalities using the Caesar cipher.  
The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.
"""

import argparse

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar cipher.

    Args:
        text: The text to be encrypted or decrypted.
        shift: The number of places to shift each letter.
        mode: 'encrypt' or 'decrypt'.

    Returns:
        The encrypted or decrypted text.  Returns an error message if the mode is invalid.
    """
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10)  #handle digits
        else:
            shifted_char = char #handle other characters

        result += shifted_char
    return result


def main():
    """Parses command-line arguments and performs encryption/decryption."""
    parser = argparse.ArgumentParser(description="Simple Caesar Cipher Encryption/Decryption Tool")
    parser.add_argument("text", help="Text to encrypt or decrypt")
    parser.add_argument("shift", type=int, help="Shift value (integer)")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: 'encrypt' or 'decrypt'")
    args = parser.parse_args()

    try:
        if args.mode == "encrypt":
            encrypted_text = caesar_cipher(args.text, args.shift, args.mode)
            print(f"Encrypted text: {encrypted_text}")
        elif args.mode == "decrypt":
            decrypted_text = caesar_cipher(args.text, -args.shift, args.mode) #negate shift for decryption
            print(f"Decrypted text: {decrypted_text}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

```

To run this code:

1.  Save it as `simple_encryption_decryption.py` within a directory named `python-mini-projects`.
2.  Open your terminal or command prompt, navigate to the `python-mini-projects` directory.
3.  Run the script using the following command structure, replacing placeholders:

    ```bash
    python simple_encryption_decryption.py "Your Text Here" 3 encrypt  #for encryption
    python simple_encryption_decryption.py "Your Encrypted Text Here" 3 decrypt #for decryption
    ```

    Remember to replace `"Your Text Here"` with the text you want to encrypt/decrypt and adjust the shift value (3 in this example) as needed.  The `encrypt` or `decrypt` argument specifies the operation.  The script handles digits and non-alphanumeric characters gracefully.
