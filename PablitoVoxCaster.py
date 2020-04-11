#!python
import os

import discord 
from dotenv import load_dotenv
from discord.ext import commands
from serializers.serializers import * 
from talents.talents import TalentsDb
from talents.talents import talent_price
from quotes.quotes import get_thought
from rules.criticals import *
from utils.table import table_from_file, table_from_list

if os.path.exists(".env"):
    load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('DISCORD_PREFIX', '#')

talentsDb = TalentsDb("./talents/talents.json")
criticalDb = load_criticals("./rules/criticals.json")
insanity_table = table_from_file("./tables/insanity.json")

bot = commands.Bot(command_prefix=PREFIX)

@bot.command(name="talents", help="returns all talents name if invoked with no arguments, returns all talents matching the provided name otherwise.", aliases=["tal"])
async def talents(ctx, name=None):
    if name is None:
        await ctx.send(embed=all_talents_to_embedd(talentsDb))
        return

    for talent in talentsDb.matching_name(name):
        await ctx.send(embed=talent_to_embedd(talent))


@bot.command(name="repo", help="returns the link to the github repository")
async def repo(ctx):
    await ctx.send("https://github.com/drblallo/PablitoVoxCaster")

@bot.command(name="thought", help="thought of the day")
async def thought(ctx):
    await ctx.send(embed=text_to_embbed(get_thought()))

def critical(type, location, level):
    if level is None:
        return multiple_critical_to_embedd(criticalDb, type, location)

    return single_critical_to_embed(criticalDb, type, location, int(level) - 1)


@bot.command(name="critical", help="returns critical of type table at location if invoked with no level. Return only the entry at level other wise.", aliases=["crit"])
async def critical_command(ctx, type, location, level=None):
    t = canonical_crit_name(type)
    if len(t) == 0:
        await ctx.send("could not find match for type "+ type)
        return

    l = canonical_location_name(location)
    if len(l) == 0:
        await ctx.send("could not find match for location "+ location)
        return

    await ctx.send(embed=critical(t[0], l[0], level))


@bot.command(name="do", help="set pablito activity")
async def set_status(ctx):
    activity = discord.Activity(type=discord.ActivityType.watching, name=" heretics burn")
    await bot.change_presence(activity=activity)

@bot.command(name="insanity", help="return insanity table if invoked without parameters, return entry which range contains value otheriwise", aliases=["ins"])
async def insanity(ctx, value=None):
    rows = insanity_table.rows()
    if value is not None:
        rows = insanity_table.matching(int(value))

    await ctx.send(embed=table_row_to_embed(rows, "insanity result"))

@bot.command(name="experience", help="outputs the cost in experience for talents by specifying tier and number of matching aptitudes", aliases=["exp","xp"])
async def exp(ctx,tier,apts):
    if tier is not None and apts is not None:
        await ctx.send(embed=text_to_embbed(str(talent_price(int(tier),int(apts)))))
        return
    return


bot.run(TOKEN)
