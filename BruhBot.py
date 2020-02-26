import discord
from discord.utils import find
from discord.ext import commands
import random 
import sys
import time


prefix = '$'
TOKEN = 'thetoken'
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')

#Events
#Ready comformation
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('{}help'.format(prefix)))
    print('Bot online')

#Guild join message
@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send("Hello {0}! I am BruhBot and my prefix is '{1}'!".format(guild.name, prefix))

#Ping
@client.command(pass_context=True)
async def ping(ctx):
    try:
        await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    except:
        await ctx.send("This command didn't work.")
        TimeoutError  
        
#Hello
@client.command(pass_context=True, aliases=['hi'])
async def hello(ctx):
    try:
        await ctx.send('{0.author.mention}, die twat.'.format(ctx))
    except:
        await ctx.send("This command didn't work.")
        TimeoutError

#Coin
@client.command(pass_context=True, aliases=['5050','coinflip', 'flip'])
async def coin(ctx):
    try:
        responses=['Heads','Tails']
        await ctx.send(f"It's {random.choice(responses)}!")
    except:
        await ctx.send("This command didn't work.")
        TimeoutError

#Join
@client.command(pass_context=True)
async def join(ctx): 
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    except:
        await ctx.send("This command didn't work.")
        TimeoutError

#Disconnect
@client.command(pass_context=True)
async def leave(ctx):
    try:
        channel = ctx.author.voice.channel
        voice_client = client.voice_client_in(channel)
        await channel.disconnect()
        await ctx.send('I have left')
    except:
        await ctx.send("This command didn't work.")
        TimeoutError

#Poggers
@client.command(pass_context=True, aliases=['pogger'])
async def poggers(ctx):
    try:
        await ctx.send('https://www.pngkit.com/png/full/149-1491764_view-pogger-pogchamp-emote.png')
    except:
        await ctx.send("This command didn't work.")
        TimeoutError

#Shutdown
@client.command(pass_context=True)
async def shutdown(ctx):
    try:
        await ctx.send('Bot shutting down')
        sys.exit()
    except:
        await ctx.send("This command didn't work.")
        TimeoutError

#Help
@client.command(pass_context=True)
async def help(ctx):
    try:
        msg="""```Prefix is {0}!
Commands:
    help          Displays all commands
    ping          Displays ping
    hello         Gives you a friendly hello
    coin          Flips a coin
    join          Joins a call
    leave         Leaves a call
    poggers       Displays god
    shutdown      Shuts down the bot```""".format(prefix)
        await ctx.send(msg)
    except:
        await ctx.send("This command didn't work.")
        TimeoutError  


client.run(TOKEN)
