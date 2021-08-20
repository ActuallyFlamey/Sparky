import discord
import json
import typing
import discord_slash as interactions
import aiohttp
from datetime import datetime
from discord_slash import cog_ext
from discord.ext import commands

class Utility(commands.Cog):
    """Utility Commands for Sparky."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        with open("./Sparky/SparkyBot/misc/assets/embed.json") as embedfile:
            self.embed = json.load(embedfile)
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.launch_time = datetime.utcnow()

    async def ping(self, ctx: typing.Union[commands.Context, interactions.SlashContext]):
        ping = round(self.bot.latency * 1000, 1)

        e = discord.Embed(title="Ping Latency", color=int(self.embed["color"], 16), description=f"My Ping Latency is {ping}ms.")
        e.set_author(name=self.embed["author"] + "Utility", icon_url=self.embed["icon"])
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])
        await ctx.send(embed=e)
    
    @commands.command(name="ping", aliases=["latency", "lat"])
    async def dpyping(self, ctx: commands.Context):
        """Gets Sparky's Ping Latency."""

        await self.ping(ctx)
    
    @cog_ext.cog_slash(name="ping", description="Utility - Gets Sparky's Ping Latency.")
    async def slashping(self, ctx: interactions.SlashContext):
        await self.ping(ctx)
    
    async def uptime(self, ctx: typing.Union[commands.Context, interactions.SlashContext]):
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        
        e = discord.Embed(title="Uptime", color=int(self.embed["color"], 16), description=f"The bot has been online for:\n{days} days, {hours} hours, {minutes} minutes and {seconds} seconds.")
        e.set_author(name=self.embed["author"] + "Utility", icon_url=self.embed["icon"])
        e.add_field(name="Last Restart", value="The Bot was last restarted on {} UTC".format(self.bot.launch_time.strftime("%A, %d %B %Y at %H:%M")), inline=False)
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])
        await ctx.send(embed=e)
    
    @commands.command(name="uptime")
    async def dpyuptime(self, ctx: commands.Context):
        """Shows Sparky's Uptime."""

        await self.uptime(ctx)
    
    @cog_ext.cog_slash(name="uptime", description="Utility - Shows Sparky's Uptime.")
    async def slashuptime(self, ctx: interactions.SlashContext):
        await self.uptime(ctx)
    
    @cog_ext.cog_context_menu(name="Translate", target=3)
    async def translate(self, ctx: interactions.MenuContext):
        async with aiohttp.ClientSession(headers={"Content-Type": "application/json"}) as session:
            async with session.post("https://libretranslate.com/detect", json={"q": ctx.target_message.clean_content}) as response1:
                language = await response1.json()
                language = language[0]["language"]
                async with session.post("https://libretranslate.com/translate", data={"q": ctx.target_message.clean_content, "source": language, "target": "en"}) as response2:
                    translation = await response2.json()
                    translation = translation["translatedText"]
        
        e = discord.Embed(title="Translation", color=int(self.embed["color"], 16), description=f"Here is what the message means.\nTranslated from **{language.upper()}** to **EN** by [LibreTranslate API](https://libretranslate.com/docs/).")
        e.set_author(name=self.embed["author"] + "Utility", icon_url=self.embed["icon"])
        e.add_field(name="Original Message", value=ctx.target_message.clean_content, inline=False)
        e.add_field(name="Translated Message", value=translation, inline=False)
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])
        await ctx.send(embed=e)

def setup(bot: commands.Bot):
    bot.add_cog(Utility(bot))