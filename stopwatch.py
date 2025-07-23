```python
"""
stopwatch.py

A simple stopwatch application.  Uses the `time` module for accurate timekeeping.
"""

import time

class Stopwatch:
    """
    Represents a stopwatch that can be started, stopped, and reset.
    """

    def __init__(self):
        """Initializes the stopwatch to a stopped state."""
        self._start_time = None
        self._elapsed_time = 0

    def start(self):
        """Starts the stopwatch."""
        if self._start_time is None:
            self._start_time = time.perf_counter()
        else:
            print("Stopwatch is already running.")

    def stop(self):
        """Stops the stopwatch and updates the elapsed time."""
        if self._start_time is not None:
            elapsed = time.perf_counter() - self._start_time
            self._elapsed_time += elapsed
            self._start_time = None
        else:
            print("Stopwatch is not running.")

    def reset(self):
        """Resets the stopwatch to a stopped state with zero elapsed time."""
        self._start_time = None
        self._elapsed_time = 0

    def get_elapsed_time(self):
        """Returns the elapsed time in seconds."""
        if self._start_time is not None:
            return self._elapsed_time + (time.perf_counter() - self._start_time)
        else:
            return self._elapsed_time

    def get_elapsed_time_formatted(self, precision=3):
        """Returns the elapsed time formatted as HH:MM:SS.sss"""
        seconds = int(self.get_elapsed_time())
        milliseconds = int((self.get_elapsed_time() * 1000) % 1000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)

        return "{:02d}:{:02d}:{:02d}.{:03d}".format(hours, minutes, seconds, milliseconds)


def main():
    """Main function to run the stopwatch interactively."""
    stopwatch = Stopwatch()
    while True:
        action = input("Enter action (start, stop, reset, time, quit): ").lower()
        if action == "start":
            stopwatch.start()
        elif action == "stop":
            stopwatch.stop()
        elif action == "reset":
            stopwatch.reset()
        elif action == "time":
            print(f"Elapsed time: {stopwatch.get_elapsed_time_formatted()}")
        elif action == "quit":
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()

```