import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

key_sizes = [512, 1024, 2048]
message = b"Test message for RSA performance"

def test_rsa_speed():
    for size in key_sizes:
        start_gen = time.time()
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=size, backend=default_backend())
        public_key = private_key.public_key()
        end_gen = time.time()
        gen_time = end_gen - start_gen

        start_enc = time.time()
        ciphertext = public_key.encrypt(
            message,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        end_enc = time.time()
        enc_time = end_enc - start_enc

        start_dec = time.time()
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        end_dec = time.time()
        dec_time = end_dec - start_dec

        print(f"Key size: {size} bits")
        print(f"Key generation time: {gen_time:.6f} sec")
        print(f"Encryption time: {enc_time:.6f} sec")
        print(f"Decryption time: {dec_time:.6f} sec")
        print(f"Decrypted message matches original: {plaintext == message}")
        print("-"*50)

if __name__ == "__main__":
    test_rsa_speed()
