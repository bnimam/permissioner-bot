"""The main running script of the Permissioner-Bot"""
import discord

creds = {}

with open('.config', 'r') as f:
    for l in f:
        kv = l.split('=')
        creds[kv[0]] = kv[1]

TOKEN = creds['token']

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_messsage(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('!perm'):
        reply = f"Don't ask me, ask @PERMISSIONER !"
        await msg.channel.send(reply)

client.run(TOKEN)
