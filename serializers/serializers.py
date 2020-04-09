from discord import Embed
from utils.utils import split_every, split_at_value

MAX_FIELD_LENGHT = 1024

def len_plus_one(string):
    return len(string) + 1

def populate_embed(embed, sentences, seperator = ""):
    divided_sencetes = split_at_value(sentences, MAX_FIELD_LENGHT, len_plus_one)

    for i, sentence in enumerate(divided_sencetes):
        embed.add_field(name=str(i+1)+": ", value=seperator.join(sentence))


def talent_to_embedd(talent):
    embed = Embed(title=talent.name)
    embed.add_field(name="tier: ", value=str(talent.tier))
    embed.add_field(name="aptitudes: ", value=talent.aptitude1 + "\n" + talent.aptitude2)
    embed.add_field(name="prerequisites: ", value=talent.prerequisite)
    if talent.has_specializations:
        embed.add_field(name="specializations: ", value=talent.specializations)

    populate_embed(embed, talent.effect.split("."))

    return embed


def all_talents_to_embedd(talentsDb):
    embed = Embed(title="Talents")
    populate_embed(embed, talentsDb.names(), "\n");

    return embed 
