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
                    pic = cat["url"]
                    catid = cat["id"]
            return [pic, catid]
        
        async def votecat(catid: str, vote: int):
            async with aiohttp.ClientSession(headers={"x-api-key": self.api["thecatapi"]}) as session:
                await session.post("https://api.thecatapi.com/v1/votes", data={
                    "image_id": catid,
                    "value": vote
                })
        
        cat = await getcat()

        e = discord.Embed(title="Random Cat Picture", color=int(self.embed["color"], 16), description="Here's a picture of a cat straight from [TheCatAPI](https://thecatapi.com/)!")
        e.set_author(name=self.embed["author"] + "Fun", icon_url=self.embed["icon"])
        e.set_image(url=cat[0])
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])
        catmsg = await ctx.send(embed=e, components=[
            interactions.utils.manage_components.create_actionrow(
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.blurple, "Another!", None, "anothercat")
            ),
            interactions.utils.manage_components.create_actionrow(
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.green, "Upvote Image", None, "upvotecat"),
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.red, "Downvote Image", None, "downvotecat")
            )
        ])

        while True:
            waitfor: interactions.ComponentContext = await interactions.utils.manage_components.wait_for_component(self.bot, catmsg, ["anothercat", "upvotecat", "downvotecat"])
            if waitfor.custom_id == "another":
                if waitfor.author.id == ctx.author.id:
                    cat = await getcat()
                    waitfor.origin_message.embeds[0].image = cat[0]
                    await waitfor.edit_origin(embed=e)
                else:
                    await waitfor.send("Only the original author can request another cat!", hidden=True)
            elif waitfor.custom_id == "upvote":
                await votecat(cat[1], 1)
                await waitfor.send("Image upvoted!", hidden=True)
            elif waitfor.custom_id == "downvote":
                await votecat(cat[1], 0)
                await waitfor.send("Image downvoted.", hidden=True)
    
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
                    pic = dog["url"]
                    dogid = dog["id"]
            return [pic, dogid]
        
        async def votedog(dogid: str, vote: int):
            async with aiohttp.ClientSession(headers={"x-api-key": self.api["thedogapi"]}) as session:
                await session.post("https://api.thedogapi.com/v1/votes", data={
                    "image_id": dogid,
                    "value": vote
                })
        
        dog = await getdog()

        e = discord.Embed(title="Random Dog Picture", color=int(self.embed["color"], 16), description="Here's a picture of a dog straight from [TheDogAPI](https://thedogapi.com/)!")
        e.set_author(name=self.embed["author"] + "Fun", icon_url=self.embed["icon"])
        e.set_image(url=dog[0])
        e.set_footer(text=self.embed["footer"], icon_url=self.embed["icon"])
        dogmsg = await ctx.send(embed=e, components=[
            interactions.utils.manage_components.create_actionrow(
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.blurple, "Another!", None, "anotherdog")
            ),
            interactions.utils.manage_components.create_actionrow(
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.green, "Upvote Image", None, "upvotedog"),
                interactions.utils.manage_components.create_button(interactions.utils.manage_components.ButtonStyle.red, "Downvote Image", None, "downvotedog")
            )
        ])

        while True:
            waitfor: interactions.ComponentContext = await interactions.utils.manage_components.wait_for_component(self.bot, dogmsg, ["anotherdog", "upvotedog", "downvotedog"])
            if waitfor.custom_id == "another":
                if waitfor.author.id == ctx.author.id:
                    dog = await getdog()
                    waitfor.origin_message.embeds[0].image = dog[0]
                    await waitfor.edit_origin(embed=e)
                else:
                    await waitfor.send("Only the original author can request another dog!", hidden=True)
            elif waitfor.custom_id == "upvote":
                await votedog(dog[1], 1)
                await waitfor.send("Image upvoted!", hidden=True)
            elif waitfor.custom_id == "downvote":
                await votedog(dog[1], 0)
                await waitfor.send("Image downvoted.", hidden=True)
    
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
                async with session.get("https://some-random-api.ml/animal/birb") as response:
                    bird = await response.json()
                    pic = bird["image"]
            return pic
        
        bird = await getbird()

        sparkyfound = None
        if random.randint(1, 250) == 125:
            bird = self.embed["icon"]
            sparkyfound = "**Congratulations! You found an Easter Egg! You found __Sparky__!**"
        
        e = discord.Embed(title="Random Bird Picture", color=int(self.embed["color"], 16), description="Here's a picture of a bird straight from [Some Random API](https://some-random-api.ml/)!")
        e.set_author(name=self.embed["author"], icon_url=self.embed["icon"])
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
                waitfor.origin_message.embeds[0].image = await getbird()
                await waitfor.edit_origin(embed=e)
            else:
                await waitfor.send("Only the original author can request another bird!", hidden=True)
        
    @commands.command(name="bird")
    async def dpybird(self, ctx: commands.Context):
        """Shows a random bird image!\nThere's a 1 in 250 chance to find Sparky!"""

        await ctx.trigger_typing()
        await self.bird(ctx)
    
    @cog_ext.cog_subcommand(base="animals", name="bird", description="Fun - Shows a random bird image!")
    async def slashbird(self, ctx: interactions.SlashContext):
        await self.bird(ctx)

def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))