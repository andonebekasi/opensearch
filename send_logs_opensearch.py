from opensearchpy import OpenSearch
import json

# Konfigurasi OpenSearch
client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],  # OpenSearch berjalan di localhost
    http_auth=("admin", "admin"),                # Username dan password
)

# Baca file JSON
file_path = "transformed_logs.json"
with open(file_path, "r") as file:
    logs = json.load(file)

# Kirim setiap log ke OpenSearch
index_name = "logsss-index"
for log in logs:
    response = client.index(index=index_name, body=log)
    print(f"Log berhasil dikirim dengan ID: {response['_id']}")
