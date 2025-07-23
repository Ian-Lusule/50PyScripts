```python
"""
File Splitter: Splits a large file into smaller chunks.

This script takes a large file as input and splits it into multiple smaller files of a specified size.  It handles potential errors such as incorrect file paths and invalid chunk sizes.
"""
import os

def split_file(input_file, output_prefix, chunk_size_bytes):
    """
    Splits a file into smaller chunks.

    Args:
        input_file (str): Path to the input file.
        output_prefix (str): Prefix for the output files (e.g., "part_").
        chunk_size_bytes (int): Size of each chunk in bytes.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If chunk_size_bytes is not a positive integer.
        IOError: If there's an error during file reading or writing.

    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Error: Input file '{input_file}' not found.")

    if not isinstance(chunk_size_bytes, int) or chunk_size_bytes <= 0:
        raise ValueError("Error: Chunk size must be a positive integer.")

    try:
        with open(input_file, 'rb') as infile:  # Open in binary mode for all file types
            chunk_num = 1
            while True:
                chunk = infile.read(chunk_size_bytes)
                if not chunk:
                    break  # End of file

                output_file = f"{output_prefix}{chunk_num:04d}"  # Pad chunk number with zeros
                with open(output_file, 'wb') as outfile:
                    outfile.write(chunk)
                chunk_num += 1
            print(f"File '{input_file}' split into {chunk_num -1} chunks.")

    except IOError as e:
        raise IOError(f"Error during file processing: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Split a large file into smaller chunks.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_prefix", help="Prefix for the output files (e.g., 'part_')")
    parser.add_argument("chunk_size_kb", type=int, help="Chunk size in kilobytes")

    args = parser.parse_args()

    chunk_size_bytes = args.chunk_size_kb * 1024  # Convert KB to bytes

    try:
        split_file(args.input_file, args.output_prefix, chunk_size_bytes)
    except (FileNotFoundError, ValueError, IOError) as e:
        print(f"Error: {e}")

```