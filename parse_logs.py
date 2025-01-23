import json
import re

# Sample log file path
log_file = 'sample.log'

# Function to parse each log line and extract relevant data
def parse_log_line(line):
    # Regular expression to match the log pattern
    log_pattern = r'(?P<timestamp>\S+ \S+) (?P<method>\S+) (?P<endpoint>\S+) (?P<status_code>\d+) (?P<response_time>\d+)ms'
    match = re.match(log_pattern, line)
    if match:
        return match.groupdict()  # Return captured groups as a dictionary
    return None  # Return None if no match is found

# Function to parse the entire log file
def parse_logs(file_path):
    parsed_logs = []
    with open(file_path, 'r') as file:
        for line in file:
            log_data = parse_log_line(line)
            if log_data:
                parsed_logs.append(log_data)
    return parsed_logs

# Transform parsed logs into JSON format
logs = parse_logs(log_file)
json_logs = json.dumps(logs, indent=2)

# Save the transformed logs to a JSON file
with open('transformed_logs.json', 'w') as json_file:
    json_file.write(json_logs)

print("Log parsing and transformation complete.")
