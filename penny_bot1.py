from urllib.parse import quote_plus
import discord
from discord.client import Client
from discord.ext import commands
import random
import COVID19Py
#INSTANCES
covid19 = COVID19Py.COVID19()
client = commands.Bot(command_prefix='=')

token = 'ODQyMTY0MDYyNzYyMDQxMzc0.YJxUZw.s1hedY7N0Tw62mTSSgDCcDa9f0c'


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
        await ctx.send(f'wtaf {question} is {percentnaeesh}% Retarded')
    elif percentnaeesh <= 10:
        new_question = str(question)
        upper_question = new_question.upper()
        await ctx.send(f'LESSSGOOOO {upper_question} IS {percentnaeesh}% Retarded')
    else:
        await ctx.send(f'{question} is {percentnaeesh}% Retarded')


@client.command()
async def getguild(ctx):
    x=0
    await ctx.send('**list of servers im in:**')
    async for guild in client.fetch_guilds(limit=10):
        guild_list = guild.name
        x+=1
        await ctx.send(f'```{x}) {guild_list}```')
@client.command()
async def covidinfo(ctx):
    info = covid19.getLatest
    print(info)
client.run(token)
