from .serializers import long_entry_to_embed
from discord import Embed

def table_row_name(row):
    entry_name = str(row.min)
    if row.min + 1 != row.max:
        entry_name += "-" + str(row.max)
    
    return entry_name

def table_row_to_embed(rows, name, entry_name=None):
    embed = Embed(title=name)
    for row in rows:
        entry_name = table_row_name(row)
        embed = long_entry_to_embed(embed, row.text, entry_name)
    return embed
