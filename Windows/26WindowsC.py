import os

root = input("Enter folder path: ").strip()
name = input("Enter file name: ").strip()

for p, d, f in os.walk(root):
    if name in f:
        print(os.path.join(p, name))
