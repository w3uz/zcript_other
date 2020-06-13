import discord
import os
from discord import utils
from discord.ext import commands

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
        
client = commands.Bot(command_prefix= '*')
Clientdiscord = discord.Client()

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked.')
	
@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


# RUN
client.run(os.environ['DISCORD_TOKEN'])
