import discord
import random
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
	
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
	responses = [
	'Это точно.',
	'Это решительно так.',
	'Без сомнения.',
	'Определенно да.',
	'Вы можете положиться на него.',
	'Как я понимаю, да.',
	'Вероятно.',
	'Прогноз хороший.',
	'Да.',
	'Знаки указывают на да.',
	'Ответ смутный, попробуйте еще раз.',
	'Спроси еще раз.',
	'Лучше не говорить тебе сейчас',
	'Не могу предсказать сейчас.',
	'Сконцентрируйся и спроси снова',
	'Не рассчитывай на это',
	'Мой ответ - нет.',
	'Мои источники говорят нет.',
	'Перспектива не очень хорошая.',
	'Очень сомнительно.'     
        ]
	await ctx.send(f'Вопрос: {question}\nОтвет: {random.choice(responses)}')
	
@client.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("Ты не можешь забанить сам себя")
        return
    if reason == None:
        reason = "Потому что клуон!"
    message = f"Ты был забанен в {ctx.guild.name} по причине {reason}"
    await member.send(message)
    # await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} забанен!")

	
# RUN
client.run(os.environ['DISCORD_TOKEN'])
