# Import smtplib for the actual sending function
import smtplib, ssl

# Import the email modules we'll need
# from email.mime.text import MIMEText
from email.message import EmailMessage

import getpass

from_email_addr = 'u.test.1446@gmail.com'
to_email_addr = from_email_addr
smtp_server = 'smtp.gmail.com'
smtp_server_login = 'u.test.1446@gmail.com'
smtp_server_password = ''

# from_email_addr = "Private Person <mailtrap@demomailtrap.com>"
# to_email_addr = "A Test User <u.test.1446@gmail.com>"
# smtp_server = "live.smtp.mailtrap.io"
# smtp_server_login = "api"
# smtp_server_password = "068eac487d66c6dcff4a91f82b83b88a"

# from_email_addr = "Private Person <from@example.com>"
# to_email_addr = "A Test User <to@example.com>"
# smtp_server = "sandbox.smtp.mailtrap.io"
# smtp_server_login = "a02576e03d89f8"
# smtp_server_password = "a643b656b4859b"

def send_email(to_email_addr, subject, body, auht_method="TSL"):
    
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    # with open(textfile, 'rb') as fp:
    #     # Create a text/plain message
    #     message = MIMEText(fp.read())

    # Buils the 'email_message':
    message = EmailMessage()
    message.set_content(body)
    message['From'] = from_email_addr
    message['To'] = to_email_addr
    message['Subject'] = subject
    #print(message)

    smtp_server_password = getpass.getpass("Type your password and press enter: ")

    # Create a secure SSL context
    context = ssl.create_default_context()

    print("Authentication method: " + auht_method)
    if auht_method == 'SSL':
        # Method 1, using SSL:
        port = 465  # For SSL
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(smtp_server_login, smtp_server_password)

            # Send email
            server.sendmail(from_email_addr, to_email_addr, message.as_string())
            print("Email sent!")

    elif auht_method == 'TSL':
        # Method 2, using TSL:
        port = 587  # For starttls
        with smtplib.SMTP(smtp_server, port) as server:
            print(server)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(smtp_server_login, smtp_server_password)

            # Send email
            server.sendmail(from_email_addr, to_email_addr, message.as_string())
            print("Email sent!")

    else:
        print("Unknown authentication method!")

# commands used in solution video for reference
if __name__ == '__main__':
    # replace receiver email address
    send_email(to_email_addr, 'Love from Umar!', 'Sending e-mail from my Python App. You are awesome!')
