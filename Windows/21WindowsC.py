import os

path = r"C:\Users\Public"

print(f"\n📂 Listing contents of: {path}\n")

try:
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print(f"[DIR]  {item}")
        else:
            print(f"[FILE] {item}")
except PermissionError:
    print("⚠️ Access denied to some items.")
except FileNotFoundError:
    print("❌ The path does not exist.")
