from discord.ext import commands
import discord
import praw
from discord.ext.commands import BucketType
import random

reddit = praw.Reddit(client_id='K2BENW0W2JpG3g',
                     client_secret='w9qirVIEkNOLw6J2TrnxEwnq5O9kgQ',
                     username='pythonmeme',
                     password='cookies',
                     user_agent='prawtutorial1v1')


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 6, BucketType.user)
    async def gay(self, ctx):
        em = discord.Embed(title="Gayrate", description=f"{ctx.author.mention} is {random.randint(0, 100)}% gay",
                           color=ctx.author.color)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 6, BucketType.user)
    async def simp(self, ctx):
        em = discord.Embed(title="Simp-o-Meter", description=f"{ctx.author.mention} is {random.randint(0, 100)}% simp",
                           color=ctx.author.color)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 6, BucketType.user)
    async def pp(self, ctx):
        responsess = ['8=D',
                      '8=========D',
                      '8==D',
                      '8====D',
                      '8=====D',
                      '8========D',
                      '8====D',
                      '8===D',
                      '8===D',
                      '8===D',
                      '8D',
                      'Unable to detect make sure u have it xD.'
                      '8============D',
                      '8====D',
                      '8====D',
                      '8====D',
                      '8======D',
                      '8===D',
                      '8==D',
                      '8=D',
                      '8======D',
                      '8=D',
                      '8D',
                      '8======D',
                      '8====D',
                      '8========D',
                      '8=======D',
                      '8=========================D',
                      '8===========D',
                      '8===D',
                      '8==D',
                      '8=D',
                      '8=======D',
                      '8===============D',
                      '8D']
        em = discord.Embed(title="Size Machine",
                           description=f"{ctx.author.name}'s penis \n {random.choice(responsess)}",
                           color=ctx.author.color)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 6, BucketType.user)
    async def toss(self, ctx):
        responses = ['heads.',
                     'tails.']
        await ctx.send(f"<a:Coin:875261665069916171>Its a {random.choice(responses)}")

    @commands.command(aliases=['8ball', '8b'])
    @commands.cooldown(1, 30, BucketType.user)
    async def eightball(self, ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "ask again later when I'm less busy with ur mum",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        em = discord.Embed(title=f"{question}", description=f"🎱 {random.choice(responses)} ", color=ctx.author.color)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(fun(bot))
