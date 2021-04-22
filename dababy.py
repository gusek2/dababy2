import discord

from discord.ext import commands

client = commands.Bot(command_prefix= 'dababy.')
# dababy.help

#words
letsgo_words = ['lets go', 'lessgo', 'lessgoo','lesssgooo', 'letsgoo', 'lesgoo','lesssgo']
answer_words = [ 'сосешь?','ты пидорас?','гей','пидарас','хуесос','еблан','долбаёб','влад','глеб','пидор','пидар','сосни',]

@client.event

async def on_ready():
    print('LETS GOOO')
@client.command(pass_content = True)

@client.event

async def letsgo(ctx) :
    author = ctx.message.author

    await ctx.send( f' {author.mention} LESSS GOOO')

@client.event

async def on_message(message):
    msg = message.content.lower()
    if msg in letsgo_words:
        await message.channel.send('LESSS GOOOO')

@client.event

async def on_message(message):
    msg = message.content.lower()
    if msg in answer_words:
         await message.channel.send('кто как обзывается тот так и называется')
         await message.channel.send('https://allya.ru/wp-content/uploads/2020/02/dababy-1.jpg')

@client.event

async def on_message(message):
    msg = message.content.lower()
    if msg == 'пососи':
        await message.channel.send('https://www.youtube.com/watch?v=Vq_9cTepBWA')
#connect

token = 'ODM0NzIwMDIxOTQ2Njk1NzAw.YIE_mQ.R6V_izgRQmfX-Wnj9CuHBv5HLBY'

client.run(token)
