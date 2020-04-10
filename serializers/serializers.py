from discord import Embed
from utils.utils import split_every, split_at_value

MAX_FIELD_LENGHT = 1024

def len_plus_one(string):
    return len(string) + 1

def populate_embed(embed, sentences, seperator = "", name=None):
    divided_sencetes = split_at_value(sentences, MAX_FIELD_LENGHT, len_plus_one)

    for i, sentence in enumerate(divided_sencetes):
        nm = str(i+1) if name is None else name
        embed.add_field(name=nm+": ", value=seperator.join(sentence))
    return embed


def talent_to_embedd(talent):
    embed = Embed(title=talent.name)
    embed.add_field(name="tier: ", value=str(talent.tier))
    embed.add_field(name="aptitudes: ", value=talent.aptitude1 + "\n" + talent.aptitude2)
    embed.add_field(name="prerequisites: ", value=talent.prerequisite)
    if talent.has_specializations:
        embed.add_field(name="specializations: ", value=talent.specializations)

    populate_embed(embed, talent.effect.split("."), ".")

    return embed

def single_critical_to_embed(db, type, location, level):
    title = "Critical Damange " + type + " " + location + " " + str(level + 1)
    text = db[type][location][level]
    return long_text_embbed(text, title)

def multiple_critical_to_embedd(db, type, location):
    t = "Critical Damange " + type + " " + location 
    embed = Embed(title=t)
    for l in range(10):
        text = db[type][location][l]
        populate_embed(embed, text.split("."), ".", str(l+1))
    
    return embed 

def all_talents_to_embedd(talentsDb):
    embed = Embed(title="Talents")
    populate_embed(embed, talentsDb.names(), "\n");

    return embed 

def long_entry_to_embbed(embed, text, entry_name=None, divisor="."):
    text = text.split(divisor)
    return populate_embed(embed, text, divisor, entry_name)

def long_text_embbed(text, tit, entry_name=None):
    embed = Embed(title=tit)
    return long_entry_to_embbed(embed, text, entry_name)

def text_to_embbed(text):
    return Embed(title=text)

def table_row_name(row):
    entry_name = str(row.min)
    if row.min + 1 != row.max:
        entry_name += "-" + str(row.max)

    return entry_name

def table_row_to_embed(rows, name, entry_name=None):
    embed = Embed(title=name)
    for row in rows:
        entry_name = table_row_name(row)
        embed = long_entry_to_embbed(embed, row.text, entry_name)
    return embed
