import aiohttp
import praw
from discord.ext.commands import BucketType
import random

import json
import requests
from requests import get
import discord
from aiohttp import ClientSession
from discord.ext import commands, tasks


# reddit = praw.Reddit(client_id='K2BENW0W2JpG3g',
#                      client_secret='w9qirVIEkNOLw6J2TrnxEwnq5O9kgQ',
#                      username='pythonmeme',
#                      password='cookies',
#                      user_agent='prawtutorial1v1')


class api(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 7, BucketType.user)
    async def meme(slef, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/dankmemes/new.json?sort=hot,") as r:
                res = await r.json()
        url = res['data']['children'][random.randint(0, 25)]['data']['url']
        title = res['data']['children'][random.randint(0, 25)]['data']['title']
        em = discord.Embed(title=f"{title}", colour=ctx.author.color)
        em.set_image(url=f"{url}")
        await ctx.send(embed=em)




    @commands.command(
        name="dadjoke",
        description="Send a dad joke!",
        aliases=['dadjokes']
    )
    @commands.cooldown(1, 7, BucketType.user)
    async def dadjoke(self, ctx):
        url = "https://dad-jokes.p.rapidapi.com/random/jokes"

        headers = {
            'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
            'x-rapidapi-key': self.bot.joke_api_key
        }

        async with ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r = await response.json()
                r = r["body"][0]
                await ctx.send(f"**{r['setup']}**\n\n||{r['punchline']}||")


def setup(bot):
    bot.add_cog(api(bot))
