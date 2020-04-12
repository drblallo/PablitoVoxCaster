from rulebook import Rulebook

from discord import Embed

rulebook = Rulebook()

def is_embed_well_formed(embed):
    for field in embed.fields:
        return field.name is not None and field.name is not ""

def are_embeds_well_formed(embeds):
    return all(is_embed_well_formed(x) for x in embeds)

def test_is_embed_well_formed():
    e = Embed(title="something")
    f = e.add_field(name="", value="asd")
    assert not is_embed_well_formed(e)

def test_is_not_embed_well_formed():
    e = Embed(title="something")
    f = e.add_field(name="xa", value="asd")
    assert is_embed_well_formed(e)

def test_cirt_is_well_formed():
    assert is_embed_well_formed(rulebook.critical("energi", "hed", 2))
    assert is_embed_well_formed(rulebook.critical("energi", "hed"))
    
def test_insanity_is_well_formed():
    assert is_embed_well_formed(rulebook.insanity(45))
    assert is_embed_well_formed(rulebook.insanity())

def test_talents_is_well_formed():
    assert are_embeds_well_formed(rulebook.talents("air"))
    assert are_embeds_well_formed(rulebook.talents())

def test_exp_is_well_formed():
    assert is_embed_well_formed(rulebook.experience(2, 2))
