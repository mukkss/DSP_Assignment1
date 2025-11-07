from rsa_keygen.generator import generate_rsa_keypair

def test_generate_keys():
    private, public = generate_rsa_keypair(2048)
    assert private.key_size == 2048
    assert hasattr(public, 'public_numbers')
