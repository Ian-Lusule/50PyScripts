```python
"""
currency_converter.py

A simple currency converter using exchange rates from a fixed dictionary.  For a production-ready application, you would replace this with a real-time API call to a currency exchange service.
"""

import sys

# Replace this with a real-time API call for production use.
EXCHANGE_RATES = {
    "USD": {"USD": 1.0, "EUR": 0.92, "GBP": 0.79, "JPY": 144.0},
    "EUR": {"USD": 1.09, "EUR": 1.0, "GBP": 0.86, "JPY": 156.0},
    "GBP": {"USD": 1.27, "EUR": 1.16, "GBP": 1.0, "JPY": 182.0},
    "JPY": {"USD": 0.0069, "EUR": 0.0064, "GBP": 0.0055, "JPY": 1.0},
}


def convert_currency(amount, from_currency, to_currency):
    """Converts an amount from one currency to another.

    Args:
        amount: The amount to convert (float).
        from_currency: The source currency (str, e.g., "USD").
        to_currency: The target currency (str, e.g., "EUR").

    Returns:
        The converted amount (float), or None if an error occurs.
    """
    try:
        amount = float(amount)
        if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES[from_currency]:
            raise ValueError("Invalid currency code.")
        return amount * EXCHANGE_RATES[from_currency][to_currency]
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """Main function to handle user input and output."""
    if len(sys.argv) != 4:
        print("Usage: python currency_converter.py <amount> <from_currency> <to_currency>")
        return

    amount, from_currency, to_currency = sys.argv[1:]
    converted_amount = convert_currency(amount, from_currency.upper(), to_currency.upper())

    if converted_amount is not None:
        print(f"{amount} {from_currency.upper()} is equal to {converted_amount:.2f} {to_currency.upper()}")


if __name__ == "__main__":
    main()

```