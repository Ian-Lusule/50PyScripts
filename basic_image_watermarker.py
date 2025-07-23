```python
"""
Basic Image Watermarker

This script adds a text watermark to an image.  It uses the Pillow library.
"""

from PIL import Image, ImageDraw, ImageFont
import argparse
import os

def add_watermark(image_path, output_path, text, font_path=None, font_size=36, color=(255, 255, 255), opacity=0.5):
    """Adds a watermark to an image.

    Args:
        image_path: Path to the input image.
        output_path: Path to save the watermarked image.
        text: Text for the watermark.
        font_path: Path to the font file (optional, defaults to a system font).
        font_size: Font size.
        color: RGB color tuple for the watermark text.
        opacity: Opacity of the watermark (0.0-1.0).

    Raises:
        FileNotFoundError: If the image file or font file is not found.
        ValueError: If the opacity is not within the range [0.0, 1.0].
        Exception: For any other errors during image processing.

    """
    try:
        # Open the image
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)

        # Choose font
        if font_path:
            try:
                font = ImageFont.truetype(font_path, font_size)
            except IOError:
                raise FileNotFoundError(f"Font file not found: {font_path}")
        else:
            try:
                font = ImageFont.load_default()  # Fallback to default font
            except Exception as e:
                raise Exception(f"Error loading default font: {e}")


        # Get text size
        text_width, text_height = draw.textsize(text, font=font)

        # Calculate watermark position (bottom right)
        margin = 10
        x = img.width - text_width - margin
        y = img.height - text_height - margin

        # Add watermark with opacity
        draw.text((x, y), text, font=font, fill=color)

        # Save the watermarked image
        img.save(output_path)
        print(f"Watermarked image saved to {output_path}")

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Image file not found: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid opacity value: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a watermark to an image.")
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("output_path", help="Path to save the watermarked image")
    parser.add_argument("text", help="Watermark text")
    parser.add_argument("-f", "--font", dest="font_path", help="Path to the font file (optional)")
    parser.add_argument("-s", "--size", type=int, default=36, help="Font size (default: 36)")
    parser.add_argument("-c", "--color", default=(255, 255, 255), type=lambda x: tuple(map(int, x.split(','))), help="Watermark color (RGB, default: 255,255,255)")
    parser.add_argument("-o", "--opacity", type=float, default=0.5, help="Watermark opacity (0.0-1.0, default: 0.5)")

    args = parser.parse_args()

    if not 0.0 <= args.opacity <= 1.0:
        raise ValueError("Opacity must be between 0.0 and 1.0")

    try:
        add_watermark(args.image_path, args.output_path, args.text, args.font_path, args.size, args.color, args.opacity)
    except (FileNotFoundError, ValueError, Exception) as e:
        print(f"Error: {e}")

```