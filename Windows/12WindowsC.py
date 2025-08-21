import psutil
import os


for proc in psutil.process_iter(['pid', 'name']):
    print(f"PID: {proc.info['pid']} | Name: {proc.info['name']}")

print("this working in windows")
Input = input("what the proccess name you want kill it: ")

process_name = Input   # change this to the name you want to kill

for proc in psutil.process_iter(['pid', 'name']):
    if proc.info['name'] == process_name:
        print(f"Killing {process_name} with PID {proc.info['pid']}")
        proc.terminate()   # or proc.kill() for force kill
