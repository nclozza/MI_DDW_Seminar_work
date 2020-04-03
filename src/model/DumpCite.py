from pprint import pprint
from src.common.object import Object
import json
import types

class DumpCite:
    def print(self):
        pprint(vars(self))

    def to_json(self):
        ret = Object()
        for attr, value in self.__dict__.items():
            if (value != ""):
                setattr(ret, attr, value)

        return json.dumps(ret, default=lambda o: o.__dict__)
