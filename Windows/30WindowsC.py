import os

path = input("Enter folder path: ").strip()
limit = 100 * 1024 * 1024

for p, d, f in os.walk(path):
    for file in f:
        fp = os.path.join(p, file)
        if os.path.isfile(fp) and os.path.getsize(fp) > limit:
            print(fp, "-", os.path.getsize(fp) // (1024 * 1024), "MB")
