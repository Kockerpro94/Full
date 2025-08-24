import base64
import binascii
import re

def detect_encoding(s: str) -> str:
    # Check Hex (only hex chars, even length)
    if re.fullmatch(r"[0-9a-fA-F]+", s) and len(s) % 2 == 0:
        return "Hex"
    
    # Check Base64 (try decoding safely)
    try:
        base64.b64decode(s, validate=True)
        return "Base64"
    except (binascii.Error, ValueError):
        pass

    return "Unknown"

input_str = input("Enter a string: ").strip()
encoding = detect_encoding(input_str)
print(f"Detected encoding: {encoding}")