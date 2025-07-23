```python
"""
simple_calendar.py

A simple calendar application that displays a calendar for a given month and year.
"""

import calendar

def display_calendar(year, month):
    """
    Displays a calendar for the specified month and year.

    Args:
        year: The year (integer).
        month: The month (integer, 1-12).

    Raises:
        ValueError: If the year or month is invalid.
    """

    try:
        year = int(year)
        month = int(month)

        if not 1 <= month <= 12:
            raise ValueError("Invalid month. Month must be between 1 and 12.")

        cal = calendar.monthcalendar(year, month)
        
        #Get month name
        month_name = calendar.month_name[month]

        print(f"\n{month_name} {year}\n")
        print("Sun Mon Tue Wed Thu Fri Sat")

        for week in cal:
            for day in week:
                if day == 0:
                    print("    ", end=" ")
                else:
                    print(f"{day:3d}", end=" ")
            print()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    while True:
        try:
            year_str = input("Enter the year (or type 'exit' to quit): ")
            if year_str.lower() == 'exit':
                break
            month_str = input("Enter the month (1-12): ")
            display_calendar(year_str, month_str)
        except ValueError as e:
            print(f"Invalid input: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

```