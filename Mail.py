import smtplib
from email.message import EmailMessage
import Config

Sender_Email=Config.Email
App_password=Config.App_password




def Send_Mail(Recipient_Email, Subject, Content):
    msg = EmailMessage()

    msg['From'] = Sender_Email
    msg['To'] = Recipient_Email
    msg['Subject'] = Subject
    msg.set_content(Content)


    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to the SMTP server
        server.login(Sender_Email, App_password)

        # Send the email message
        server.send_message(msg)
        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate. Check your email and password.")
    except smtplib.SMTPException as e:
        print("SMTP error occurred:", e)
    except Exception as e:
        print("Failed to send email:", e)

    finally:
        server.quit()
