from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key_input = input("Enter a key (16, 24, or 32 chars): ").strip()
key = key_input.encode()
if len(key) not in (16, 24, 32):
    print("Key must be 16, 24, or 32 bytes!")
    exit()

text = input("Enter text to encrypt: ").strip().encode()
output_file = input("Enter output filename: ").strip()

# Generate random IV
iv = get_random_bytes(16)

# Encrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(text, AES.block_size))

# Save IV + ciphertext to file
with open(output_file, "wb") as f:
    f.write(iv + ciphertext)

print(f"Encrypted data saved to {output_file}")
