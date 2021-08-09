import discord
import json
import typing
import discord_slash as interactions
import aiohttp
import random
from discord_slash import cog_ext
from discord.ext import commands

class Fun(commands.Cog):
    """Fun Commands for Sparky!"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        with open("./api.json") as apifile:
            self.api = json.load(apifile)
        with open("./Sparky/SparkyBot/misc/assets/embed.json") as embedfile:
            self.embed = json.load(embedfile)
    
    async def cat(self, ctx: typing.Union[commands.Context, interactions.SlashContext]):
        async def getcat():
            async with aiohttp.ClientSession(headers={"x-api-key": self.api["thecatapi"]}) as session:
                async with session.get("https://api.thecatapi.com/v1/images/search") as response:
                    cat = await response.json()
                    pic = cat[0]["url"]
            return pic
        
        cat = await getcat()

        e = discord.Embed(title="Random Cat Picture", color=int(self.embed["color"], 16), description="Here's a picture of a cat straight from [TheCatAPI](https://thecatapi.com/)!")
        e.set_author(name=self.embed["author"] + "Fun", icon_url=self.embed["icon"])
        e.set_image(url=cat)
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])
        catmsg = await ctx.send(embed=e, components=[
            interactions.utils.manage_components.create_actionrow(
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.blurple, "Another!", None, "anothercat")
            )
        ])

        while True:
            waitfor: interactions.ComponentContext = await interactions.utils.manage_components.wait_for_component(self.bot, catmsg, ["anothercat", "upvotecat", "downvotecat"])
            if waitfor.author.id == ctx.author.id:
                cat = await getcat()
                e.set_image(url=cat)
                await waitfor.edit_origin(embed=e)
            else:
                await waitfor.send("Only the original author can request another cat!", hidden=True)
    
    @commands.command(name="cat")
    async def dpycat(self, ctx: commands.Context):
        """Shows a random cat image!"""

        await ctx.trigger_typing()
        await self.cat(ctx)
    
    @cog_ext.cog_subcommand(base="animals", name="cat", description="Fun - Shows a random cat image!")
    async def slashanimalscat(self, ctx: interactions.SlashContext):
        await self.cat(ctx)
    
    async def dog(self, ctx: typing.Union[commands.Context, interactions.SlashContext]):
        async def getdog():
            async with aiohttp.ClientSession(headers={"x-api-key": self.api["thedogapi"]}) as session:
                async with session.get("https://api.thedogapi.com/v1/images/search") as response:
                    dog = await response.json()
                    pic = dog[0]["url"]
            return pic
        
        dog = await getdog()

        e = discord.Embed(title="Random Dog Picture", color=int(self.embed["color"], 16), description="Here's a picture of a dog straight from [TheDogAPI](https://thedogapi.com/)!")
        e.set_author(name=self.embed["author"] + "Fun", icon_url=self.embed["icon"])
        e.set_image(url=dog)
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])
        dogmsg = await ctx.send(embed=e, components=[
            interactions.utils.manage_components.create_actionrow(
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.blurple, "Another!", None, "anotherdog")
            )
        ])

        while True:
            waitfor: interactions.ComponentContext = await interactions.utils.manage_components.wait_for_component(self.bot, dogmsg, ["anotherdog", "upvotedog", "downvotedog"])
            if waitfor.author.id == ctx.author.id:
                dog = await getdog()
                e.set_image(url=dog)
                await waitfor.edit_origin(embed=e)
            else:
                await waitfor.send("Only the original author can request another dog!", hidden=True)
    
    @commands.command(name="dog")
    async def dpydog(self, ctx: commands.Context):
        """Shows a random dog image!"""

        await ctx.trigger_typing()
        await self.dog(ctx)
    
    @cog_ext.cog_subcommand(base="animals", name="dog", description="Fun - Shows a random dog image!")
    async def slashanimalsdog(self, ctx: interactions.SlashContext):
        await self.dog(ctx)
    
    async def bird(self, ctx: typing.Union[commands.Context, interactions.SlashContext]):
        async def getbird():
            async with aiohttp.ClientSession() as session:
                async with session.get("https://some-random-api.ml/img/birb") as response:
                    bird = await response.json()
                    pic = bird["link"]
            return pic
        
        bird = await getbird()

        sparkyfound = None
        if random.randint(1, 250) == 125:
            bird = self.embed["icon"]
            sparkyfound = "**Congratulations! You found an Easter Egg! You found __Sparky__!**"
        
        e = discord.Embed(title="Random Bird Picture", color=int(self.embed["color"], 16), description="Here's a picture of a bird straight from [Some Random API](https://some-random-api.ml/)!")
        e.set_author(name=self.embed["author"] + "Fun", icon_url=self.embed["icon"])
        if sparkyfound is not None:
            e.description += f"\n\n{sparkyfound}"
        e.set_image(url=bird)
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])
        birdmsg = await ctx.send(embed=e, components=[
            interactions.utils.manage_components.create_actionrow(
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.blurple, "Another!", None, "anotherbird")
            )
        ])

        while True:
            waitfor: interactions.ComponentContext = await interactions.utils.manage_components.wait_for_component(self.bot, birdmsg, ["anotherbird"])
            if waitfor.author.id == ctx.author.id:
                bird = await getbird()
                e.set_image(url=bird)
                await waitfor.edit_origin(embed=e)
            else:
                await waitfor.send("Only the original author can request another bird!", hidden=True)
        
    @commands.command(name="bird")
    async def dpybird(self, ctx: commands.Context):
        """Shows a random bird image!\nThere's a 1 in 250 chance to find Sparky!"""

        await ctx.trigger_typing()
        await self.bird(ctx)
    
    @cog_ext.cog_subcommand(base="animals", name="bird", description="Fun - Shows a random bird image!")
    async def slashanimalsbird(self, ctx: interactions.SlashContext):
        await self.bird(ctx)
    
    async def fox(self, ctx: typing.Union[commands.Context, interactions.SlashContext]):
        async def getfox():
            async with aiohttp.ClientSession() as session:
                async with session.get("https://randomfox.ca/floof") as response:
                    fox = await response.json()
                    pic = fox["image"]
            return pic
        
        fox = await getfox()
        
        e = discord.Embed(title="Random Fox Picture", color=int(self.embed["color"], 16), description="Here's a picture of a fox straight from [Random Fox](https://randomfox.ca/)!")
        e.set_author(name=self.embed["author"] + "Fun", icon_url=self.embed["icon"])
        e.set_image(url=fox)
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])
        foxmsg = await ctx.send(embed=e, components=[
            interactions.utils.manage_components.create_actionrow(
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.blurple, "Another!", None, "anotherfox")
            )
        ])

        while True:
            waitfor: interactions.ComponentContext = await interactions.utils.manage_components.wait_for_component(self.bot, foxmsg, ["anotherfox"])
            if waitfor.author.id == ctx.author.id:
                fox = await getfox()
                e.set_image(url=fox)
                await waitfor.edit_origin(embed=e)
            else:
                await waitfor.send("Only the original author can request another fox!", hidden=True)
        
    @commands.command(name="fox")
    async def dpyfox(self, ctx: commands.Context):
        """Shows a random fox image!"""

        await ctx.trigger_typing()
        await self.fox(ctx)
    
    @cog_ext.cog_subcommand(base="animals", name="fox", description="Fun - Shows a random fox image!")
    async def slashanimalsfox(self, ctx: interactions.SlashContext):
        await self.fox(ctx)
    
    async def redpanda(self, ctx: typing.Union[commands.Context, interactions.SlashContext]):
        async def getredpanda():
            async with aiohttp.ClientSession() as session:
                async with session.get("https://some-random-api.ml/img/red_panda") as response:
                    redpanda = await response.json()
                    pic = redpanda["link"]
            return pic
        
        redpanda = await getredpanda()
        
        e = discord.Embed(title="Random Red Panda Picture", color=int(self.embed["color"], 16), description="Here's a picture of a red panda straight from [Some Random API](https://some-random-api.ml/)!")
        e.set_author(name=self.embed["author"] + "Fun", icon_url=self.embed["icon"])
        e.set_image(url=redpanda)
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])
        redpandamsg = await ctx.send(embed=e, components=[
            interactions.utils.manage_components.create_actionrow(
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.blurple, "Another!", None, "anotherredpanda")
            )
        ])

        while True:
            waitfor: interactions.ComponentContext = await interactions.utils.manage_components.wait_for_component(self.bot, redpandamsg, ["anotherredpanda"])
            if waitfor.author.id == ctx.author.id:
                redpanda = await getredpanda()
                e.set_image(url=redpanda)
                await waitfor.edit_origin(embed=e)
            else:
                await waitfor.send("Only the original author can request another red panda!", hidden=True)
        
    @commands.command(name="redpanda", aliases=["rpanda", "redp"])
    async def dpyredpanda(self, ctx: commands.Context):
        """Shows a random red panda image!"""

        await ctx.trigger_typing()
        await self.redpanda(ctx)
    
    @cog_ext.cog_subcommand(base="animals", name="red-panda", description="Fun - Shows a random red panda image!")
    async def slashanimalsredpanda(self, ctx: interactions.SlashContext):
        await self.redpanda(ctx)
    
    async def koala(self, ctx: typing.Union[commands.Context, interactions.SlashContext]):
        async def getkoala():
            async with aiohttp.ClientSession() as session:
                async with session.get("https://some-random-api.ml/img/koala") as response:
                    koala = await response.json()
                    pic = koala["link"]
            return pic
        
        koala = await getkoala()
        
        e = discord.Embed(title="Random Koala Picture", color=int(self.embed["color"], 16), description="Here's a picture of a koala straight from [Some Random API](https://some-random-api.ml/)!")
        e.set_author(name=self.embed["author"] + "Fun", icon_url=self.embed["icon"])
        e.set_image(url=koala)
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])
        koalamsg = await ctx.send(embed=e, components=[
            interactions.utils.manage_components.create_actionrow(
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.blurple, "Another!", None, "anotherkoala")
            )
        ])

        while True:
            waitfor: interactions.ComponentContext = await interactions.utils.manage_components.wait_for_component(self.bot, koalamsg, ["anotherkoala"])
            if waitfor.author.id == ctx.author.id:
                koala = await getkoala()
                e.set_image(url=koala)
                await waitfor.edit_origin(embed=e)
            else:
                await waitfor.send("Only the original author can request another koala!", hidden=True)
    
    @commands.command(name="koala")
    async def dpykoala(self, ctx: commands.Context):
        """Shows a random koala image!"""

        await ctx.trigger_typing()
        await self.koala(ctx)
    
    @cog_ext.cog_subcommand(base="animals", name="koala", description="Fun - Shows a random koala image!")
    async def slashanimalskoala(self, ctx: interactions.SlashContext):
        await self.koala(ctx)
    
    async def panda(self, ctx: typing.Union[commands.Context, interactions.SlashContext]):
        async def getpanda():
            async with aiohttp.ClientSession() as session:
                async with session.get("https://some-random-api.ml/img/panda") as response:
                    panda = await response.json()
                    pic = panda["link"]
            return pic
        
        panda = await getpanda()
        
        e = discord.Embed(title="Random Panda Picture", color=int(self.embed["color"], 16), description="Here's a picture of a panda straight from [Some Random API](https://some-random-api.ml/)!")
        e.set_author(name=self.embed["author"] + "Fun", icon_url=self.embed["icon"])
        e.set_image(url=panda)
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])
        pandamsg = await ctx.send(embed=e, components=[
            interactions.utils.manage_components.create_actionrow(
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.blurple, "Another!", None, "anotherpanda")
            )
        ])

        while True:
            waitfor: interactions.ComponentContext = await interactions.utils.manage_components.wait_for_component(self.bot, pandamsg, ["anotherpanda"])
            if waitfor.author.id == ctx.author.id:
                panda = await getpanda()
                e.set_image(url=panda)
                await waitfor.edit_origin(embed=e)
            else:
                await waitfor.send("Only the original author can request another panda!", hidden=True)
    
    @commands.command(name="panda")
    async def dpypanda(self, ctx: commands.Context):
        """Shows a random panda image!"""

        await ctx.trigger_typing()
        await self.panda(ctx)
    
    @cog_ext.cog_subcommand(base="animals", name="panda", description="Fun - Shows a random panda image!")
    async def slashanimalspanda(self, ctx: interactions.SlashContext):
        await self.panda(ctx)

def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))