```python
# system_information_display.py

"""
Displays system information such as operating system, processor, RAM, and disk space.

This script uses the platform and psutil libraries to gather system information.  
Ensure these are installed (`pip install platform psutil`).
"""

import platform
import psutil
import os

def get_os_info():
    """Retrieves and formats operating system information."""
    return f"Operating System: {platform.system()} {platform.release()} ({platform.version()})"

def get_processor_info():
    """Retrieves and formats processor information."""
    return f"Processor: {platform.processor()}"

def get_ram_info():
    """Retrieves and formats RAM information."""
    mem = psutil.virtual_memory()
    total_ram = mem.total >> 20  # Convert bytes to MB
    available_ram = mem.available >> 20 #Convert bytes to MB
    return f"RAM: Total - {total_ram} MB, Available - {available_ram} MB"


def get_disk_info():
    """Retrieves and formats disk space information."""
    disk_info = {}
    for partition in psutil.disk_partitions():
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            disk_info[partition.mountpoint] = {
                'total': partition_usage.total >> 20, #Convert bytes to MB
                'used': partition_usage.used >> 20,  #Convert bytes to MB
                'free': partition_usage.free >> 20,  #Convert bytes to MB
                'percent': partition_usage.percent
            }
        except PermissionError:
            print(f"Permission denied accessing partition: {partition.mountpoint}")
            continue

    disk_info_str = "Disk Space:\n"
    for mountpoint, usage in disk_info.items():
        disk_info_str += f"  {mountpoint}:\n"
        disk_info_str += f"    Total: {usage['total']} MB\n"
        disk_info_str += f"    Used: {usage['used']} MB\n"
        disk_info_str += f"    Free: {usage['free']} MB\n"
        disk_info_str += f"    Percentage Used: {usage['percent']}%\n"
    return disk_info_str


def display_system_info():
    """Displays the gathered system information."""
    try:
        os_info = get_os_info()
        processor_info = get_processor_info()
        ram_info = get_ram_info()
        disk_info = get_disk_info()

        print("-" * 30)
        print("System Information")
        print("-" * 30)
        print(os_info)
        print(processor_info)
        print(ram_info)
        print(disk_info)
        print("-" * 30)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    display_system_info()

```