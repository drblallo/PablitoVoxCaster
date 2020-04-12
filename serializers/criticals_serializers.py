from .serializers import long_text_embed, populate_embed
from discord import Embed

def single_critical_to_embed(db, type, location, level):
    title = "Critical Damange {} {} {}".format(type, location, level + 1)
    text = db[type][location][level]
    return long_text_embed(text, title)

def multiple_critical_to_embedd(db, type, location):
    t = "Critical Damange {} {} ".format(type, location)
    embed = Embed(title=t)
    for l in range(10):
        text = db[type][location][l]
        populate_embed(embed, text.split("."), ".", str(l+1))
    
    return embed 

def critical_to_embed(db, type, location, level: int=None):
    if level is None:
        return multiple_critical_to_embedd(db, type, location)

    return single_critical_to_embed(db, type, location, level - 1)
