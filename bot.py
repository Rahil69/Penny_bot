from urllib.parse import quote_plus
import discord
from discord import member
from discord.client import Client
from discord.ext import commands
import random

#TOKEN
client = commands.Bot(command_prefix='=')
with open('token.txt') as f:
    contents= f.read()
token = contents


#LOG IN
@client.event
async def on_ready():
    print(f'logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name='use  =help | gm'))
    
#LATENCY
@client.command()
async def ping(ctx):
    await ctx.send(f'```Pong! {round(client.latency*1000)}ms```')

#8 BALL
@client.command(aliases=['8ball'])
async def eightball(ctx,*,question):
    responses = [
        'yes',
        'no',
        'perhaps',
        'defenietly lol',
        'probably?'
    ]
    await ctx.send(f'Question: {question}\n\nAnswer: {random.choice(responses)}')

#RETARDOMETER    
@client.command(aliases=['retardometer','Retardometer'])
async def RetardoMeter(ctx,question):
    percentnaeesh = round(random.uniform(1,101))
    if percentnaeesh == 100:
        await ctx.send(f'congratulations {question} {percentnaeesh}% Retarded')
    elif percentnaeesh == 101:
        await ctx.send(f'Bruh. {question} is {percentnaeesh}% Retarded')
    elif percentnaeesh <= 10:
        new_question = str(question)
        upper_question = new_question.upper()
        await ctx.send(f'LESSSGOOOO {upper_question} IS {percentnaeesh}% Retarded')
    else:
        await ctx.send(f'{question} is {percentnaeesh}% Retarded')

#GET GUILDS 
@client.command()
async def getguild(ctx):
    x=0
    await ctx.send('**list of servers im in:**')
    async for guild in client.fetch_guilds(limit=10):
        guild_list = guild.name
        x+=1
        await ctx.send(f'```{x}) {guild_list}```')

#DELETE MESSAGES
@client.command()
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit=amount)
    if True:
        channel = client.get_channel(ctx.channel.id)
        embed = discord.Embed(
            title=f"{ctx.author.name} cleared: {ctx.channel.name}",
            description=f"{amount} messages were deleted",
            colour=0x71368a,
        )
        await channel.send(embed=embed)

#KICK MEMBERS
@client.command()
async def kick(ctx,member:discord.Member,*,reason=None):
    await member.kick(reason=reason)
    if True:
        embedd = discord.Embed(title=f'{member} kicked',description=f'reason: {reason}',color=0x71368a)
        await ctx.send(embed=embedd)

client.run(token)
