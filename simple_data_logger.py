```python
# simple_data_logger.py
"""
A simple data logger that writes data to a CSV file.

This script allows users to log data with timestamps.  It handles potential errors 
like file I/O issues and provides a basic command-line interface.
"""

import csv
import datetime
import os
from typing import List, Dict, Any


def log_data(data: Dict[str, Any], filename: str = "data_log.csv") -> None:
    """Logs data to a CSV file.

    Args:
        data: A dictionary where keys are column headers and values are the data to be logged.
        filename: The name of the CSV file to write to. Defaults to "data_log.csv".

    Raises:
        IOError: If there's an error writing to the file.
        ValueError: If the data dictionary is empty.

    """
    if not data:
        raise ValueError("Data dictionary cannot be empty.")

    timestamp = datetime.datetime.now().isoformat()
    data['timestamp'] = timestamp  #add timestamp to the data

    #Check if the file exists. If not, create it with header row.
    file_exists = os.path.exists(filename)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = list(data.keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  #Write header only if file is newly created.

        writer.writerow(data)


def main():
    """Main function to handle user interaction."""
    filename = input("Enter the filename for the log (default: data_log.csv): ") or "data_log.csv"

    while True:
        try:
            num_entries = int(input("Enter the number of data entries to log: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    for i in range(num_entries):
        data_entry = {}
        while True:
            try:
                key = input(f"Enter key for entry {i+1} (or type 'done' to finish entry): ")
                if key.lower() == 'done':
                    break
                value = input(f"Enter value for key '{key}': ")
                data_entry[key] = value
            except Exception as e:
                print(f"Error processing entry: {e}")
                continue
        
        if data_entry: #only log if there is data in the entry
            try:
                log_data(data_entry, filename)
                print(f"Entry {i+1} logged successfully.")
            except (IOError, ValueError) as e:
                print(f"Error logging data: {e}")
        else:
            print("Skipping empty entry.")


if __name__ == "__main__":
    main()

```