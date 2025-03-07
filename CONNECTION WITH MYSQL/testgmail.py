import smtplib
from email.message import EmailMessage

EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 465,
    'sender_email': 'vdubey8511@gmail.com',
    'sender_password': 'nogcmdrmgvgcrkik',  # Use the EXACT App Password
    'recipient_email': 'vdubey8511@gmail.com'
}

def send_test_email():
    msg = EmailMessage()
    msg['Subject'] = "Test Email"
    msg['From'] = EMAIL_CONFIG['sender_email']
    msg['To'] = EMAIL_CONFIG['recipient_email']
    msg.set_content("This is a test email.")

    try:
        with smtplib.SMTP_SSL(
            EMAIL_CONFIG['smtp_server'], 
            EMAIL_CONFIG['smtp_port']
        ) as server:
            server.login(
                EMAIL_CONFIG['sender_email'], 
                EMAIL_CONFIG['sender_password']
            )
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_test_email()