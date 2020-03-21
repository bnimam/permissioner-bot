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
        reply = f"{discord.Member(ctx.message.author)} Permission granted!"
    elif rnd == 1:
        reply = f"{discord.Member(ctx.message.author)} Permission denied!"
    else:
        reply = f"{discord.Member(ctx.message.author)} Don't ask me, ask {discord.Member('PERMISSIONER')} !"

    await ctx.channel.send(reply)

client.run(TOKEN)
