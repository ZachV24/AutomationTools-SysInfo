import time
from monitor import load_config, collect_system_metrics, check_processes
from logger import init_log, write_log  
from notifier import notifiy

def main():
    config = load_config()
    init_log()

    cpu_alert_counter = 0

    while True:
        metrics = collect_system_metrics()
        write_log(metrics)

        #CPU threshold logistics
        if metrics["cpu_usage"] >= config["cpu_Usage_Threshold_Percent"]:
            cpu_alert_counter += 1
        else: 
            cpu_alert_counter = 0

        #Trigger CPU alert if threshold exceeded for 5 consecutive samples
        if cpu_alert_counter >= 5:
            notifiy("High CPU Usage Alert", f"CPU usage has exceeded {config['cpu_Usage_Threshold_Percent']}% for 5 consecutive samples.")
            cpu_alert_counter = 0  #Reset counter after alert

        #RAM threshold alert
        if metrics["ram_usage"] >= config["ram_Usage_Threshold_Percent"]:
            notifiy("High RAM Usage Alert", f"RAM usage is at {metrics['ram_usage']}%, exceeding the threshold of {config['ram_Usage_Threshold_Percent']}%.")

        #Check for required processes
        missing_processes = check_processes(metrics["running_processes"], config["required_Processes"])
        if missing_processes:
            notifiy("Missing Processes Alert", f"The following required processes are not running: {', '.join(missing_processes)}")

        time.sleep(config["Sampling_interval_Seconds"])

if __name__ == "__main__":
    main()