import os
import shutil
import schedule
import time
from datetime import datetime

SOURCE = input("Enter the folder you want to back up: ").strip()
DESTINATION = input("Enter the folder where backups should be saved: ").strip()

def backup():
    today = datetime.now().strftime("%Y-%m-%d")
    target = os.path.join(DESTINATION, f"backup-{today}")
    if not os.path.exists(target):
        shutil.copytree(SOURCE, target)
        print(f"Backup created: {target}")
    else:
        print(f"Backup for {today} already exists.")

schedule.every().day.at("10:00").do(backup)

print("Backup scheduler started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
