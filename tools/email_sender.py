
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(
    sender_email,
    sender_password,
    receiver_email,
    subject,
    body
):

    message = MIMEMultipart()

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(
        MIMEText(body, "plain")
    )

    with smtplib.SMTP(
        "smtp.gmail.com",
        587
    ) as server:

        server.starttls()

        server.login(
            sender_email,
            sender_password
        )

        server.send_message(
            message
        )

    print(
        "Email sent successfully"
    )