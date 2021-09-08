import json
from json import JSONEncoder


# subclass JSONEncoder
class StockEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

