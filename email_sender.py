```python
"""
email_sender.py

A simple email sender using smtplib and ssl.  This script sends a single email.

For security, you should store your email credentials in environment variables 
rather than hardcoding them directly into the script.
"""

import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    """Sends an email using SMTP with SSL.

    Args:
        sender_email: The sender's email address.
        sender_password: The sender's email password.
        receiver_email: The recipient's email address.
        subject: The email subject.
        body: The email body.

    Raises:
        Exception: If there's an error sending the email.  Provides detailed error information.
    """
    try:
        # Create a multipart message
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the body of the email as plain text and HTML.
        text = body
        html = f"""\
        <html>
          <body>
            <p>{body}</p>
          </body>
        </html>
        """

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best for most email clients.
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())

    except Exception as e:
        error_message = f"Error sending email: {e}"
        print(error_message)  # Print to console for debugging
        raise Exception(error_message) # Re-raise the exception to be handled by calling function


if __name__ == "__main__":
    # Get email credentials from environment variables.  This is crucial for security.
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PASSWORD")
    receiver_email = os.environ.get("RECEIVER_EMAIL")

    # Check if credentials are set
    if not all([sender_email, sender_password, receiver_email]):
        raise ValueError("Please set SENDER_EMAIL, SENDER_PASSWORD, and RECEIVER_EMAIL environment variables.")

    subject = "Test Email from Python"
    body = "This is a test email sent from a Python script."

    try:
        send_email(sender_email, sender_password, receiver_email, subject, body)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Email sending failed: {e}")

```

**To use this code:**

1.  **Install `smtplib`:**  It's usually included with Python, but you might need to install it if you're using a minimal Python installation.  You can check if it's installed with `pip show smtplib`. If not, install it with `pip install smtplib`.
2.  **Set Environment Variables:**  Create environment variables for your sender email, password, and receiver email.  **Do not hardcode these in your script!**  How you do this depends on your operating system:
    *   **Linux/macOS:**  Use the `export` command in your terminal (e.g., `export SENDER_EMAIL="your_email@gmail.com"`).
    *   **Windows:** Use the System Properties dialog to set environment variables.
3.  **Run the script:** Execute `python email_sender.py`.

**Important Security Notes:**

*   **Never hardcode your email password directly into your code.**  This is a major security risk.  Always use environment variables or a more secure method like a secrets management system.
*   **Use a strong password** for your email account.
*   **Be aware of the security implications** of sending emails programmatically.  Ensure you understand the risks involved.  Consider using a dedicated email service for sending transactional emails in a production environment.  Gmail, for example, may have restrictions on sending emails from less secure apps. You might need to enable "less secure app access" in your Gmail settings (not recommended for security reasons).  A better approach would be to use an application-specific password.


This improved version includes better error handling, uses environment variables for security, and adds HTML support for richer email formatting.  Remember to replace the placeholder email addresses and subject/body with your actual values.
