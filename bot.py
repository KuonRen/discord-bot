import discord
from discord.ext import commands

# Botの設定
TOKEN = "YOUR_BOT_TOKEN"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# 起動時の処理
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# 簡単なコマンド
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm alive!")

# Botを起動
bot.run(TOKEN)
