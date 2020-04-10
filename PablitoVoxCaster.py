#!python
import os

import random
import discord 
from dotenv import load_dotenv
from discord.ext import commands
from serializers.serializers import * 
from talents.talents import TalentsDb
from quotes.quotes import get_quotes
from rules.criticals import load_criticals
from utils.table import table_from_file, table_from_list

if os.path.exists(".env"):
    load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

talentsDb = TalentsDb("./talents/talents.json")
criticalDb = load_criticals("./rules/criticals.json")
insanity_table = table_from_file("./tables/insanity.json")

today_quote = random.choice(get_quotes("./quotes/quotes.txt"))

bot = commands.Bot(command_prefix='/')

@bot.command(name="talents", help="dump talents name", aliases=["tal"])
async def talents(ctx, name=None):
    if name is None:
        await ctx.send(embed=all_talents_to_embedd(talentsDb))
        return

    for talent in talentsDb.matching_name(name):
        await ctx.send(embed=talent_to_embedd(talent))


@bot.command(name="repo", help="returns the link to the repo")
async def repo(ctx):
    await ctx.send("https://github.com/drblallo/PablitoVoxCaster")

@bot.command(name="thought", help="thought of the day")
async def thought(ctx):
    await ctx.send(embed=text_to_embbed(today_quote))

def critical(type, location, level):
    if level is None:
        return multiple_critical_to_embedd(criticalDb, type, location)

    return single_critical_to_embed(criticalDb, type, location, int(level) - 1)


@bot.command(name="energy", help="criticals damage of energy type")
async def energy_critical(ctx, location, level=None):
    await ctx.send(embed=critical("energy", location, level))

@bot.command(name="impact", help="criticals damage of impact type")
async def impact_critical(ctx, location, level=None):
    await ctx.send(embed=critical("impact", location, level))

@bot.command(name="rendering", help="criticals damage of rendering type")
async def rendering_critical(ctx, location, level=None):
    await ctx.send(embed=critical("rendering", location, level))

@bot.command(name="explosive", help="criticals damage of explosive type")
async def explosive_critical(ctx, location, level=None):
    await ctx.send(embed=critical("explosive", location, level))

@bot.command(name="do", help="set pablito activity")
async def set_status(ctx):
    activity = discord.Activity(type=discord.ActivityType.watching, name=" heretics die")
    await bot.change_presence(activity=activity)

@bot.command(name="insanity", help="return insanity table value ", aliases=["ins"])
async def insanity(ctx, value=None):
    rows = insanity_table.rows()
    if value is not None:
        rows = insanity_table.matching(int(value))

    await ctx.send(embed=table_row_to_embed(rows, "insanity result"))



bot.run(TOKEN)
