# import asyncpg
# from requests import get
# import discord
# from discord.ext import commands, tasks
# from discord.ext.commands import when_mentioned_or
# intents = discord.Intents.all()
# client = discord.Client()
# DEFAULT_PREFIX = "$"

# async def get_prefix(client, message):
#     if not message.guild:
#         return commands.when_mentioned_or(DEFAULT_PREFIX)(client, message)
#     prefix = await client.db.fetch('SELECT prefix From guilds WHERE guild_id =$1', message.guild.id)
#     if len(prefix) == 0:
#         await client.db.execute('INSERT INTO guild (guild_id, prefix) VALUES ($1, $2)', message.guild.id,
#                                 DEFAULT_PREFIX)
#         prefix = DEFAULT_PREFIX
#     else:
#         prefix = prefix[0].get(prefix)
#     return commands.when_mentioned_or(prefix)(client, message)

# client = commands.Bot(command_prefix=get_prefix, intents=intents)


# class prefix(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#         self.bot.loop.run_until_complete(self.create_pool())
        

#     async def create_pool(self):
#         client.db = await asyncpg.create_pool(database="tutorial", user = "postgres", password = "rehan2006kinggf")
#         print("Connection succesfull to data base")

#     @commands.command(aliases=['setpre'])
#     @commands.has_permissions(administrator=True)
#     async def setprefix(self, ctx, new_prefix):
#         await client.db.execute('UPDATE guilds SET prefix = $1 WHERE guild_id = $2', new_prefix, ctx.guild.id)
#         await ctx.send("Prefix Updated")


# def setup(bot):
#     bot.add_cog(prefix(bot))
