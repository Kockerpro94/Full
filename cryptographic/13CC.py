import secrets

# 128-bit key (16 bytes)
key_128 = secrets.token_bytes(16)
print("AES-128 key (hex):", key_128.hex())

# 256-bit key (32 bytes)
key_256 = secrets.token_bytes(32)
print("AES-256 key (hex):", key_256.hex())
