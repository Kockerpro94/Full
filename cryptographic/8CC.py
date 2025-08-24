import base64

file_in = input("Enter file path: ").strip()
file_out = file_in + ".b64"

with open(file_in, "rb") as f_in, open(file_out, "wb") as f_out:
    base64.encode(f_in, f_out)

print(f"Encoded file saved as {file_out}")
