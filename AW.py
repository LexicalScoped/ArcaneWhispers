import cfg
import asyncio
import database_models
from engine import Check_For_Player, Create_Player
from database_models import Player, Mob, Session
from discord.ext import commands

TOKEN = cfg.D_TOKEN
GUILD = cfg.D_GUILD
CHANNEL = cfg.D_CHAN

prefix = ">"

bot = commands.Bot(command_prefix=prefix, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command('join')
async def join(ctx):
    if ctx.channel.id != CHANNEL:
        return
    if Check_For_Player(ctx.author.id):
        await ctx.send(f'Unable to register {ctx.author.name} - Character for this user already exists.')
        return
    await ctx.send(Create_Player(ctx.author.id, ctx.author.name))

def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    main()

