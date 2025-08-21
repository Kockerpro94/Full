import hashlib

# Hashing a string
Input = input("enter string to hash it: ")
hash_object_sha256 = hashlib.md5(Input.encode())
hex_digest = hash_object_sha256.hexdigest()
print(f"Hash: {hex_digest}")

# Hashing a file iteratively
def hash_file(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(4096)  # Read in 4KB chunks
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

# Example usage (assuming a file named 'example.txt' exists)
# file_hash = hash_file('example.txt')
# print(f"File hash: {file_hash}")