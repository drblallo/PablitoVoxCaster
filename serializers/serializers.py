from discord import Embed
from utils.utils import split_every

MAX_FIELD_LENGHT = 1024

def talent_to_embedd(talent):
    embed = Embed(title=talent.name)
    embed.add_field(name="tier: ", value=str(talent.tier))
    embed.add_field(name="aptitudes: ", value=talent.aptitude1 + "\n" + talent.aptitude2)
    embed.add_field(name="prerequisites: ", value=talent.prerequisite)
    if talent.has_specializations:
        embed.add_field(name="specializations: ", value=talent.specializations)
    for i, partial in enumerate(split_every(talent.effect, MAX_FIELD_LENGHT)):
        embed.add_field(name=str(i+1)+": ", value=partial)


    return embed

def all_talents_to_embedd(talentsDb):
    embed = Embed(title="Talents")
    allTalents = "\n".join(talentsDb.names())
    for i, partial in enumerate(split_every(allTalents, MAX_FIELD_LENGHT)):
        embed.add_field(name=str(i+1)+": ", value=partial)
    return embed 
