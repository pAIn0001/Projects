from discord.ext import commands

import discord

from discord.ext.commands import BucketType


class helpcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    @commands.cooldown(2, 30, BucketType.user)
    async def help(self, ctx):
        em = discord.Embed(title="HELP", description="Use $help <command> for more information.", color=0xFF5733)
        em.add_field(name="miscellaneous",
                     value="changeprefix | vote | ping | Link | serverinfo | membercount | calculator",
                     inline=False)
        em.add_field(name="Moderation", value="clear | mute | unmute | warn | kick | ban | unban ", inline=False)
        em.add_field(name="Fun", value="meme | toss | tictactoe | simp | gay | pp | eightball", inline=False)
        em.add_field(name="Giveaways", value=" giveaway | reroll ", inline=False)
        em.add_field(name="Music",
                     value="join | leave | play | pause | resume | loop | queue | skip | remove | stop | volume "
                           "| nowplaying ",
                     inline=False)

        em.add_field(name="Still facing problem", value="**[Madent's official server](https://discord.gg/auz4kdK8Bq)**",
                     inline=False)

        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def kick(self, ctx):
        em = discord.Embed(title="Kick", description="Kicks a member from the server.", color=0xFF5733)
        em.add_field(name="Syntax", value="$kick @anyone123 [reason]")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def calculator(self, ctx):
        em = discord.Embed(title="Calculator", description="Starts a calculator", color=0xFF5733)
        em.add_field(name="Syntax", value="`$calculator`, `$calc`, `$maths`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def eightball(self, ctx):
        em = discord.Embed(title="Eightball", description="Plays Eightball with You", color=0xFF5733)
        em.add_field(name="ALiases", value="$eightball, $8ball, $8b")
        em.add_field(name="Syntax", value="$eightball `question`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def serverinfo(self, ctx):
        em = discord.Embed(title="Serverinfo", description="Tells you about the guild", color=0xFF5733)
        em.add_field(name="Syntax", value="$serverinfo")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def membercount(self, ctx):
        em = discord.Embed(title="Membercount", description="Tells you the number of members present in the guild",
                           color=0xFF5733)
        em.add_field(name="Syntax", value="$membercount")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def link(self, ctx):
        em = discord.Embed(title="link", description="Sends the link of the all popular sites.", color=0xFF5733)
        em.add_field(name="Syntax", value="$link")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def clear(self, ctx):
        em = discord.Embed(title="Clear", description="clears the message send on that channel", color=0xFF5733)
        em.add_field(name="Syntax", value="$clear [value]")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def warn(self, ctx):
        em = discord.Embed(title="Warn", description="Warns the member on that server", color=0xFF5733)
        em.add_field(name="Syntax", value="$warn @anyone123 [reason]")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def mute(self, ctx):
        em = discord.Embed(title="Mute", description="Mutes a member from the server", color=0xFF5733)
        em.add_field(name="Syntax", value="$mute @anyone123 [reason]")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def unmute(self, ctx):
        em = discord.Embed(title="Unmute", description="Unmutes a muted member ", color=0xFF5733)
        em.add_field(name="Syntax", value="$unmute @anyone123")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def ban(self, ctx):
        em = discord.Embed(title="Ban", description="Bans a member from the guild", color=0xFF5733)
        em.add_field(name="Syntax", value="$ban @anyone123 [reason]")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def unban(self, ctx):
        em = discord.Embed(title="Unban", description="Unbans a member from the guild")
        em.add_field(name="Syntax", value="$unban @anyone123#9876 ")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def changeprefix(self, ctx):
        em = discord.Embed(title="Changeprefix", description="Changes the bot prefix for the server", color=0xFF5733)
        em.add_field(name="Syntax", value="$changeprefix [new prefix]")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def vote(self, ctx):
        em = discord.Embed(title="Vote", description="Gives you the voting link for the bot", color=0xFF5733)
        em.add_field(name="Syntax", value="$vote")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def meme(self, ctx):
        em = discord.Embed(title="Meme", description="Gives you a fresh meme", color=0xFF5733)
        em.add_field(name="Syntax", value="$meme")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def giveaway(self, ctx):
        em = discord.Embed(title="Giveaway",
                           description="First you need to make a role called <Giveaways> then give it to all those "
                                       "you want after. After triggering the command bot will start the giveaway",
                           color=0xFF5733)
        em.add_field(name="Syntax", value="$giveaway")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def ping(self, ctx):
        em = discord.Embed(title="Ping", description="Tells the bot's latency", color=0xFF5733)
        em.add_field(name="Syntax", value="$ping")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def toss(self, ctx):
        em = discord.Embed(title="Coinflip", description="Flips a coin and tells wether its a head or tails.",
                           color=0xFF5733)
        em.add_field(name="Syntax", value="$toss")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def tictactoe(self, ctx):
        em = discord.Embed(title="TicTacToe", description="Starts a tictactoe match between two players.",
                           color=0xFF5733)
        em.add_field(name="Syntax",
                     value="`$tictactoe @player1 @player 2` and to place use $place [block no.] `$place 5`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def gay(self, ctx):
        em = discord.Embed(title="Gay", description="Tells the author's gayrate", color=0xFF5733)
        em.add_field(name="Syntax", value="$gay")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def simp(self, ctx):
        em = discord.Embed(title="Simp", description="Tells the simprate of the author", color=0xFF5733)
        em.add_field(name="Syntax", value="$simp")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def pp(self, ctx):
        em = discord.Embed(title="PP", description="Tells the author's penis size", color=0xFF5733)
        em.add_field(name="Syntax", value="`$pp`")
        await ctx.send(embed=em)

        #########################################################################################

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def join(self, ctx):
        em = discord.Embed(title="Join", description="Makes the bot to join VC", color=0xFF5733)
        em.add_field(name="Syntax", value="`$join`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def leave(self, ctx):
        em = discord.Embed(title="Leave", description="Makes the bot to leave the VC", color=0xFF5733)
        em.add_field(name="Syntax", value="`$leave`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def play(self, ctx):
        em = discord.Embed(title="Play", description="Plays the song", color=0xFF5733)
        em.add_field(name="Syntax", value="`$play [song name]` or `$play [song link]`")
        em.add_field(name="Example", value=f"`$play lofi`\n`$play https://youtube.com/watch?v=saxcDfvZf`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def pause(self, ctx):
        em = discord.Embed(title="Pause", description="Pauses the song", color=0xFF5733)
        em.add_field(name="Syntax", value="`$pause`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def resume(self, ctx):
        em = discord.Embed(title="Resume", description="Resumes the song", color=0xFF5733)
        em.add_field(name="Syntax", value="`$resume`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def loop(self, ctx):
        em = discord.Embed(title="Loop", description="Loops the current playing song", color=0xFF5733)
        em.add_field(name="Syntax", value="`$loop`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def skip(self, ctx):
        em = discord.Embed(title="Skip", description="Skips the current playing song", color=0xFF5733)
        em.add_field(name="Syntax", value="`$skip`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def queue(self, ctx):
        em = discord.Embed(title="Queue", description="Tells the status of the queue", color=0xFF5733)
        em.add_field(name="Syntax", value="`$queue`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def remove(self, ctx):
        em = discord.Embed(title="Remove", description="Removes the song from the queue", color=0xFF5733)
        em.add_field(name="Syntax", value="`$remove [song no.]`")
        em.add_field(name="Example", value="`$remove 0` this removes the current song \n`$remove 3`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def stop(self, ctx):
        em = discord.Embed(title="Stop", description="Stops the player", color=0xFF5733)
        em.add_field(name="Syntax", value="`$stop`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def nowplaying(self, ctx):
        em = discord.Embed(title="Nowplaying", description="Tells the current playing song", color=0xFF5733)
        em.add_field(name="Syntax", value="`$nowplaying`")
        await ctx.send(embed=em)

    @help.command()
    @commands.cooldown(1, 60, BucketType.user)
    async def volume(self, ctx):
        em = discord.Embed(title="Volume", description="Sets the volume", color=0xFF5733)
        em.add_field(name="Syntax", value="`$volume [volume]`")
        em.add_field(name="Example", value="`#volume 30`")
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(helpcommands(bot))
