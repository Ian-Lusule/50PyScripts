```python
"""
Simple Image Resizer

This script resizes images to a specified width and height while maintaining aspect ratio.
It uses the Pillow library for image manipulation.  Make sure to install it: `pip install Pillow`
"""

from PIL import Image
import argparse
import os

def resize_image(input_path, output_path, width, height):
    """
    Resizes an image while maintaining aspect ratio.

    Args:
        input_path: Path to the input image file.
        output_path: Path to save the resized image.
        width: Desired width of the resized image.
        height: Desired height of the resized image.

    Raises:
        FileNotFoundError: If the input image file is not found.
        ValueError: If width or height are not positive integers.
        IOError: If there's an error during image processing.

    """
    try:
        #Open the image using Pillow library
        img = Image.open(input_path)
        
        #Get original image dimensions
        original_width, original_height = img.size

        #Calculate aspect ratio
        aspect_ratio = original_width / original_height

        #Determine new dimensions while maintaining aspect ratio
        if width and height:  #Both width and height are specified
            if width / height > aspect_ratio:
                new_width = int(height * aspect_ratio)
                new_height = height
            else:
                new_width = width
                new_height = int(width / aspect_ratio)

        elif width: #Only width is specified
            new_width = width
            new_height = int(width / aspect_ratio)
        elif height: #Only height is specified
            new_width = int(height * aspect_ratio)
            new_height = height
        else:
            raise ValueError("At least one of width or height must be specified.")

        #Resize the image
        resized_img = img.resize((new_width, new_height))

        #Save the resized image
        resized_img.save(output_path)

        print(f"Image resized and saved to: {output_path}")

    except FileNotFoundError:
        print(f"Error: Input image file not found at {input_path}")
    except ValueError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error during image processing: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Parses command-line arguments and resizes the image.
    """
    parser = argparse.ArgumentParser(description="Resize an image while maintaining aspect ratio.")
    parser.add_argument("input_path", help="Path to the input image file")
    parser.add_argument("output_path", help="Path to save the resized image")
    parser.add_argument("-w", "--width", type=int, help="Desired width of the resized image")
    parser.add_argument("-h", "--height", type=int, help="Desired height of the resized image")

    args = parser.parse_args()

    #Check if output directory exists, create if not
    output_dir = os.path.dirname(args.output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    resize_image(args.input_path, args.output_path, args.width, args.height)


if __name__ == "__main__":
    main()

```