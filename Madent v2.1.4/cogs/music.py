import DiscordUtils
from discord.ext.commands import BucketType
from discord.ext import commands
import discord
import youtube_dl


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    music = DiscordUtils.Music()

    # async def search_song(self, amount, song, get_url=False):
    #     info = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet" : True}).extract_info(f"ytsearch{amount}:{song}", download=False, ie_key="YoutubeSearch"))
    #     if len(info["entries"]) == 0: return None
    #
    #     return [entry["webpage_url"] for entry in info["entries"]] if get_url else info

    @commands.command()
    @commands.cooldown(3, 100, BucketType.guild)
    async def join(self, ctx):
        voicetrue = ctx.author.voice
        if voicetrue is None:
            return await ctx.send(">>> Currently You are not in a voice channel \n Connect to a voice channel first.")

        await ctx.author.voice.channel.connect()
        em = discord.Embed(title="Madent-o-Player", description="Joined your voice channel", color=ctx.author.color)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(3, 100, BucketType.guild)
    async def leave(self, ctx):
        voicetrue = ctx.author.voice
        mevoicetrue = ctx.guild.me.voice
        if voicetrue is None:
            return await ctx.send(
                ">>> Currently You are not in a voice channel \nConnect to a voice channel first to use this command.")
        if mevoicetrue is None:
            return await ctx.send(
                ">>> Currently I am  not in voice channel \nConnect me to a voice channel to use this command.")
        player = self.music.get_player(guild_id=ctx.guild.id)
        if player:
            player.delete()
        await ctx.voice_client.disconnect()
        em = discord.Embed(title="Madent-o-player", description="Left your voice channel", color=ctx.author.color)
        await ctx.send(embed=em)

    # @commands.command()
    # async def search(self, ctx, *, song=None):
    #     if song is None:
    #         await ctx.send("You forgot to include a song to search for.")
    #
    #     await ctx.send("Searching for song, this may take a few seconds.")
    #
    #     info = await self.search_song(5, song)
    #
    #     embed = discord.Embed(title=f"Results for '{song}':",
    #                           description="*You can use these URL's to play an exact song if the "
    #                                       "one you want isn't the first result.*\n",
    #                           colour=discord.Colour.red())
    #
    #     amount = 0
    #     for entry in info["entries"]:
    #         embed.description += f"[{entry['title']}]({entry['webpage_url']})\n"
    #         amount += 1
    #
    #     embed.set_footer(text=f"Displaying the first {amount} results.")
    #     await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(3, 100, BucketType.guild)
    async def play(self, ctx, *, url):
        player = self.music.get_player(guild_id=ctx.guild.id)
        if not player:
            player = self.music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True)
            song = await player.play()
            em = discord.Embed(title="Madent-o-Player", description=f"I have started playing `{song.name}`",
                               color=ctx.author.color)
            await ctx.send(embed=em)
        else:
            song = await player.queue(url, search=True)
            em = discord.Embed(title="Madent-o-Player", description=f"`{song.name}` has been added to playlist",
                               color=ctx.author.color)
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(4, 60, BucketType.guild)
    async def queue(self, ctx):
        player = self.music.get_player(guild_id=ctx.guild.id)
        embed = discord.Embed(title="Madent-o-Player",
                              description=f"`{', '.join([song.name for song in player.current_queue()])}`",
                              color=ctx.author.color)
        await ctx.send(embed=embed)
        if len(player.current_queue()) == 0:
            em = discord.Embed(title="Madent-o-Player", description="There is nothing is Queue", color=ctx.author.color)
            await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(4, 60, BucketType.guild)
    async def pause(self, ctx):
        player = self.music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        embed = discord.Embed(title="Madent-o-Player",
                              description=f"Paused `{song.name}` <:gxplayer:875706020465377290>",
                              colour=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(4, 60, BucketType.guild)
    async def resume(self, ctx):
        player = self.music.get_player(guild_id=ctx.guild.id)
        song = await player.resume()
        embed = discord.Embed(title="Madent-o-Player", description=f"Resumed `{song.name}` <:pause:875705292099309589>",
                              colour=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command(aliases=['np'])
    @commands.cooldown(3, 60, BucketType.guild)
    async def nowplaying(self, ctx):
        player = self.music.get_player(guild_id=ctx.guild.id)
        song = player.now_playing()
        embed = discord.Embed(title="Madent-o-Player", description=f"**Now Playing**\n`{song.name}` ",
                              colour=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(4, 60, BucketType.guild)
    async def skip(self, ctx):
        player = self.music.get_player(guild_id=ctx.guild.id)
        song = await player.skip()
        embed = discord.Embed(title="Madent-o-Player", description=":track_next: Skipped to the next song ",
                              colour=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(4, 60, BucketType.guild)
    async def loop(self, ctx):
        player = self.music.get_player(guild_id=ctx.guild.id)
        song = await player.toggle_song_loop()
        embed = discord.Embed(title="Madent-o-Player", description=f"`{song.name}`is looping :loop: ",
                              colour=ctx.author.color)
        embed1 = discord.Embed(title="Madent-o-Player", description=f"`{song.name}`is not looping :loop: ",
                               colour=ctx.author.color)
        if song.is_looping:
            return await ctx.send(embed=embed)
        else:
            return await ctx.send(embed=embed1)

    @commands.command()
    @commands.cooldown(3, 60, BucketType.guild)
    async def remove(self, ctx, index):
        player = self.music.get_player(guild_id=ctx.guild.id)
        song = await player.remove_from_queue(int(index))
        embed = discord.Embed(title="Madent-o-Player", description=f"`{song.name}` has been removed from the queue",
                              colour=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(5, 60, BucketType.guild)
    async def volume(self, ctx, vol):
        player = self.music.get_player(guild_id=ctx.guild.id)
        song, volume = await player.change_volume(float(vol) / 100)  # volume should be a float between 0 to 1
        em = discord.Embed(title="Madent-o-Player",
                           description=f"Changed volume for `{song.name}` to `{volume * 100}%`",
                           color=ctx.author.color)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(5, 60, BucketType.guild)
    async def stop(self, ctx):
        player = self.music.get_player(guild_id=ctx.guild.id)
        await player.stop()
        await ctx.send("**Stopped**")


def setup(bot):
    bot.add_cog(music(bot))
