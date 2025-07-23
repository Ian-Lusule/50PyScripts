```python
"""
File Merger: Merges multiple files into a single output file.

This script takes a list of input files and merges their contents into a single 
output file.  It handles various file types and provides error handling for 
missing files and other potential issues.
"""

import os
import argparse

def merge_files(input_files, output_file):
    """
    Merges multiple files into a single output file.

    Args:
        input_files: A list of paths to input files.
        output_file: The path to the output file.

    Raises:
        FileNotFoundError: If any of the input files are not found.
        IOError: If there's an error reading or writing a file.
    """

    if not input_files:
        raise ValueError("No input files specified.")

    try:
        with open(output_file, 'wb') as outfile:  # 'wb' for binary mode to handle various file types
            for input_file in input_files:
                if not os.path.exists(input_file):
                    raise FileNotFoundError(f"Input file not found: {input_file}")
                with open(input_file, 'rb') as infile:  # 'rb' for binary mode
                    outfile.write(infile.read())
        print(f"Files merged successfully into: {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error during file I/O: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def main():
    """Parses command-line arguments and merges files."""
    parser = argparse.ArgumentParser(description="Merge multiple files into one.")
    parser.add_argument("input_files", nargs="+", help="Paths to the input files")
    parser.add_argument("output_file", help="Path to the output file")
    args = parser.parse_args()

    try:
        merge_files(args.input_files, args.output_file)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

```