import requests
import json

url = "http://localhost:9200/logs/_doc/"
headers = {'Content-Type': 'application/json'}
log_data = {
    "message": "This is a sample log message",
    "timestamp": "2025-01-23T12:00:00",
    "log_level": "INFO"
}

response = requests.post(url, data=json.dumps(log_data), headers=headers, auth=('admin', 'admin'))

if response.status_code == 200:
    print("Log ingested successfully")
else:
    print(f"Failed to ingest log: {response.status_code}, {response.text}")
