import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.all() # Syntax required when intents are active.
bot = commands.Bot(command_prefix="!", help_command=None, intents=intents) 

TOKEN = "TOKEN HERE"

@bot.event
async def on_ready():
    print(bot.user.name)
    print('Bot Start!')
    game = nextcord.Game('Activity')
    await bot.change_presence(status=nextcord.Status.online, activity=game)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(TOKEN)
