from inspect import getinnerframes
from re import X
from urllib.parse import quote_plus
import discord
from discord import member
from discord import channel
from discord.abc import GuildChannel
from discord.client import Client
from discord.errors import Forbidden
from discord.ext import commands
import random
from discord.ext.commands.converter import MessageConverter
import time as kais
from discord.ext.commands.errors import BotMissingPermissions, MissingPermissions, MissingRequiredArgument


from requests import api
from requests.models import Response
#TOKEN
client = commands.Bot(command_prefix='=')
with open('token.txt') as f:
    contents= f.read()
token = contents


moistid = '278858104056315904'
#LOG IN
@client.event
async def on_ready():
    print(f'---------------------------------------------\nlogged in as {client.user}\n---------------------------------------------\nDeveloper: Moist water\n---------------------------------------------')
    await client.change_presence(activity=discord.Game(name='my prefix is = | mmmYes. cat'))
    
#LATENCY
@client.command()
async def ping(ctx):
    await ctx.send(f'```Pong! {round(client.latency*1000)}ms```')

#8 BALL
@client.command(aliases=['8ball'])
async def eightball(message,*,question):
    responses = [
        'yes',
        'no',
        'perhaps',
        'defenietly lol',
        'probably?'
    ]
    await message.send(f'Question: {question}\n\nAnswer: {random.choice(responses)}')

#RETARDOMETER    
@client.command(aliases=['retardometer','Retardometer'])
async def RetardoMeter(ctx,*,question):
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
@RetardoMeter.error
async def retarderror(ctx,error:MissingRequiredArgument):
    hundredperc= '101%'
    await ctx.send(f'pretty sure youre atleast {hundredperc} retarded since u forgot the arguement\n```=retardometer <persons name>```')


#GET GUILDS 
@client.command()
async def getguild(ctx):
    x=0
    if str(ctx.message.author.id) == moistid:
        await ctx.send('lol check your terminal :wink:')
        async for guild in client.fetch_guilds(limit=None):
            guild_list = guild.name
            x+=1
            print(f'{x}- {guild_list}')
    else:
        await ctx.send('this is an admin only command. :japanese_goblin:')

#DELETE MESSAGES
@client.command()
@commands.has_permissions(administrator=True)
async def purge(ctx,amount=2):
    await ctx.channel.purge(limit=amount)
    if True:
        channel = client.get_channel(ctx.channel.id)
        embed = discord.Embed(
            title=f"{ctx.author.name} cleared messages from: {ctx.channel.name}",
            description=f"{amount} messages were deleted",
            colour=0x71368a,
        )
        await channel.send(embed=embed)
@purge.error
async def purgeerror(ctx,error:MissingPermissions):
    await ctx.send('you dont have the permissions. idiot')

#KICK MEMBERS
@client.command()
async def kick(ctx,member:discord.Member,*,reason=None):
    await member.kick(reason=reason)
    if True:
        embedd = discord.Embed(title=f'{member} kicked',description=f'reason: {reason}',color=0x71368a)
        await ctx.send(embed=embedd)
@kick.error
async def kickerror(ctx,error:Forbidden):
    await ctx.send('what :smiling_imp:')

#ROULETTE
@client.command()
async def roulette(ctx,person):
    with open('response.txt') as resp:
        cntnt = resp.readlines()
    await ctx.send(f'{person} {random.choice(cntnt)}')

#ECHO
@client.command()
async def say(ctx,*,message=None):
    await ctx.message.delete()
    await ctx.send(f'```{message}```')

#TOTAL MEMBERS  
@client.command()
async def members(ctx):
    membercount = (ctx.guild.member_count)
    await ctx.send(f'```Number of members in the server {membercount}```')

    
#ROULETTE ERROR
@roulette.error
async def rouletteerror(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send(f'SPECIFY A PERSONS NAME RETARD AJSDJAKS WAHTS WRONG W YOU??\n```=roulette <persons name>``` ')
#GET CHATS
@client.command()
async def chats(ctx, channel:discord.TextChannel=None):
    numofchats = 0
    with open('chatsgif.txt','r') as gif1:
        gif1cnt = gif1.readlines()
    channel = ctx.channel
    await ctx.send('**THINKING.....\n This will take some time depending on the number of messages in your server**')
    await ctx.send(random.choice(gif1cnt))
    async for chats in channel.history(limit=None):
        numofchats += 1
    await ctx.send(f'```Done!!\nthere are {numofchats} messages in {ctx.channel.name}```')


#MESSAGE EDIT NOTIF
@client.event
async def on_message_edit(before,after):
    guild = (client.get_guild)
    channel = (client.get_channel)
    embed = discord.Embed(title=f'{before.author} edited a message',description=f'before:\n{before.content}')
    embed.add_field(name=f'after: ',value=f'{after.content}',inline=False)
    #await before.channel.send(embed=embed)
    print(f'\n{before.author} edited a message in {before.guild} channel:({   before.channel})\nbefore: "{before.content}"\nafter: "{after.content}"')

#RANDOM GIF IN TEXT FILE
@client.command()
async def randgif(ctx):
    with open('chatsgifs.txt','r') as randgiff:
        contentOfRandGif = randgiff.readlines()
    await ctx.send('ok')
    kais.sleep(1)
    await ctx.send(random.choice(contentOfRandGif))

#SUB STATS
@client.command()
async def guilds(ctx):
    guilds = 0
    async for guild in client.fetch_guilds(limit=None):
        guild_list = guild.name
        guilds +=1
    await ctx.send(f'Number of servers im in: {guilds}')  

client.run(token)
    


