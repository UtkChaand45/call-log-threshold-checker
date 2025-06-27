# ----------- src/config.py ----------- #
import os
from dotenv import load_dotenv

load_dotenv()

# Base Elasticsearch URL from .env
BASE_ELASTIC_URL = os.getenv("ELASTIC_URL")

ELASTIC_SEARCH_ENDPOINT = f"{BASE_ELASTIC_URL}/call_logs/_search"
ELASTIC_BULK_ENDPOINT = f"{BASE_ELASTIC_URL}/_bulk"

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

EMAIL_RECIPIENTS = os.getenv("EMAIL_RECIPIENTS")

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = os.getenv("SMTP_PORT", 587)

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

THRESHOLD = 100

LOG_FILE_PATH = "./cron_output.log"

TIME_WINDOW_MINUTES = 5



"""

twilio-alerts/
├── app/
│   ├── __pycache__/
│   ├── config.py          ✅ Holds all constants, env variables, paths, threshold
│   ├── elastic_query.py   ✅ Contains DSL query creation, call to Elastic, JSON parsing
│   ├── email_alert.py     ✅ Handles email formatting & sending
│   ├── slack_alert.py     ✅ Handles Slack message formatting & sending
│   ├── main.py            ✅ Orchestrates all functionality
│   └── cron_output.log  (Can be docker-mounted to a shared volume if needed)
├── .env                 ✅ Holds EMAIL_PASSWORD and sensitive vars
├── scheduler.py         ✅ Periodically calls main
├── requirements.txt     ✅ Declares dependencies
├── Dockerfile           ✅ Containerizes everything


"""