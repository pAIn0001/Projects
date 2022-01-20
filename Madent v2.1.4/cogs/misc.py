from discord.ext import commands
import discord
from discord.ext.commands import BucketType
client = discord.Client()


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    @commands.cooldown(1, 60, BucketType.user)
    async def vote(self, ctx):
        em = discord.Embed(title="VOTE", description="**[VOTE HERE](https://discordbotlist.com/bots/madent/upvote)**",
                           color=0xFF5733)
        em.add_field(name="Server Invite", value="**[Invite Here](https://discord.gg/auz4kdK8Bq)**", inline=False)

        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def link(self, ctx):
        em = discord.Embed(title="LINKS", description="Here are the links for popular sites.", color=0xFF5733)

        em.add_field(name="Vote", value="**[Vote us](https://discordbotlist.com/bots/madent/upvote)**")

        em.add_field(name="Server Invite", value="**[Invite Here](https://discord.gg/auz4kdK8Bq)**")

        em.add_field(name="Google", value="**[Google](https://www.google.com/)**")

        em.add_field(name="Youtube", value="**[Youtube](https://www.youtube.com/)**")

        em.add_field(name="Twitter", value="**[Twitter](https://twitter.com/)**")

        em.add_field(name="Facebook", value="**[Facebook](https://www.facebook.com/)**")

        em.add_field(name="Instagram", value="**[Insta](https://www.instagram.com/)**")

        em.add_field(name="Gmail", value="**[Gmail](https://mail.google.com/)**")

        em.add_field(name="Discor bot list", value="**[DBL](https://discordbotlist.com/)**")

        em.add_field(name="Madent's page", value="**[Our page](https://discord.ly/madent)**")

        await ctx.send(embed=em)




def setup(bot):
    bot.add_cog(misc(bot))
