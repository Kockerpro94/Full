from Crypto.Util.Padding import pad, unpad

block_size = 16  # AES block size in bytes

def pkcs7_pad(plaintext: bytes) -> bytes:
    return pad(plaintext, block_size)

def pkcs7_unpad(padded: bytes) -> bytes:
    return unpad(padded, block_size)

# Example usage
plaintext = b"Hello, this is a test!"
print("Original:", plaintext)

padded = pkcs7_pad(plaintext)
print("Padded (hex):", padded.hex())

unpadded = pkcs7_unpad(padded)
print("Unpadded:", unpadded)
