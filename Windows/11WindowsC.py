import psutil

for proc in psutil.process_iter(['pid', 'name']):
    print(f"PID: {proc.info['pid']} | Name: {proc.info['name']}")
