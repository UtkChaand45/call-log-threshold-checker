# ----------- src/slack_alert.py -----------
import requests
from datetime import datetime, timedelta
from config import SLACK_WEBHOOK_URL, LOG_FILE_PATH, TIME_WINDOW_MINUTES

def send_slack_alert(breach_entries):
    now = datetime.now()
    start_time = now - timedelta(minutes=TIME_WINDOW_MINUTES)
    time_range = f"{start_time.strftime('%I:%M %p')} - {now.strftime('%I:%M %p')}"

    message = f"🚨 *High Call Volume Alert* 🚨\n📅 Interval: `{time_range}`\n"
    for entry in breach_entries:
        message += f"• 📞 `{entry['phone']}` → *{entry['calls']} calls* (Account SID: `{entry['account_sid']}`)\n"

    payload = {"message_text": message}
    try:
        response = requests.post(SLACK_WEBHOOK_URL, json=payload)
        response.raise_for_status()
    except Exception as e:
        with open(LOG_FILE_PATH, "a") as f:
            f.write(f"[{datetime.now()}] Slack send error: {e}\n")