import psutil
import time
import json
from datetime import datetime

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)
    
def collect_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("C://").percent
    running_processes = [p.name() for p in psutil.process_iter()]
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return {
        "timestamp": timestamp,
        "cpu_usage": cpu_usage,
        "ram_usage": ram_usage,
        "disk_usage": disk_usage,
        "running_processes": running_processes
    }

def check_processes(running_processes, required):
    missing = []
    for item in required:
        if item not in running_processes:
            missing.append(item)
    return missing