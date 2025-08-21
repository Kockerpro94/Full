import psutil
import time
import os

def show_processes():
    os.system("cls")
    print(f"{'PID':<10}{'Name':<25}{'CPU %':<10}{'Memory %':<10}")
    print("-" * 55)

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            pid = proc.info['pid']
            name = proc.info['name'][:23] if proc.info['name'] else "Unknown"
            cpu = proc.info['cpu_percent']
            mem = round(proc.info['memory_percent'], 2)
            print(f"{pid:<10}{name:<25}{cpu:<10}{mem:<10}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

while True:
    show_processes()
    time.sleep(5) 