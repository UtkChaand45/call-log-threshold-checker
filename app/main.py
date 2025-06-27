# ----------- src/main.py -----------
from datetime import datetime
from config import LOG_FILE_PATH
from slack_alert import send_slack_alert
from email_alert import send_email_alert
from elastic_query import fetch_breaches

def main():
    try:
        with open(LOG_FILE_PATH, "a") as f:
            f.write(f"\n--- {datetime.now()} ---\n")

        matches = fetch_breaches()
        if matches:
            with open(LOG_FILE_PATH, "a") as f:
                f.write("Threshold breaches found:\n")
                for entry in matches:
                    f.write(f"Phone: {entry['phone']} | Calls: {entry['calls']} | SID: {entry['account_sid']}\n")
            send_slack_alert(matches)
            send_email_alert(matches)
        else:
            with open(LOG_FILE_PATH, "a") as f:
                f.write("No threshold breaches.\n")

    except Exception as e:
        with open(LOG_FILE_PATH, "a") as f:
            f.write(f"Exception occurred: {e}\n")

if __name__ == "__main__":
    main()
