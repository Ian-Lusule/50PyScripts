```python
"""
File Downloader

This script downloads files from URLs provided by the user.  It handles potential errors
such as invalid URLs, network issues, and file access problems.
"""

import requests
import os
from urllib.parse import urlparse

def download_file(url, output_dir="downloads"):
    """
    Downloads a file from a given URL.

    Args:
        url: The URL of the file to download.
        output_dir: The directory to save the downloaded file. Defaults to "downloads".

    Returns:
        The path to the downloaded file, or None if an error occurred.
    """

    try:
        # Validate URL
        parsed_url = urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError("Invalid URL format.")

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Get file name from URL
        file_name = os.path.basename(parsed_url.path)
        if not file_name:
            file_name = "downloaded_file" #default name if no filename in URL

        output_path = os.path.join(output_dir, file_name)

        # Download the file
        response = requests.get(url, stream=True)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"File downloaded successfully to: {output_path}")
        return output_path

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return None
    except OSError as e:
        print(f"Error saving file: {e}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    url = input("Enter the URL of the file to download: ")
    download_file(url)

```