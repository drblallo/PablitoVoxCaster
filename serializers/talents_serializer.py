from .serializers import populate_embed
from discord import Embed

def single_talent_to_embed(talent):
    embed = Embed(title=talent.name)
    embed.add_field(name="tier: ", value=str(talent.tier))
    embed.add_field(name="aptitudes: ", value=talent.aptitude1 + "\n" + talent.aptitude2)
    embed.add_field(name="prerequisites: ", value=talent.prerequisite)
    if talent.has_specializations:
        embed.add_field(name="specializations: ", value=talent.specializations)

    populate_embed(embed, talent.effect.split("."), ".")

    return embed

def all_talents_to_embedd(talentsDb):
    embed = Embed(title="Talents")
    populate_embed(embed, talentsDb.names(), "\n");

    return embed 


def talent_to_embed(talentsDb, name=None):
    if name is None:
        yield all_talents_to_embedd(talentsDb)
        return

    for talent in talentsDb.matching_name(name):
        yield single_talent_to_embed(talent)
