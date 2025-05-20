import os
import datetime
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding, utils
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.exceptions import InvalidSignature
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
from base64 import b16encode
backend = default_backend()

# This is our fictitious server - feel free to look at its code for tips
from servers import EncryptionServer
server = EncryptionServer()

### Hashing ###
# Hash the following messages using SHA256
message_one = b'This is a message we\'d like to hash. It includes a number #0112933.'
message_two = b'This is a message we\'d like to hash. It includes a number #0112934.'

# Load the entire works of Shakespeare into a bytes object

# Use the SHA-256 hash function to hash the entire works of Shakespeare



### Asymmetric Cryptography ###
# Load server public key.

# Create a challenge token

# Have the server sign it

# Verify the signature



### Digital Certificates ###
# Load certificate chain

# Validate signatures x3

# Validate certificate valid periods x3

# Optional: verify KeyUsage x3
