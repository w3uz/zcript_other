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
	
#The below code bans player.
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#The below code unbans player.
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, amount=None):
    await ctx.channel.purge(limit=int(amount))
    await ctx.channel.send('(amount) Сообщений было удалено')

@client.command(aliases=['roll'])
async def _roll(ctx, number:int):
	num = random.randint(0,random.randint(0,number))
	await ctx.send(f'Вам выпало: {num}')
	
# RUN
client.run(os.environ['DISCORD_TOKEN'])
