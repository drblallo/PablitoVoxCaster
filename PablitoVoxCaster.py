#!python
import os

from dotenv import load_dotenv
from discord.ext import commands
from serializers.serializers import talent_to_embedd, all_talents_to_embedd
from talents.talents import TalentsDb

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/')
talentsDb = TalentsDb("./talents/talents.json")

@bot.command(name="talents", help="dump talents name")
async def talents(ctx, name=None):
    if name is None:
        await ctx.send(embed=all_talents_to_embedd(talentsDb))
        return

    for talent in talentsDb.matching_name(name):
        await ctx.send(embed=talent_to_embedd(talent))


@bot.command(name="repo", help="returns the link to the repo")
async def repo(ctx):
    await ctx.send("https://github.com/drblallo/PablitoVoxCaster")

bot.run(TOKEN)
