```python
"""
File Organizer: This script organizes files in a directory based on their type.

Usage:
  python file_organizer.py <directory_path>

Arguments:
  <directory_path>  The path to the directory to organize.

Example:
  python file_organizer.py /path/to/my/files
"""

import os
import shutil
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def organize_files(directory_path):
    """Organizes files in the specified directory based on their extension."""

    if not os.path.isdir(directory_path):
        logging.error(f"Error: Invalid directory path: {directory_path}")
        return

    file_types = {}
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath):
            extension = os.path.splitext(filename)[1].lower()
            if extension:  # Ignore files without extensions
                if extension not in file_types:
                    file_types[extension] = []
                file_types[extension].append(filename)

    for extension, files in file_types.items():
        target_dir = os.path.join(directory_path, extension[1:]) #remove leading dot
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        for file in files:
            source_path = os.path.join(directory_path, file)
            target_path = os.path.join(target_dir, file)
            try:
                shutil.move(source_path, target_path)
                logging.info(f"Moved '{file}' to '{target_dir}'")
            except shutil.Error as e:
                logging.error(f"Error moving '{file}': {e}")
            except OSError as e:
                logging.error(f"Error moving '{file}': {e}")


def main():
    """Parses command-line arguments and organizes files."""

    parser = argparse.ArgumentParser(description="Organize files in a directory.")
    parser.add_argument("directory_path", help="The path to the directory to organize")
    args = parser.parse_args()

    organize_files(args.directory_path)

if __name__ == "__main__":
    main()
```