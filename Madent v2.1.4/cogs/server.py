from discord.ext import commands
import discord
from discord.ext.commands import BucketType
import datetime


class server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 30, BucketType.user)
    async def serverinfo(self, ctx):
        role_count = len(ctx.guild.roles)
        list_of_bots = [bot.name for bot in ctx.guild.members if bot.bot]


        embed2 = discord.Embed(title='ServerInfo', color=ctx.author.color)
        embed2.add_field(name='Name', value=f"{ctx.guild.name}")
        embed2.add_field(name='Owner', value=f'{str(ctx.guild.owner)}')
        embed2.add_field(name='Verification Level', value=str(ctx.guild.verification_level))
        embed2.add_field(name='Highest role', value=ctx.guild.roles[-2])
        embed2.add_field(name='Contributers:', value="None")



        embed2.add_field(name='Number of roles', value=str(role_count))
        embed2.add_field(name='Number Of Members', value=ctx.guild.member_count)
        embed2.add_field(name='Bots:', value=(', '.join(list_of_bots)))
        embed2.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'),
                         inline=False)
        embed2.set_thumbnail(url=ctx.guild.icon_url)
        embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed2)

    @commands.command()
    @commands.cooldown(1, 30, BucketType.user)
    async def membercount(self, ctx):
        em = discord.Embed(title="Members", description=f"{ctx.guild.member_count}", color=ctx.author.color)
        em.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(server(bot))
