from collections import namedtuple
import json

CriticalDamage = namedtuple("CriticalDamage", "arm body head leg")
CriticalTable = namedtuple("CriticalTable", "energy impact explosion rendering")

def json_to_criticaldamage(js):
    return CriticalTable(js["arm"], js["body"], js["head"], js["leg"])

def json_to_criticaltable(js):
    mapped = {k: json_to_criticaldamage(i) for k, i in js.items()}
    return CriticalTable(mapped["energy"], None, None, None)

def load_criticals(path):
    with open(path) as f:
        return json.load(f)
