
from collections import UserDict

class BaseAsset(UserDict):

    def __init__(self, dic, client):
        if isinstance(dic, dict):
            super(BaseAsset, self).__init__(dic)
        else:
            raise ValueError(dic)

        self.data = _recursive_wrap_dict(self.data)
        self._client = client


    def __getattr__(self, key):
        return self.data.get(key)


class AttributeTree(dict):

    def __getattr__(self, key):
        return self.get(key)


    def __setattr__(self, key, value):
        self[key] = value


def _recursive_wrap_dict(node):
    if isinstance(node, dict):
        for key in node.keys():
            wrapped = _recursive_wrap_dict(node[key])
            if wrapped is not None: node[key] = wrapped

        return AttributeTree(node)

    elif isinstance(node, list):
        for i, value in enumerate(node):
            wrapped = _recursive_wrap_dict(value)
            if wrapped is not None: node[i] = wrapped

        return wrapped

