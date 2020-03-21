"""The main running script of the Permissioner-Bot"""
import configparser
import random

from discord.ext import commands

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

    rnd = random.randint(0, 3)
    roles = ctx.message.guild.roles
    pm_role = None
    for r in roles:
        if r.name == 'PERMISSIONER':
            pm_role = r

    if rnd == 0:
        reply = f"{ctx.message.author.mention} Permission granted!"
    elif rnd == 1:
        reply = f"{ctx.message.author.mention} Permission denied!"
    elif pm_role:
        reply = f"{ctx.message.author.mention} Don't ask me! Ask {pm_role.mention}!"
    else:
        reply = f"{ctx.message.author.mention} Don't ask me! Ask someone more important!"

    await ctx.channel.send(reply)

client.run(TOKEN)
