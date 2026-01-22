import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

# Create a multipart email message object
message = MIMEMultipart()

# Sender email address
message["From"] = "xxxxx@gmail.com"

# Receiver email address
message["To"] = "xxxxxxxx@gmail.com"

# Email subject
message["Subject"] = "Test"

# Email body content
body = """
Sending email via SMTP
"""

# Attach the body text to the email as plain text
message_body = MIMEText(body, "plain")
message.attach(message_body)

try:
    # Connect to Gmail SMTP server using TLS
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()

    # Login using Gmail address and 16-digit Google App Password
    # NOTE: This password is NOT your Gmail account password.
    # It is a 16-character App Password generated from Google Account settings.
    mail.login("xxxxx@gmail.com", "xxxx xxxx xxxx xxxx")

    # Send the email
    mail.sendmail(
        message["From"],
        message["To"],
        message.as_string()
    )

    print("Email was sent successfully.")
    mail.close()

except Exception as e:
    # Print error message if something goes wrong
    sys.stderr.write("An error occurred while sending the email.\n")
    sys.stderr.write(str(e))
    sys.stderr.flush()
