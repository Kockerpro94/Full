import os
from typing import Tuple
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives import serialization

PRIVATE_KEY_PATH = "private_key.pem"
PUBLIC_KEY_PATH = "public_key.pem"

def ensure_rsa_keys(private_path: str = PRIVATE_KEY_PATH, public_path: str = PUBLIC_KEY_PATH, key_size: int = 2048) -> Tuple[RSAPrivateKey, RSAPublicKey]:
    if not (os.path.exists(private_path) and os.path.exists(public_path)):
        private_key: RSAPrivateKey = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
        public_key: RSAPublicKey = private_key.public_key()

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

    with open(private_path, "rb") as f:
        loaded_private = serialization.load_pem_private_key(f.read(), password=None)
    with open(public_path, "rb") as f:
        loaded_public = serialization.load_pem_public_key(f.read())

    if not isinstance(loaded_private, RSAPrivateKey) or not isinstance(loaded_public, RSAPublicKey):
        raise TypeError("Loaded keys are not RSA keys")

    return loaded_private, loaded_public
