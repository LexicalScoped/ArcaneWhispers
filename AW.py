import cfg
import asyncio
import database_models
from engine import World
from database_models import Player, Mob, Session
from discord.ext import commands

world = World()

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
    if world.Check_For_Player(ctx.author.id):
        await ctx.send(f'Unable to register {ctx.author.name} - Character for this user already exists.')
        return
    await ctx.send(world.Create_Player(ctx.author.id, ctx.author.name))

@bot.command('rest')
async def rest(ctx):
    if ctx.channel.id != CHANNEL:
        return
    if not world.Check_For_Player(ctx.author.id):
        await ctx.send(f'unable to locate player character for {ctx.author.name}.')
        return
    await ctx.send(world.Player_Rest(ctx.author.id))
  
@bot.command('wake')
async def wake(ctx):
    if ctx.channel.id != CHANNEL:
        return
    if not world.Check_For_Player(ctx.author.id):
        await ctx.send(f'unable to locate player character for {ctx.author.name}.')
        return
    await ctx.send(world.Player_Wake(ctx.author.id))

@bot.command('awake')
async def awake(ctx):
    if ctx.channel.id != CHANNEL:
        return
    names = []
    for player in world.players_awake:
        names.append(player.player_name)
    await ctx.send(names)

def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    main()

