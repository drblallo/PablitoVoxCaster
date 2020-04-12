from collections import namedtuple
from difflib import get_close_matches 
import json


def crit_find_string(name, names, short_hand):
    if len(name) == 1:
        return short_hand[name]

    possible = get_close_matches(name, names, 1)
    if len(possible) == 0:
        return None
    return possible[0]


crit_types = ["energy", "impact", "explosive", "rendering"]
short_type_dict = {"e": "energy", "x" : "explosive", "r": "rendering", "i": "impact"}
def canonical_type_name(name):
    return crit_find_string(name, crit_types, short_type_dict)


location_names = ["head", "body", "arm", "leg"]
short_location_names = { "h": "head", "b":"body", "a":"arm", "l":"leg" }
def canonical_location_name(name):
    return crit_find_string(name, location_names, short_location_names)

def canonical_crit_names(tp, location):
    t = canonical_type_name(tp)
    if t is None:
        raise ValueError("could not find match for type {}".format(type))

    l = canonical_location_name(location)
    if l is None:
        raise ValueError("could not find match for location {}".format(location))

    return (t, l)


def load_criticals(path):
    with open(path) as f:
        return json.load(f)
