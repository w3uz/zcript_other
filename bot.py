import requests
import discord
import random
import os
from discord import utils
from discord.ext import commands

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
        
client = commands.Bot(command_prefix= 'z!')
Clientdiscord = discord.Client()
client.remove_command('help')

#кик
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} Был кикнут.')
	
@client.command()
async def ping(ctx):
	await ctx.send(embed=discord.Embed(title='Пинг бота', description= f'Pong! Пинг бота - {round(client.latency * 1000)} ms'))
	
#8балл
@client.command(aliases=['8ball'])
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
	await ctx.send(embed=discord.Embed(title='Помогу решить за тебя', description= f'Вопрос: {question} \n Ответ: {random.choice(responses)}'))
	
#Команда на бан
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#Разбан
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

@client.command(aliases=['roll'])
async def _roll(ctx, number:int):
    num = random.randint(0,random.randint(0, number))
    await ctx.send(embed=discord.Embed(title='Рандом', description= f'Вам выпало число {num}'))
	
#команда info
@client.command(pass_context=True, aliases=['info'])
async def _info(ctx):
	author = ctx.message.author
	
	embed = discord.Embed (
		colour = discord.Colour.red()
	)
	embed=discord.Embed(title="Краткая информация", url="https://discord.gg/AKd63AS", description="Бот сделанный почти полностью в одиночку")
	embed.set_author(name="zcript info", url="https://vk.com/weu_z", icon_url="https://sun9-51.userapi.com/c856032/v856032447/221860/cyThQyAZFdU.jpg")
	embed.set_thumbnail(url="https://media.discordapp.net/attachments/721319431317356609/721770633456910347/image_5.png")
	embed.add_field(name="clear (число)", value="очищает выбранное кол-во сообщений ( нужны права администратора )", inline=True)
	embed.add_field(name="ban (упомянание)", value="блокирует пользователя ( нужны права на блокировку пользователей )", inline=True)
	embed.add_field(name="kick (упомянание)", value="выгоняет пользователя нужны права на исключение пользователей )", inline=True)
	embed.add_field(name="ping", value="Показывает ping бота ( что-то типо скорости соединения )", inline=True)
	embed.add_field(name="roll (число)", value="Выбирает число от 0 до выбранного вами числа", inline=True)
	embed.add_field(name="8ball (вопрос)", value="Помогает решить выбранный вопрос", inline=True)
	embed.add_field(name="dollar", value="Показывает актуальный курс доллара", inline=True)
	embed.add_field(name="case", value="Самые обычные кейсы, может выпасть: Ничего, Личная роль, Личный цвет. Кулдаун 24ч", inline=True)
	embed.set_footer(text="zcript devs: discord.gg/pC8wTaj")
	await author.send(embed=embed)
	
#курс доллара
@client.command()
async def dollar(ctx):
	r = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
	course = r.json()
	course = course['Valute']['USD']['Value'] 
	await ctx.send("Курс доллара: {} рублей".format(course))

@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, amount=None):
    await ctx.channel.purge(limit=int(amount))
    await ctx.send(embed=discord.Embed(title='Удаление сообщений', description= f'Было очищенно {amount} сообщений'))

#кейсы
#@client.command()
#@commands.cooldown(1, 86400, commands.BucketType.user)
#async def case(ctx):
#	responses = [
#	'Ничего',	
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',	
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',	
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',	
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Ничего',
#	'Личная роль на +- 7 дней\nЗа получением этого, напишите в лс овнеру с пруфами',
#	'Личный цвет навсегда\nЗа получением этого, напишите в лс овнеру с пруфами'
#         ]
#	await ctx.send(f'```Вам выпало: {random.choice(responses)}.```')
#
#@case.error
#async def case_error(ctx, error):
#    if isinstance(error, commands.CommandOnCooldown):
#        msg = 'У вас задержка на эту команду. Повторите через {:.2f} секунд'.format(error.retry_after)
#        await ctx.send(msg)
#    else:
#        raise error

@client.command(aliases=['5opka'])
async def _5opka(ctx):
    await ctx.send(f'https://cdn.discordapp.com/attachments/556081968467542039/731073414839795742/video0.mp4')

	
	# RUN
client.run(os.environ['DISCORD_TOKEN'])
