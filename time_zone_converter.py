```python
# python-mini-projects/time_zone_converter.py

"""
A simple time zone converter.

This script allows users to convert a datetime object from one time zone to another.  It utilizes the `pytz` library for time zone handling.  Make sure to install it using `pip install pytz`.
"""

import datetime
import pytz

def convert_timezone(datetime_obj, from_timezone, to_timezone):
    """
    Converts a datetime object from one time zone to another.

    Args:
        datetime_obj: The datetime object to convert.  Must be timezone-aware.
        from_timezone: The name of the source time zone (e.g., 'America/New_York').
        to_timezone: The name of the target time zone (e.g., 'Europe/London').

    Returns:
        A datetime object in the target time zone, or None if an error occurs.
    """
    try:
        # Check if the input datetime object is timezone-aware
        if datetime_obj.tzinfo is None:
            raise ValueError("Input datetime object must be timezone-aware.")

        # Get timezone objects
        from_tz = pytz.timezone(from_timezone)
        to_tz = pytz.timezone(to_timezone)

        # Convert to target timezone
        converted_datetime = datetime_obj.astimezone(to_tz)
        return converted_datetime

    except pytz.exceptions.UnknownTimeZoneError:
        print(f"Error: Unknown time zone: {from_timezone} or {to_timezone}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main():
    """
    Gets user input and performs the time zone conversion.
    """
    try:
        # Get user input for datetime
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (MM): "))
        day = int(input("Enter day (DD): "))
        hour = int(input("Enter hour (HH): "))
        minute = int(input("Enter minute (MM): "))
        second = int(input("Enter second (SS): "))

        # Create a timezone-aware datetime object (using UTC as a default)
        datetime_obj = pytz.utc.localize(datetime.datetime(year, month, day, hour, minute, second))

        # Get user input for time zones
        from_timezone = input("Enter source time zone (e.g., America/New_York): ")
        to_timezone = input("Enter target time zone (e.g., Europe/London): ")

        # Perform conversion
        converted_datetime = convert_timezone(datetime_obj, from_timezone, to_timezone)

        if converted_datetime:
            print(f"Converted datetime: {converted_datetime}")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except KeyboardInterrupt:
        print("\nConversion cancelled.")


if __name__ == "__main__":
    main()

```