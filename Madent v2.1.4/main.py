import os
from pathlib import Path
from sqlite3.dbapi2 import Cursor
from flask import Flask, render_template, request
import discord
# import os
import DiscordUtils
import asyncpg
import json
from discord.ext.commands import BucketType
from discord_components import *
import datetime
from discord.ext import commands

# from discord import Member, Embed
# import praw
# import requests
# import re
# import asyncio
import random
# import datetime
# from discord.ext import tasks
# from discord.ext.commands import cog, BucketType

# from discord.ext.commands import BadArgument
# from discord.ext.commands import command, cooldown
# from discord.ext.commands import CommandOnCooldown
# from discord.ext.commands import CommandNotFound
from requests import get
import sqlite3

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")
intents = discord.Intents.all()

client = discord.Client()

client._skip_check = lambda x, y: False
x = True





music = DiscordUtils.Music()
DEFAULT_PREFIX = "$"


# async def create_pool():
#     client.db = await asyncpg.create_pool(database="tutorial", user = "postgres", password = "rehan2006kinggf")
#     print("Connection succesfull to data base")











async def get_prefix(client, message):
    print("HI")
    if not message.guild:
        return commands.when_mentioned_or(DEFAULT_PREFIX)(client, message)
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute(f"SELECT pre FROM main WHERE guild_id={message.guild.id}")
    result = cursor.fetchone()
    if result is None:
        sql = ("INSERT INTO main (guild_id, pre) VALUES (?,?)") 
        val = (message.guild.id, DEFAULT_PREFIX)
        prefix = DEFAULT_PREFIX

        cursor.execute(sql,val)
        db.commit()
        cursor.close()
        db.close()
    else:
        prefix = result[0]

    return commands.when_mentioned_or(prefix)(client, message)
    

client = commands.Bot(command_prefix=get_prefix, intents=intents)
client.remove_command('help')
@client.event
async def on_ready():
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS main(
        guild_id TEXT,
        prefix TEXT
        )
        ''')
    print('Bot is ready.')
    DiscordComponents(client)
    return await client.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"With {len(set(client.users))} users | $help"))


@client.command(aliases=['setpre'])
@commands.has_permissions(administrator=True)
async def setprefix(ctx, new_prefix):
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute("SELECT pre FROM main WHERE guild_id = ?", (ctx.guild.id,))
    result = cursor.fetchone()

    if result:
        sql = ("UPDATE main SET pre = ? WHERE guild_id = ?")
        val = (new_prefix, ctx.guild.id)
        await ctx.send("Prefix Updated")
    if not result:
        sql = "INSERT INTO main(prefix, guild_id) VALUES(?,?)"
        val = (new_prefix, ctx.guild.id)
        await ctx.send("Prefix Inserted")

    cursor.execute(sql,val)
    db.commit()
    cursor.close()
    db.close()
########################################################################################################################
buttons = [
    [
        Button(style=ButtonStyle.grey, label='1'),
        Button(style=ButtonStyle.grey, label='2'),
        Button(style=ButtonStyle.grey, label='3'),
        Button(style=ButtonStyle.blue, label='×'),
        Button(style=ButtonStyle.red, label='Exit')
    ],
    [
        Button(style=ButtonStyle.grey, label='4'),
        Button(style=ButtonStyle.grey, label='5'),
        Button(style=ButtonStyle.grey, label='6'),
        Button(style=ButtonStyle.blue, label='÷'),
        Button(style=ButtonStyle.red, label='←')
    ],
    [
        Button(style=ButtonStyle.grey, label='7'),
        Button(style=ButtonStyle.grey, label='8'),
        Button(style=ButtonStyle.grey, label='9'),
        Button(style=ButtonStyle.blue, label='+'),
        Button(style=ButtonStyle.red, label='Clear')
    ],
    [
        Button(style=ButtonStyle.grey, label='00'),
        Button(style=ButtonStyle.grey, label='0'),
        Button(style=ButtonStyle.grey, label='.'),
        Button(style=ButtonStyle.blue, label='-'),
        Button(style=ButtonStyle.green, label='=')
    ],
]


# calculates answer
def calculate(exp):
    o = exp.replace('×', '*')
    o = o.replace('÷', '/')
    result = ''
    try:
        result = str(eval(o))
    except:
        result = 'An error occurred.'
    return result


@client.command(aliases=['calc', 'maths', 'math'])
@commands.cooldown(1, 60, BucketType.user)
async def calculator(ctx):
    m = await ctx.send(content='Loading Calculators...')
    expression = 'None'
    delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    e = discord.Embed(title=f'{ctx.author.name}\'s calculator | {ctx.author.id}', description=expression,
                      timestamp=delta, colour=ctx.author.color)
    await m.edit(components=buttons, embed=e)
    while m.created_at < delta:
        res = await client.wait_for('button_click')
        if res.author.id == int(res.message.embeds[0].title.split('|')[1]) and res.message.embeds[
            0].timestamp < delta:
            expression = res.message.embeds[0].description
            if expression == 'None' or expression == 'An error occurred.':
                expression = ''
            if res.component.label == 'Exit':
                await res.respond(content='Calculator Closed', type=7)
                break
            elif res.component.label == '←':
                expression = expression[:-1]
            elif res.component.label == 'Clear':
                expression = 'None'
            elif res.component.label == '=':
                expression = calculate(expression)
            else:
                expression += res.component.label
            f = discord.Embed(title=f'{res.author.name}\'s calculator|{res.author.id}', description=expression,
                              timestamp=delta, color=ctx.author.color)
            await res.respond(content='', embed=f, components=buttons, type=7)


########################################################################################################################


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ping(ctx):
    await ctx.send(f':ping_pong:Pong!\n   In {round(client.latency * 1000)}ms '
                   f'<a:pingpongloading:875577854438539294>')



if __name__ == '__main__':
    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            client.load_extension(f"cogs.{file[:-3]}")
# client.loop.run_until_complete(create_pool())
client.run("ODMxMDUyMjk0NzMxODU3OTQw.YHPnww.eEgKpBmoo4J7OeH4G4RMyToI5tM")
