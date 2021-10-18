import cfg
import asyncio
from discord.ext import commands

TOKEN = cfg.D_TOKEN
GUILD = cfg.D_GUILD
CHANNEL = cfg.D_CHAN

prefix = ">"

bot = commands.Bot(command_prefix=prefix, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# @bot.command('hello')
# async def Hello(ctx):
#     if ctx.channel.id != CHANNEL:
#         return
#     await ctx.send(f'Hello there! I am new here.')

def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    main()

