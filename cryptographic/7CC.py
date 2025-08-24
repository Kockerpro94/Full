import hashlib

target_hash = input("Enter MD5 hash: ").strip()

for pin in range(10000):
    guess = f"{pin:04d}"   # ensures 4 digits with leading zeros
    h = hashlib.md5(guess.encode()).hexdigest()
    if h == target_hash:
        print(f"PIN found: {guess}")
        break
else:
    print("No match found in range 0000-9999")
