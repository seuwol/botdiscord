import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print('등장!!')
    
    @bot.command()
    async def 안녕하세요(ctx):
        await ctx.send('반갑다냥.!!')
        await ctx.send('공지사항 읽고 자기소개 부탁한다냥!')

    @bot.command()
    async def 심심해(ctx):
        await ctx.send('나랑 놀쟈!')

    @bot.command()
    async def 안녕(ctx):
        await ctx.send('안냥')

    @bot.command()
    async def 안냥(ctx):
        await ctx.send('반가워~!')






    @bot.command()
    async def 바보(ctx):
        await ctx.send('너가 더 바보다냥')

    @bot.command()
    async def 멍멍(ctx):
        await ctx.send('야옹~!')

    @bot.command()
    async def ㅂㅂ(ctx):
        await ctx.send('잘가라냥')

    @bot.command()
    async def 안녕히주무세요(ctx):
        await ctx.send('잘가라냥~! 좋은꿈 꿔라냥')

    @bot.command()
    async def 사랑해(ctx):
        await ctx.send('내가 더 사랑한다냥~!❤')

    @bot.command()
    async def 냥드야(ctx):
        await ctx.send('왜부르냥~??')

    @bot.command()
    async def 냥드(ctx):
        await ctx.send('왜부르냥~??')

    @bot.command()
    async def 냥드야사랑해(ctx):
        await ctx.send('주인님 저도 사랑해요❤❤')

    @bot.command()
    async def 냥드야잘가(ctx):
        await ctx.send('주인님 뱌뱌❤')

    @bot.command()
    async def 냥드야인사해(ctx):
        await ctx.send('반갑다냥')

    @bot.command()
    async def 좋은아침(ctx):
        await ctx.send('좋은아침이다냥~!!')

    @bot.command()
    async def 하트뿅뿅(ctx):
        await ctx.send('땨랑해~!❤❤')

    @bot.command()
    async def 앙누(ctx):
        await ctx.send('앙누~~❤')

    @bot.command()
    async def 헿(ctx):
        await ctx.send('흐ㅔ헤헤헿❤')


bot.run('NjkyNTgzNjE0MDU5MjQ5Njg0.XnxCfA.EUYmn0t3W87tZutET8WnZrWSfHE')

