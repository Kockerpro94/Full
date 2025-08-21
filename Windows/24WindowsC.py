import os

path = input("Enter folder path: ").strip()
for f in os.listdir(path):
    fp = os.path.join(path, f)
    if os.path.isfile(fp):
        print(f"{f} - {os.path.getsize(fp)} bytes")
