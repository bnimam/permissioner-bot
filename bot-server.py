"""The main running script of the Permissioner-Bot"""
import discord
import configparser

creds = configparser.ConfigParser()
creds.read('.config')

TOKEN = creds['credentials']['token']

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
