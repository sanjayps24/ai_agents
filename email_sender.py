import smtplib
from email.message import EmailMessage
from secrets import app_password,sender_email,receiver_email

# Email details
def send_email(receiver_email:str, Subject:str, content:str) -> str:
    

    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = Subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(content)

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
    print("Email sent!")
    return "Email send successfully"

send_email(receiver_email,"test","content")