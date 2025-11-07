from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_rsa_keypair(key_size=2048):
    """
    Generate RSA public and private keys.
    Returns tuple: (private_key_obj, public_key_obj)
    """
    if key_size not in [1024, 2048, 4096]:
        raise ValueError("Invalid key size. Choose 1024, 2048, or 4096 bits.")

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size
    )
    public_key = private_key.public_key()
    return private_key, public_key


def serialize_private_key(private_key, password=None):
    """Return private key bytes in PEM format."""
    encryption = serialization.NoEncryption()
    if password:
        encryption = serialization.BestAvailableEncryption(password.encode())

    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=encryption
    )


def serialize_public_key(public_key):
    """Return public key bytes in PEM format."""
    return public_key.public_bytes( 
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
