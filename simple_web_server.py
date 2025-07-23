```python
# python-mini-projects/simple_web_server.py

"""
A simple web server using Python's built-in `http.server` module.

This server serves files from the current directory.  It's intended for
demonstration and testing purposes only and should not be used in a production
environment.  For production, consider using a more robust web server like
Gunicorn or uWSGI with a framework like Flask or Django.
"""

import http.server
import socketserver
import os
import argparse

def serve(port=8000, directory="."):
    """Starts a simple HTTP server.

    Args:
        port: The port number to listen on (default: 8000).
        directory: The directory to serve files from (default: current directory).
    """

    try:
        os.chdir(directory)  # Change to the specified directory
        print(f"Serving files from: {os.getcwd()}")

        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Serving at port {port}")
            httpd.serve_forever()

    except OSError as e:
        print(f"Error: {e}")
        if e.errno == 98: # Address already in use
            print("Port already in use. Please choose a different port.")
    except KeyboardInterrupt:
        print("\nServer stopped.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple HTTP Server")
    parser.add_argument("-p", "--port", type=int, default=8000, help="Port number to listen on")
    parser.add_argument("-d", "--directory", type=str, default=".", help="Directory to serve files from")
    args = parser.parse_args()

    serve(port=args.port, directory=args.directory)

```

To run this:

1.  Save the code as `simple_web_server.py` in the `python-mini-projects` directory.
2.  Navigate to the `python-mini-projects` directory in your terminal.
3.  Run the server using: `python simple_web_server.py -p 8080 -d ./my_web_files` (replace `8080` with your desired port and `./my_web_files` with the directory containing your website files, if different from the current directory).

This will start a simple web server. You can then access your website files through your web browser at `http://localhost:8080` (or the port and directory you specified).  Remember to stop the server using Ctrl+C.  The `argparse` module allows for flexible command-line arguments.  The `try...except` block handles potential errors like port conflicts and keyboard interrupts for a more robust experience.
