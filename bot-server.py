"""The main running script of the Permissioner-Bot"""

import configparser
import random
import praw

from discord.ext import commands
from discord import Embed

from interact import run

CBOT = run()

creds = configparser.ConfigParser()
creds.read('.config')

TOKEN = creds['credentials']['token']

client = commands.Bot(command_prefix='!')

reddit = praw.Reddit(client_id=creds['reddit_creds']['client_id'],
                     client_secret=creds['reddit_creds']['secret'],
                     user_agent='permissioner-bot')


@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'ID: {client.user.id}')
    print('------')


@client.command()
async def perm(ctx):
    if ctx.author == client.user:
        return

    if ctx.message.guild is None:
        await ctx.channel.send("This is not the proper way to ask me")
        return

    roles = ctx.message.guild.roles
    pm_role = None
    for r in roles:
        if r.name == 'permiisoner':
            pm_role = r

    rnd = random.randint(0, 3)
    if rnd == 0:
        reply = f"{ctx.message.author.mention} Permission granted!"
    elif rnd == 1:
        reply = f"{ctx.message.author.mention} Permission denied!"
    elif pm_role is not None:
        reply = f"{ctx.message.author.mention} Don't ask me! Ask {pm_role.mention}!"
    else:
        reply = f"{ctx.message.author.mention} Don't ask me! Ask someone more important!"

    await ctx.channel.send(reply)
    return


@client.command()
async def q(ctx):
    if ctx.author == client.user:
        return

    if ctx.message.guild is None:
        await ctx.channel.send("This is not the proper way to ask me")
        return

    reply = f"{ctx.message.author.mention} " + CBOT.process_text(ctx.message.content)

    await ctx.channel.send(reply)
    return


@client.command()
async def memepls(ctx):
    if ctx.author == client.user:
        return

    if ctx.message.guild is None:
        await ctx.channel.send("This is not the proper way to ask me")
        return

    subreddits = ['DeepFriedMemes', 'dankmemes', 'bonehurtingjuice', 'meirl']
    chosen_sub = random.choice(subreddits)

    subreddit = reddit.subreddit(chosen_sub)

    posts = subreddit.hot(limit=100)
    urls = [p.url for p in posts if any(['.jpg', '.png', '.gif', 'jpeg'])]

    picked_url = random.choice(urls)

    e = Embed()
    e.set_image(url=picked_url)

    reply = f"{ctx.message.author.mention} subreddit: {chosen_sub}"
    await ctx.channel.send(reply, embed=e)
    return

client.run(TOKEN)
