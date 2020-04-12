#!python
import os
from rulebook import Rulebook
import discord 
from dotenv import load_dotenv
from discord.ext import commands

if os.path.exists(".env"):
    load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('DISCORD_PREFIX', '#')

bot = commands.Bot(command_prefix=PREFIX)
rulebook = Rulebook()

@bot.command( \
    help="""returns all talents name if invoked with no arguments, 
            returns all talents matching 
            the provided name otherwise.""", \
    aliases=["tal"])
async def talents(ctx, name=None):
    for embed in rulebook.talents(name):
        await ctx.send(embed=embed)

@bot.command(help="returns the link to the github repository")
async def repo(ctx):
    await ctx.send("https://github.com/drblallo/PablitoVoxCaster")

@bot.command(help="thought of the day")
async def thought(ctx):
    await ctx.send(embed=rulebook.get_thought())

@bot.command(
    help="""returns critical of type table at location 
            if invoked with no level. 
            Return only the entry at level otherwise.""", \
    aliases=["crit"])
async def critical(ctx, type, location, level :int=None):
    await ctx.send(embed=rulebook.critical(type, location, level))

@bot.command(help="set pablito activity")
async def do(ctx):
    activity = discord.Activity(type=discord.ActivityType.watching, name=" heretics burn")
    await bot.change_presence(activity=activity)

@bot.command(
    help="""return insanity table if invoked without parameters, 
        return entry which range contains value otheriwise""", 
    aliases=["ins"])
async def insanity(ctx, value:int =None):
    await ctx.send(embed=rulebook.insanity(value))

@bot.command(
    help="""outputs the cost in experience for talents 
            by specifying tier and number of matching aptitudes""", 
    aliases=["exp","xp"])
async def experience(ctx, tier :int, apts :int):
    await ctx.send(embed=rulebook.experience(tier, apts))


bot.run(TOKEN)
