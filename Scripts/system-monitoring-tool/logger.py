import csv
import os

LOG_PATH = "logs/performance_log.csv"

def init_log():
    """Initializes the log file with headers if it doesn't exist."""
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    if not os.path.isfile(LOG_PATH):
        with open(LOG_PATH, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "cpu_usage", "ram_usage", "disk_usage", "running_processes"]) #CSV headers

def write_log(Data_Entry):
    """Appends a new entry to the log file."""
    with open(LOG_PATH, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            Data_Entry["timestamp"],
            Data_Entry["cpu_usage"],
            Data_Entry["ram_usage"],
            Data_Entry["disk_usage"],
            ";".join(Data_Entry["running_processes"])  # Join list into a single string
        ])