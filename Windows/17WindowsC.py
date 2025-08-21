import os
import psutil
import subprocess

output = subprocess.run(["sc", "query", "type=", "service", "state=", "all"], capture_output=True, text=True)
lines = output.stdout.splitlines()

services = []
service_name = ""
display_name = ""
status = ""

for line in lines:
    line = line.strip()
    if line.startswith("SERVICE_NAME:"):
        service_name = line.split(":", 1)[1].strip()
    elif line.startswith("DISPLAY_NAME:"):
        display_name = line.split(":", 1)[1].strip()
    elif line.startswith("STATE"):
        status = "Running" if "4" in line else "Stopped"
        services.append((display_name, status))

print("\nList of all services and their status:\n")
for display_name, status in services:
    print(f"- {display_name} is currently {status}.")

print("you can type ]automatic Start] should you type like this if you want make it start automatic")
print("type exit to quit")
Input = input("type what is the proccess you want startup: ")

if "automatic Start" or "automatic start"in Input:
    os.system(f"sc config {Input} start=auto")
if "exit" or "quit" in Input:
    exit()
else:
    print("Erorr")
os.system(f"net start {Input}")