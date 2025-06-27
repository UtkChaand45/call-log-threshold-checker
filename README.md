<details>
    <summary>📄 <strong>README.md</strong> (click to expand)</summary>

# 🚨 Twilio Emergency Call Alerting System (POC)

A production-ready Python-based monitoring system that continuously checks for emergency call volume threshold breaches in real time, using data from an Elasticsearch instance. Alerts are sent to Slack and email channels.

---

## 📦 Features

- ✅ Periodic check for emergency call threshold breach
- ✅ Slack & Email notifications
- ✅ Dockerized Elasticsearch and Kibana
- ✅ Configurable thresholds and alerting intervals via `.env`
- ✅ Logs written to `cron_output.log`

---

## 📁 Project Structure

```
twilio-alerts/
│
├── app/
│   ├── config.py
│   ├── elastic_query.py
│   ├── email_alert.py
│   ├── slack_alert.py
│   ├── main.py
│   ├── cron_output.log
│   ├── populate_es.py
│
├── scheduler.py
├── requirements.txt
├── Dockerfile
├── .env               # Keep this local (NEVER commit)
├── .env.example       # Share this instead
├── docker-compose.yml
└── es-data/           # Elasticsearch volume mount
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/twilio-alerts.git
cd twilio-alerts
```

### 2. Create `.env` File

Copy `.env.example` to `.env` and fill in your configuration. **Never commit your `.env` file.**

### 3. Start the Stack

```bash
docker compose up -d
```

- **Mount Volumes:** Logs and Elasticsearch data are volume-mounted so you can view them locally.
- **Persist Data:** `es-data/` ensures your Elasticsearch data is not lost between Docker restarts.

### 4. Stopping and Cleaning Up

```bash
docker compose down
```

Your logs and Elasticsearch data will be preserved thanks to volume mounts.

---

## 🛠️ Future Improvements

- Auto-remediation scripts post alert
- Dashboard summary using Kibana
- Alert suppression during expected surges
- Automated call classification via ML

---

## 👨‍💻 Maintainer

**Utkarsh**

Feel free to raise issues or pull requests!

</details>