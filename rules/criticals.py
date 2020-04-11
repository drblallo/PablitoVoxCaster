from collections import namedtuple
from difflib import get_close_matches 
import json

crit_types = ["energy", "impact", "explosive", "rendering"]
short_type_dict = {"e": "energy", "x" : "explosive", "r": "rendering", "i": "impact"}

location_names = ["head", "body", "arm", "leg"]
short_location_names = { "h": "head", "b":"body", "a":"arm", "l":"leg" }

def canonical_crit_name(name):
    if len(name) == 1:
        return [short_type_dict[name]]

    return get_close_matches(name, crit_types, 1)

def canonical_location_name(name):
    if len(name) == 1:
        return [short_location_names[name]]
    return get_close_matches(name, location_names, 1)

def load_criticals(path):
    with open(path) as f:
        return json.load(f)
