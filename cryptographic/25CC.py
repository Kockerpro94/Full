import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.exceptions import InvalidSignature

PRIVATE_KEY_PATH = "private_key.pem"
PUBLIC_KEY_PATH = "public_key.pem"


def generate_and_save_keys(private_path: str, public_path: str, key_size: int = 2048):
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


def load_keys(private_path: str, public_path: str):
    with open(private_path, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    with open(public_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    return private_key, public_key


def sign_message(private_key, message: bytes) -> bytes:
    signature = private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return signature


def verify_signature(public_key, signature: bytes, message: bytes) -> bool:
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False


def main():
    if not (os.path.exists(PRIVATE_KEY_PATH) and os.path.exists(PUBLIC_KEY_PATH)):
        private_key, public_key = generate_and_save_keys(PRIVATE_KEY_PATH, PUBLIC_KEY_PATH)
    else:
        private_key, public_key = load_keys(PRIVATE_KEY_PATH, PUBLIC_KEY_PATH)

    message = b"Hello, World!"
    signature = sign_message(private_key, message)

    print(signature.hex())

    if verify_signature(public_key, signature, message):
        print("Signature is valid.")
    else:
        print("Signature is invalid.")


if __name__ == "__main__":
    main()
