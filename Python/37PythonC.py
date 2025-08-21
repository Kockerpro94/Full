def xor_encrypt_decrypt(data, key):

    xored_data = bytearray()
    key_len = len(key)
    for i in range(len(data)):
        xored_data.append(data[i] ^ key[i % key_len])
    return bytes(xored_data)

Input = input("enter string to encrypt it: ")
plaintext = b"Hello, World!"
key = b"secret"

encrypted_data = xor_encrypt_decrypt(plaintext, key)
print(f"Encrypted: {encrypted_data}")