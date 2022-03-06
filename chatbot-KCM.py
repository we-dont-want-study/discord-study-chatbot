import discord
from discord.ext import commands
import os
import time

def main():
    prefix = '!'
    intents = discord.Intents.all()

    client = commands.Bot(command_prefix=prefix, intents=intents)
    
    @client.command(name='이름')
    
    async def _이름(ctx):
        await ctx.send("hi" + ctx.author.name + "!")
    
    @client.command(name='서버')

    async def _서버(ctx):
        await ctx.send("저 살아있어요..!")

    @client.command(name='시간')
    
    async def _시간(ctx):
        now = time.localtime()
        await ctx.send("현재 시간은 %02d월 %02d일 %02d:%02d:%02d 입니다아!"%(now.tm_mon, now.tm_day, now.tm_hour, now.tm_min, now.tm_sec))

    with open('token.txt', 'r') as f:
        token=f.read()
    client.run(token)
    

if __name__ == '__main__':
    main()