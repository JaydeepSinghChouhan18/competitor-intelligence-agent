from tools.email_sender import send_email

with open(
    "reports/latest_report.md",
    "r",
    encoding="utf-8"
) as f:

    report = f.read()

send_email(
    sender_email="yourgmail@gmail.com",
    sender_password="app_password",
    receiver_email="yourgmail@gmail.com",
    subject="Competitor Intelligence Report",
    body=report
)