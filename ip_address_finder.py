```python
"""
File: ip_address_finder.py
Project: python-mini-projects

This script finds the public IP address of the machine it's running on.  It handles potential errors during the connection process.
"""

import requests
import socket

def get_public_ip():
    """
    Retrieves the public IP address using a public IP API.

    Returns:
        str: The public IP address as a string, or None if an error occurs.
    """
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        return data["ip"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP address from API: {e}")
        return None
    except KeyError:
        print("Error: Unexpected response format from IP API.")
        return None


def get_local_ip():
    """
    Retrieves the local IP address.

    Returns:
        str: The local IP address as a string, or None if an error occurs.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)) # Connect to a known public DNS server
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except OSError as e:
        print(f"Error getting local IP address: {e}")
        return None


if __name__ == "__main__":
    print("Finding your IP addresses...")
    public_ip = get_public_ip()
    local_ip = get_local_ip()

    if public_ip:
        print(f"Your public IP address is: {public_ip}")
    else:
        print("Could not retrieve your public IP address.")

    if local_ip:
        print(f"Your local IP address is: {local_ip}")
    else:
        print("Could not retrieve your local IP address.")

```