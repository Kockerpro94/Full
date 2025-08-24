from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key = b'ThisIsA16ByteKey'  # 16-byte AES key
plaintext = b"This is a secret message. " * 4  # repeated to show pattern

# Pad plaintext
padded = pad(plaintext, AES.block_size)

# Encrypt with ECB
cipher_ecb = AES.new(key, AES.MODE_ECB)
ciphertext_ecb = cipher_ecb.encrypt(padded)

# Encrypt with CBC
iv = get_random_bytes(16)
cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
ciphertext_cbc = cipher_cbc.encrypt(padded)

# Show results
print("ECB ciphertext (hex):", ciphertext_ecb.hex())
print("CBC ciphertext (hex):", ciphertext_cbc.hex())
