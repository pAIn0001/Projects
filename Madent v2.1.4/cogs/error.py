from discord.ext import commands
import discord
from discord.ext.commands import BucketType

client = discord.Client()


class error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, "original", error)

        if isinstance(error, commands.errors.CommandOnCooldown):

            em = discord.Embed(title="Cooldown",
                               description="You are spamming **{}** \nSpamming isn't fun mate!\nIt puts a lot of pressure on Bot as wells as on API\nYour are on cooldown for {:.2f}".format(
                                   ctx.command.name, error.retry_after),
                               colour=ctx.author.color)

            return await ctx.send(embed=em)
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            em2 = discord.Embed(title="Error!!!",
                                description="Please enter all the required argument. Do `$help` for reference.",
                                colour=ctx.author.color

                                )
            return await ctx.send(embed=em2)

        elif isinstance(error, commands.errors.MemberNotFound):
            em3 = discord.Embed(title="Error!!!",
                                description="Member not found! check the spellings",
                                colour=ctx.author.color

                                )
            return await ctx.send(embed=em3)

        elif isinstance(error, commands.errors.CommandNotFound):
            em1 = discord.Embed(title="ERROR!!!", description=f"Command not found.", color=ctx.author.color)
            return await ctx.send(embed=em1)
        else:
            raise error


def setup(bot):
    bot.add_cog(error(bot))
