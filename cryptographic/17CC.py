from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'8ByteKey'  # DES key must be exactly 8 bytes
message = "Hello DES encryption!"
data = message.encode()

# Pad data to 8-byte blocks
padded_data = pad(data, DES.block_size)

# Encrypt (ECB mode)
cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(padded_data)
print("Encrypted (hex):", ciphertext.hex())

# Decrypt
decipher = DES.new(key, DES.MODE_ECB)
decrypted_padded = decipher.decrypt(ciphertext)
decrypted = unpad(decrypted_padded, DES.block_size)
print("Decrypted:", decrypted.decode())
