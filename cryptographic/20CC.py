from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter

key = b'ThisIsA16ByteKey'  # 16-byte AES key
plaintext = b"Hello, this is a secret message!"

# Generate a random 64-bit nonce
nonce = get_random_bytes(8)

# Create counter starting from nonce
ctr = Counter.new(64, prefix=nonce, initial_value=0)

# Encrypt
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
ciphertext = cipher.encrypt(plaintext)
print("Encrypted (hex):", ciphertext.hex())

# Decrypt (need the same nonce)
ctr_dec = Counter.new(64, prefix=nonce, initial_value=0)
decipher = AES.new(key, AES.MODE_CTR, counter=ctr_dec)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
