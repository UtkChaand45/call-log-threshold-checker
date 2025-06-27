import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from config import EMAIL_SENDER, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT, EMAIL_RECIPIENTS, LOG_FILE_PATH

def send_email_alert(breach_entries):
    subject = "🚨 Emergency Call Volume Breach Detected"
    body = "One or more phone numbers have breached the emergency call threshold:\n\n"

    for entry in breach_entries:
        body += f"• Phone: {entry['phone']} | Calls: {entry['calls']} | Account SID: {entry['account_sid']}\n"

    body += "\n--\nAutomated Alert System (Emergency Monitor)"

    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = ", ".join(EMAIL_RECIPIENTS)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENTS, msg.as_string())
        server.quit()
    except Exception as e:
        with open(LOG_FILE_PATH, "a") as f:
            f.write(f"[{datetime.now()}] Email send error: {e}\n")
