import hashlib

def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

file1 = input("Enter first file path: ").strip()
file2 = input("Enter second file path: ").strip()

try:
    hash1 = sha256sum(file1)
    hash2 = sha256sum(file2)

    print(f"{file1} -> {hash1}")
    print(f"{file2} -> {hash2}")

    if hash1 == hash2:
        print("✅ Files are identical (SHA-256 match).")
    else:
        print("❌ Files differ (SHA-256 mismatch).")
except FileNotFoundError as e:
    print(f"Error: {e}")
