import discord
import json
import discord_slash as interactions
from discord_slash import cog_ext
from discord.ext import commands

class Developer(commands.Cog):
    """Developer Commands. As a normal user, you shouldn't be looking here."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

def setup(bot: commands.Bot):
    bot.add_cog(Developer(bot))