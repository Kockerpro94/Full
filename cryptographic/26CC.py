import os
import json
import base64

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag
os.system("pip install cryptography")

PRIVATE_KEY_PATH = "private_key.pem"
PUBLIC_KEY_PATH = "public_key.pem"


def generate_rsa_keypair(private_path: str, public_path: str, key_size: int = 2048):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
    public_key = private_key.public_key()

    with open(private_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))
    try:
        os.chmod(private_path, 0o600)
    except Exception:
        pass

    with open(public_path, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    return private_key, public_key


def load_private_key(path: str):
    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)


def load_public_key(path: str):
    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())


def hybrid_encrypt(public_key, plaintext: bytes) -> bytes:
    # 1) Generate random AES-256 key and nonce
    aes_key = AESGCM.generate_key(bit_length=256)
    aesgcm = AESGCM(aes_key)
    nonce = os.urandom(12)  # recommended size for GCM

    # 2) Encrypt plaintext with AES-GCM
    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data=None)

    # 3) Encrypt AES key with RSA-OAEP
    enc_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # 4) Package as JSON with base64 fields
    package = {
        "enc_key": base64.b64encode(enc_key).decode("ascii"),
        "nonce": base64.b64encode(nonce).decode("ascii"),
        "ciphertext": base64.b64encode(ciphertext).decode("ascii")
    }
    return json.dumps(package).encode("utf-8")


def hybrid_decrypt(private_key, package_bytes: bytes) -> bytes:
    # 1) Parse package
    package = json.loads(package_bytes.decode("utf-8"))
    enc_key = base64.b64decode(package["enc_key"])
    nonce = base64.b64decode(package["nonce"])
    ciphertext = base64.b64decode(package["ciphertext"])

    # 2) Decrypt AES key using RSA-OAEP
    aes_key = private_key.decrypt(
        enc_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # 3) Decrypt ciphertext with AES-GCM
    aesgcm = AESGCM(aes_key)
    try:
        plaintext = aesgcm.decrypt(nonce, ciphertext, associated_data=None)
    except InvalidTag as e:
        raise ValueError("Decryption failed or authentication tag invalid") from e

    return plaintext


def ensure_keys():
    if not (os.path.exists(PRIVATE_KEY_PATH) and os.path.exists(PUBLIC_KEY_PATH)):
        generate_rsa_keypair(PRIVATE_KEY_PATH, PUBLIC_KEY_PATH)


def example_usage():
    ensure_keys()
    public_key = load_public_key(PUBLIC_KEY_PATH)
    private_key = load_private_key(PRIVATE_KEY_PATH)

    message = b"Hello, World!"
    packaged = hybrid_encrypt(public_key, message)
    print("Encrypted package (JSON):")
    print(packaged.decode("utf-8"))

    decrypted = hybrid_decrypt(private_key, packaged)
    print("Decrypted message:")
    print(decrypted.decode("utf-8"))


if __name__ == "__main__":
    example_usage()

