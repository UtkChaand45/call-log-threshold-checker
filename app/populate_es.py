from datetime import datetime, timedelta
import random
import json
import requests
from config import ELASTIC_BULK_ENDPOINT  # Adjusted import to match your config structure



# ---------- STEP 1: Generate Emergency Call Logs ----------

start_time_utc = datetime(2025, 6, 27, 13, 45)
end_time_utc = datetime(2025, 6, 27, 14, 00)

accounts = [
    {"account_sid": "AC123A", "caller": "+1111111111", "pn_sid": "PN123A", "provider_sid": "OT123A", "trunk_sid": "TK1111"},
    {"account_sid": "AC123A", "caller": "+2222222222", "pn_sid": "PN456B", "provider_sid": "OT456B", "trunk_sid": "TK2222"},
    {"account_sid": "AC789C", "caller": "+3333333333", "pn_sid": "PN789C", "provider_sid": "OT789C", "trunk_sid": "TK3333"},
    {"account_sid": "AC654D", "caller": "+4444444444", "pn_sid": "PN654D", "provider_sid": "OT654D", "trunk_sid": "TK4444"},
    {"account_sid": "AC987E", "caller": "+5555555555", "pn_sid": "PN987E", "provider_sid": "OT987E", "trunk_sid": "TK5555"},
]

random.seed(42)
base_distribution = [random.randint(1000, 1500) for _ in range(5)]
scale = 3000 / sum(base_distribution)
call_counts = [int(c * scale) for c in base_distribution]

while sum(call_counts) < 3000:
    call_counts[random.randint(0, 4)] += 1

call_logs = []
call_id_counter = 199581

for acc, count in zip(accounts, call_counts):
    for _ in range(count):
        offset = random.randint(0, int((end_time_utc - start_time_utc).total_seconds()))
        call_time = start_time_utc + timedelta(seconds=offset)
        ts = call_time.isoformat(timespec='milliseconds') + "Z"
        log = {
            "account_sid": acc["account_sid"],
            "call_sid": f"CA{call_id_counter}",
            "caller_id_name": acc["caller"],
            "duration": random.randint(10, 240),
            "end_time": ts,
            "from": acc["caller"],
            "phone_number_sid": acc["pn_sid"],
            "provider_sid": acc["provider_sid"],
            "start_time": ts,
            "to": "+1911",
            "trunk_sid": acc["trunk_sid"],
            "year_month": "2025-06"
        }
        call_logs.append(log)
        call_id_counter += 1

# ---------- STEP 2: Convert to Bulk Format ----------
bulk_file_path = "18_45to19_00Wed_bulk.json"
index_name = "call_logs"

with open(bulk_file_path, "w") as outfile:
    for doc in call_logs:
        outfile.write(json.dumps({ "index": { "_index": index_name } }) + "\n")
        outfile.write(json.dumps(doc) + "\n")

# ---------- STEP 3: Upload to Elasticsearch ----------
#es_url = "http://localhost:9200/_bulk"

headers = { "Content-Type": "application/json" }

with open(bulk_file_path, "rb") as bulk_file:
    response = requests.post(ELASTIC_BULK_ENDPOINT, headers=headers, data=bulk_file)

# ---------- STEP 4: Print Result ----------
if response.status_code == 200:
    print("✅ Successfully uploaded to Elasticsearch.")
else:
    print(f"❌ Failed to upload: {response.status_code}\n{response.text}")
