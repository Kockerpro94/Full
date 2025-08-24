import hashlib

text = input("Enter text: ").strip().encode()

hashes = {
    "MD5": hashlib.md5(text).hexdigest(),
    "SHA1": hashlib.sha1(text).hexdigest(),
    "SHA256": hashlib.sha256(text).hexdigest()
}

for algo, h in hashes.items():
    print(f"{algo}: {h}")
