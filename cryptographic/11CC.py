from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

print("Installing libary...")

os.system("pip install pycryptodome")
# Key must be 16, 24, or 32 bytes
key = b'ThisIsA16ByteKey'

message = "Hello, this is a secret message!"
data = message.encode()

# Pad the data to be multiple of 16 bytes
padded_data = pad(data, AES.block_size)

# Encrypt
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(padded_data)
print("Encrypted (hex):", ciphertext.hex())

# Decrypt
decipher = AES.new(key, AES.MODE_ECB)
decrypted_padded = decipher.decrypt(ciphertext)
decrypted = unpad(decrypted_padded, AES.block_size)
print("Decrypted:", decrypted.decode())
