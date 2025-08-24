from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key_hex = input("Enter AES key (hex): ").strip()
key = bytes.fromhex(key_hex)

input_file = "example.enc"
output_file = "example_decrypted.txt"

# Read IV + ciphertext from file
with open(input_file, "rb") as f:
    iv = f.read(16)           # first 16 bytes are IV
    ciphertext = f.read()

# Decrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext_padded = cipher.decrypt(ciphertext)
plaintext = unpad(plaintext_padded, AES.block_size)

# Write decrypted file
with open(output_file, "wb") as f:
    f.write(plaintext)

print(f"File decrypted as {output_file}")
