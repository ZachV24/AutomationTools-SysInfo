import platform
import psutil
import socket
from datetime import datetime

def get_sys_info();
    #Pulling Regular System Information
    info = {}
    info["System"] = platform.system()
    info["Node Name"] = platform.node()
    info["Release"] = platform.release()
    info["Version"] = platform.version()
    info["Machine"] = platform.machine()
    info["Processor"] = platform.processor()
    info["CPU Count"] = psutil.cpu_count(logical=True)
    info["Total RAM (GB)"] = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    

    # Disk Information
    disk = psutil.disk_usage('/')
    info["Total Disk Space (GB)"] = round(disk.total / (1024 ** 3), 2)
    info["Used Disk Space (GB)"] = round(disk.used / (1024 ** 3), 2)
    info["Free Disk Space (GB)"] = round(disk.free / (1024 ** 3), 2)

    # Network Information
    info["Hostname"] = socket.gethostname()
    info["IP Address"] = socket.gethostbyname(info["Hostname"])

    return info
    #Pulling Regular System Information

    def save_info_to_file(info):
        filename = f"system_info_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            for key, value in info.items():
                f.write(f"{key}: {value}\n")
        print(f"System information saved to {filename}")

    if __name__ == "__main__":
        system_info = get_sys_info()
        save_info_to_file(system_info)