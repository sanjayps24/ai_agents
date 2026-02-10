import smtplib
from email.message import EmailMessage
from secrets import app_password,sender,receiver
# Email details



msg = EmailMessage()
msg.set_content("Hello! This email was sent using Python 🐍")
msg["Subject"] = "Python Email Test"
msg["From"] = sender
msg["To"] = receiver

# Send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, app_password)
    server.send_message(msg)

print("Email sent!")
