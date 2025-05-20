import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.backends import default_backend

backend = default_backend()

# This is our fictitious server - feel free to look at its code for tips
from servers import EncryptionServer
server = EncryptionServer()

### Electronic Code Book ###
key = b'\xb4\xdd$4\xbb\xa4\xf4\x8d\x9c\x17\xfb\x1b\xd4Q?\xf8'
message = b"this is a 32 byte secret message"



### Counter Mode ###
# A new 128-bit key for AES
key = b'>SMNs^\xc0\xed\xc1\xc0SS\x9d\x8f&\x02'
message = b"This secret message is an arbitrary length, as CTR mode operates as a stream cipher."

nonce = b'0000000000000001'



### Key Exchange ###
# Get server parameters (g,n)

# Generate our private key (a)

# Generate a public key using our private key (g^a mod n)

# Get server public key (g^b mod n)

# Exchange for pre-master-secret (g^ab mod n)

# Send our public key to the server so it can do the same



### Key Derivation ###
# Use HKDF to derive a symmetric key (256-bytes)

# Get a message from the server encrypted using the new shared symmetric key

# Use AES-CTR to decrypt the message



### Authenticated Encryption ###
# Generate a random key and nonce pair

# The fictitious database record
record = {
    "ID": "0054",
    "Surname": "Smith",
    "FirstName": "John",
    "JoinDate": "2016-03-12",
    "LastLogin": "2017-05-19",
    "Address": "5 Mornington Crescent, London, WN1 1DA",
    "Nationality": "UK",
    "DOB": "1963-09-14",
    "NI": "JC123456C",
    "Phone": "01224103232",
    "Data": None,
    "Nonce": None,
}

# Encrypt record function
def encrypt_record(record, key, nonce):
    # Remove pass and provide implementation
    pass

def decrypt_record(record, key):
    # Remove pass and provide implementation
    pass

# Helper function, you dont need to change it
def print_record(record):
    print("{")
    for k, v in record.items():
        print(" ", k, ":", v)
    print("}")

# Encrypt the record and print it. All confidential fields should be "None" at this point

# Decrypt the record and print it. All confidential fields should be restored
