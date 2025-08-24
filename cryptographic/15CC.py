from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128-bit AES key
input_file = "example.txt"
output_file = "example.enc"

# Read plaintext
with open(input_file, "rb") as f:
    plaintext = f.read()

# Generate random IV
iv = get_random_bytes(16)

# Encrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# Write IV + ciphertext to file
with open(output_file, "wb") as f:
    f.write(iv + ciphertext)

print(f"File encrypted as {output_file}")
print(f"AES key (hex) for decryption: {key.hex()}")
