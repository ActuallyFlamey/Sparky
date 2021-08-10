import discord
import json
import random
import typing
import platform
import discord_slash as interactions
from discord_slash import cog_ext
from discord.ext import commands, tasks

class Core(commands.Cog):
    """Core Commands for Sparky!"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.presence.start()
        with open("./Sparky/SparkyBot/misc/assets/embed.json") as embedfile:
            self.embed = json.load(embedfile)
    
    @tasks.loop(seconds=400.0)
    async def presence(self):
        presences = {"playing": ["with Pets", "around", "Shopkeeping Simulator", "with s!help"], "watching": ["discord.gg/pets", "the Shop"]}
        playorwatch = random.randint(1, 2)
        if playorwatch == 1:
            presencetouse = random.randint(0, 1)
            await self.bot.change_presence(activity=discord.Game(name=presences["playing"][presencetouse]))
        else:
            presencetouse = random.randint(0, 1)
            await self.bot.change_presence(activity=discord.Activity(name=presences["watching"][presencetouse], type=discord.ActivityType.watching))
    
    @presence.before_loop
    async def before_presence(self):
        await self.bot.wait_until_ready()
    
    async def info(self, ctx: typing.Union[commands.Context, interactions.SlashContext]):
        luckyint = random.randint(1, 20)

        e = discord.Embed(title="Information about Sparky", color=int(self.embed["color"], 16), description="**Sparky** is a Bot private to the **Pet Store** server.")
        e.set_author(name=self.embed["author"] + "Core", icon_url=self.embed["icon"])
        e.set_thumbnail(url=self.embed["icon"])
        e.add_field(name="Developers", value="<@450678229192278036>: All commands and their Slash equivalents.\n<@598325949808771083>: `s!help`.\nOther: `s!jishaku` (External Extension).", inline=False)
        e.add_field(name="Versions", value=f"Sparky: v0.0.3\nPython: v{platform.python_version()}\ndiscord.py: v{discord.__version__}", inline=False)
        e.set_image(url=self.embed["banner"])
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])

        await ctx.send(embed=e)

        if luckyint == 8:
            await ctx.author.send("Hey!")
            await ctx.author.send("You should try running `bab bab`!")

    @commands.command(name="info")
    async def dpyinfo(self, ctx: commands.Context):
        """Shows information about Sparky."""

        await self.info(ctx)
    
    @cog_ext.cog_subcommand(base="info", name="bot", description="Core - Shows information about Sparky.")
    async def slashinfobot(self, ctx: interactions.SlashContext):
        await self.info(ctx)
    
    @commands.command(name="parky", hidden=True)
    async def sparky(self, ctx: commands.Context):
        """???"""

        await ctx.send("Hi, I'm **Sparky the Shopkeeper**! I am a bird, and because of that, there's an Easter *Egg*!\nYes, **Flamey#0075** does really bad jokes.")

def setup(bot: commands.Bot):
    bot.add_cog(Core(bot))