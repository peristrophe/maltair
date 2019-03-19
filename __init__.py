
from . import client

Client = client.Communicator

class AttrDict(dict):
    def __getattr__(self, key):
        return self.get(key, None)

    def __setattr__(self, key, value):
        self[key] = value

