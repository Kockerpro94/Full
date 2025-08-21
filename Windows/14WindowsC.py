import psutil
import time

while True:
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    processes = sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)

    print("\nTop 5 CPU-consuming processes:")
    for proc in processes[:5]:
        print(f"PID: {proc['pid']} | Name: {proc['name']} | CPU: {proc['cpu_percent']}%")

    time.sleep(2) 
