from .DHServer import DHServer
from .RSAServer import RSAServer
from .SymmetricServer import SymmetricServer
from .ECDHServer import ECDHServer


class EncryptionServer(SymmetricServer, DHServer, RSAServer):
    def __init__(self):
        super().__init__()
        self._shared_key = None

