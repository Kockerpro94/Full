import os
import time

path = input("Enter folder path: ").strip()
now = time.time()
day = 24 * 60 * 60

for f in os.listdir(path):
    fp = os.path.join(path, f)
    if os.path.isfile(fp):
        if now - os.path.getmtime(fp) <= day:
            print(fp)
