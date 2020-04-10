from collections import namedtuple
import json

def load_criticals(path):
    with open(path) as f:
        return json.load(f)
