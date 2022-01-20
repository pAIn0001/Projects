"""@tasks.loop(seconds=0.7)

async def votee():
    # print(datetime.now().hour == 15)
    # print("test")
    text_channel = client.get_channel(bid)
    # print(text_channel)
    if text_channel != None:
        # words = ["@everyone ", "cunt", "faggot","pussy","bitch","fuck"]
        # print(x)
        num = ('To access this channel vote us on \n https://top.gg/servers/803518328991514655/vote')

        await text_channel.send(str(num))

        intervals = [1800, 3600]
        await asyncio.sleep(random.choice(intervals))


votee.start()"""

"""@tasks.loop(seconds=0.7)
async def voteer():
    # print(datetime.now().hour == 15)
    # print("test")
    text_channel = client.get_channel(mid)
    # print(text_channel)
    if text_channel != None:
        # words = ["@everyone ", "cunt", "faggot","pussy","bitch","fuck"]
        # print(x)
        num = ('To access this channel vote us on \n https://top.gg/servers/803518328991514655/vote')

        await text_channel.send(str(num))

        intervals = [1800, 3600]
        await asyncio.sleep(random.choice(intervals))


voteer.start()"""