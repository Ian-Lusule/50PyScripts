```python
# morse_code_translator.py

"""
This module provides a function to translate text to and from Morse code.
"""

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.-', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def translate_morse(text, to_morse=True):
    """
    Translates text to or from Morse code.

    Args:
        text: The text to translate.  Should be uppercase for accurate translation.
        to_morse: A boolean indicating the translation direction. 
                  True for text to Morse, False for Morse to text.

    Returns:
        The translated text, or None if an error occurs.
    """
    try:
        if to_morse:
            text = text.upper()  # Ensure uppercase for accurate translation
            morse_code = ""
            for char in text:
                if char != ' ':
                    if char in MORSE_CODE_DICT:
                        morse_code += MORSE_CODE_DICT[char] + " "
                    else:
                        return None #Handle unsupported characters
                else:
                    morse_code += "  " #Two spaces for word separation
            return morse_code.strip() #remove trailing space

        else: #Morse to text
            words = text.split("  ")
            text = ""
            for word in words:
                chars = word.split()
                for char in chars:
                    if char in MORSE_CODE_DICT.values():
                        text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(char)]
                    else:
                        return None #Handle invalid Morse code
                text += " "
            return text.strip()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    while True:
        choice = input("Translate to Morse (1) or from Morse (2)? (Enter 'q' to quit): ")
        if choice == 'q':
            break
        elif choice in ('1', '2'):
            text = input("Enter text: ")
            to_morse = (choice == '1')
            translated_text = translate_morse(text, to_morse)
            if translated_text:
                print("Translated text:", translated_text)
            else:
                print("Invalid input or unsupported character.")
        else:
            print("Invalid choice. Please enter 1 or 2.")

```