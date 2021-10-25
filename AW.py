import cfg
import asyncio
import database_models
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
        await ctx.send(f'Unable to register {ctx.author.name} - User may already have character.')
        return
    try:
        session = Session()
        player = Player(ctx.author.id, ctx.author.name)
        session.add(player)
        session.commit()
        await ctx.send(f'{ctx.author.name} has registered a character')
        session.close()
    except:
        print(f'Something went horribly wrong with character registration!')

def Check_For_Player(pid):
    try:
        session = Session()
        if session.query(Player).filter(Player.player_id==pid).first():
            session.close()
            return True
        else:
            session.close()
            return False
    except:
        print(f'Something went wrong with the character check')

def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    main()

