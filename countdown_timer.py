```python
# countdown_timer.py

import time
import os

def countdown(t):
    """
    Counts down from a given time in seconds.

    Args:
        t: The time in seconds to count down from.  Must be a positive integer.

    Raises:
        ValueError: If t is not a positive integer.
        TypeError: if t is not an integer.

    """
    if not isinstance(t, int):
        raise TypeError("Time must be an integer.")
    if t <= 0:
        raise ValueError("Time must be a positive integer.")

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')
    #Adding a system sound for better user experience.  This is OS-dependent.
    try:
        os.system('afplay /System/Library/Sounds/Glass.aiff') #For macOS
    except:
        print("System sound not available on this OS.")



if __name__ == "__main__":
    try:
        seconds = int(input("Enter the time in seconds: "))
        countdown(seconds)
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nCountdown aborted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

```