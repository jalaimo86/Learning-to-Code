from http import server
import smtplib
import ssl

def send_sms_via_email(number: str, message: str, provider: str, sender_credentials: tuple, subject: str = "send usring python", smtp_server: str = "smtp.gmail.com", smtp_port: int = 465):
    sender_email, email_password = sender_credentials

    receiver_email = f"{number}@txt.att.net"
    message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, message)


def main():
    number = "8435405406"
    message = input("enter message: ")
    provider = "AT&T"
    sender_credentials = ("jalaimo86@gmail.com", "azrltidhiuskmzeh")
    send_sms_via_email(number, message, provider, sender_credentials)
    

main()