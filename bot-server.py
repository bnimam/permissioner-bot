"""The main running script of the Permissioner-Bot"""
import discord
from discord.ext import commands
import configparser
import random

creds = configparser.ConfigParser()
creds.read('.config')

TOKEN = creds['credentials']['token']

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def perm(ctx):
    if ctx.author == client.user:
        return

    #q = ''.join(ctx.content.replace('!perm', '').split(' '))
    rnd = random.randint(0, 3)

    if rnd == 0:
        reply = f"{ctx.message.author.mention()} Permission granted!"
    elif rnd == 1:
        reply = f"{ctx.message.author.mention()} Permission denied!"
    else:
        reply = f"{ctx.message.author.mention()} Don't ask me, ask <@!PERMISSIONER>!"

    await ctx.channel.send(reply)

client.run(TOKEN)
