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
@commands.has_permissions(mute_members=True)
async def mute(ctx, self, member: discord.Member, *, reason=None):
    await member.mute(reason=reason)
    await ctx.send(f'User {member} has been muted.')
    
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, self, anything: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {anything} has been banned.')


# RUN
client.run(os.environ['DISCORD_TOKEN'])
