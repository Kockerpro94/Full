import base64

original_bytes = b"Hello, World!"
encoded_bytes = base64.b64encode(original_bytes)
print(f"Base64 Encoded: {encoded_bytes}")

decoded_bytes = base64.b64decode(encoded_bytes)
print(f"Base64 Decoded: {decoded_bytes}")