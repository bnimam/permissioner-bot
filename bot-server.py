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
async def perm(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('!perm'):
        #q = ''.join(msg.content.replace('!perm', '').split(' '))
        rnd = random.randint(0, 3)

        if rnd == 0:
            reply = f"@{msg.author} Permission granted!"
        elif rnd == 1:
            reply = f"@{msg.author} Permission denied!"
        else:
            reply = f"@{msg.author} Don't ask me, ask @PERMISSIONER !"

        await msg.channel.send(reply)

client.run(TOKEN)
