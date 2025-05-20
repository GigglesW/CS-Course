from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class ECDHServer(object):
    def __init__(self):
        super().__init__()
        # This example DH server uses a known elliptic curve. NIST P-256. This curve is used often
        # on the web to secure TLS messages. There is some controversy around it, with suggestions
        # of NSA involvement (!) but my strong suspicion is it's fine for normal use. If you are
        # overly cautious, use X25519.

        # Unlike standard DH, it is strongly recommended you don't generate your own curves.
        self.curve = ec.SECP256R1()

    # Return DH parameters (prime and generator)
    def get_parameters(self):
        return self.curve

    # Generate a new private key (a random number) and produce the public key based on this and the parameters.
    def get_public_key(self):
        self.private_key = ec.generate_private_key(self.curve, default_backend())
        self.public_key = self.private_key.public_key()
        return self.public_key

    # Receive another public key as part of a handshake, and use it to calculate a share secret
    def submit_public_key(self, pk):
        if pk == None:
            return

        self._pre_master_secret = self.private_key.exchange(ec.ECDH(), pk)

        # Derive the key
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.hkdf import HKDF
        hkdf = HKDF(algorithm = hashes.SHA256(), length = 32, salt = None, info = b'g53sec', backend = default_backend())

        self._shared_key = hkdf.derive(self._pre_master_secret)

