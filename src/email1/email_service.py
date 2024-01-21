import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class EmailService:
    def send_email(body, to_email):
        # email server details
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'ourtodoapp@gmail.com'
        smtp_password = 'wxcu eqbg hscg snnh'
        # Sender and recipient email addresses
        sender_email = 'ourtodoapp@gmail.com'
        recipient_email = to_email

        # We construct the email message
        message = MIMEText(body)
        message['Subject'] = "Task List"
        message['From'] = sender_email
        message['To'] = recipient_email

        try:
            # Connecting to the smtp server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls(context=ssl.create_default_context())

            # Login to the email server
            server.login(smtp_username, smtp_password)

            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())

            # Close the connection
            server.quit()

            print(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            print(f"Error sending email: {e}")

