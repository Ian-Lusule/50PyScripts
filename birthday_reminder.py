```python
"""
birthday_reminder.py: A simple birthday reminder application.

This script allows users to store birthdays and receive reminders.  It uses a JSON file
to persist data between runs.  Error handling is included to manage file I/O and data
integrity issues.
"""

import json
import datetime
import os

DATA_FILE = "birthdays.json"


def load_birthdays():
    """Loads birthdays from the JSON file.  Creates an empty dictionary if the file doesn't exist."""
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON data in birthdays.json.  Please correct the file.")
        return {}


def save_birthdays(birthdays):
    """Saves birthdays to the JSON file."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(birthdays, f, indent=4)
    except IOError as e:
        print(f"Error saving birthdays: {e}")


def add_birthday():
    """Adds a new birthday to the database."""
    name = input("Enter name: ")
    while True:
        try:
            birthdate_str = input("Enter birthdate (YYYY-MM-DD): ")
            birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    birthdays = load_birthdays()
    birthdays[name] = birthdate.strftime("%Y-%m-%d")
    save_birthdays(birthdays)
    print(f"Birthday for {name} added successfully.")


def check_birthdays():
    """Checks for birthdays within the next 7 days and prints reminders."""
    today = datetime.date.today()
    birthdays = load_birthdays()
    for name, birthdate_str in birthdays.items():
        try:
            birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d").date()
            next_birthday = birthdate.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)

            days_until = (next_birthday - today).days
            if 0 <= days_until <= 7:
                print(f"{name}'s birthday is in {days_until} days ({next_birthday.strftime('%Y-%m-%d')})")
        except ValueError:
            print(f"Warning: Invalid date format for {name}. Skipping...")


def delete_birthday():
    """Deletes a birthday from the database."""
    birthdays = load_birthdays()
    name = input("Enter name to delete: ")
    if name in birthdays:
        del birthdays[name]
        save_birthdays(birthdays)
        print(f"Birthday for {name} deleted successfully.")
    else:
        print(f"Birthday for {name} not found.")


def main():
    """Main function to run the birthday reminder application."""
    while True:
        print("\nBirthday Reminder:")
        print("1. Add birthday")
        print("2. Check birthdays")
        print("3. Delete birthday")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_birthday()
        elif choice == "2":
            check_birthdays()
        elif choice == "3":
            delete_birthday()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

```