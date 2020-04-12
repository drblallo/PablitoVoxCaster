from discord import Embed
from utils import split_at_value

MAX_FIELD_LENGHT = 1024

def len_plus_one(string):
    return len(string) + 1

def populate_embed(embed, sentences, seperator = "", name=None, inline=False):
    divided_sencetes = split_at_value(sentences, MAX_FIELD_LENGHT, len_plus_one)

    for i, sentence in enumerate(divided_sencetes):
        nm = str(i+1)+": "  if name is None else name
        embed.add_field(name=nm, value=seperator.join(sentence), inline=inline)
    return embed

def long_entry_to_embed(embed, text, entry_name, divisor=".", inline=False):
    return populate_embed(embed, text.split(divisor), divisor, entry_name, inline)


def long_text_embed(text, tit, entry_name=None, inline=False):
    embed = Embed(title=tit)
    return long_entry_to_embed(embed, text, entry_name, ".", inline)

def text_to_embed(text):
    return Embed(title=text)
