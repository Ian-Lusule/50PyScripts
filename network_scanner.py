```python
# python-mini-projects/network_scanner.py

"""
A basic network scanner that uses the `scapy` library to discover devices on a network.

This script scans a specified IP range for active hosts by sending ARP requests.  It's important to note that running this script without proper authorization on a network you don't own or manage is unethical and potentially illegal.

Requires the `scapy` library: `pip install scapy`
"""

import argparse
import ipaddress
from scapy.all import srp, Ether, ARP, conf

def scan_network(ip_range):
    """
    Scans the specified IP range for active hosts.

    Args:
        ip_range: The IP range to scan (e.g., "192.168.1.0/24").

    Returns:
        A list of active IP addresses.  Returns an empty list if no hosts are found or an error occurs.
    """

    try:
        ip_network = ipaddress.ip_network(ip_range)
    except ValueError:
        print(f"Error: Invalid IP range '{ip_range}'. Please use CIDR notation (e.g., 192.168.1.0/24).")
        return []

    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=str(ip_network.network_address))
    answered_list = srp(arp_request, timeout=2, verbose=False)[0] # timeout in seconds

    active_hosts = []
    for answered in answered_list:
        active_hosts.append(answered[1].psrc)

    return active_hosts


def main():
    """
    Parses command-line arguments and runs the network scan.
    """
    parser = argparse.ArgumentParser(description="Basic network scanner using Scapy.")
    parser.add_argument("ip_range", help="IP range to scan (e.g., 192.168.1.0/24)")
    args = parser.parse_args()

    # Set Scapy's default interface if needed (optional, uncomment if necessary).  Replace 'eth0' with your interface name.
    # conf.iface = "eth0" 

    active_hosts = scan_network(args.ip_range)

    if active_hosts:
        print("Active hosts found:")
        for ip in active_hosts:
            print(f"- {ip}")
    else:
        print("No active hosts found in the specified range.")


if __name__ == "__main__":
    main()

```

To use this script:

1.  **Install Scapy:** `pip install scapy`
2.  **Run the script:** `python network_scanner.py <ip_range>`  (replace `<ip_range>` with the IP range you want to scan, e.g., `192.168.1.0/24`).

Remember to run this script with appropriate privileges (likely as administrator or root) and only on networks you have permission to scan.  Improper use can lead to legal consequences.  This is a basic scanner; more sophisticated tools offer additional features and capabilities.
