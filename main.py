import discord
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKENが設定されていません")

# サーバー情報（実際の値に置き換えてください）
VANILLA_IP = "your_vanilla_server_ip"      # 例: "192.168.1.100"
VANILLA_PORT = 25565
FORGE_IP = "your_forge_server_ip"          # 例: "192.168.1.101"
FORGE_PORT = 25565
VANILLA_CHANNEL_ID = 1346129785830772756    # バニラ鯖用チャンネルID（DiscordSRVが送信）
FORGE_CHANNEL_ID = 1346129946304577619      # Forge鯖用チャンネルID（DiscordIntegrationが送信）

# Discord設定
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

# チャンネル名更新関数
async def update_channel(status, channel_id, name_prefix):
    channel = client.get_channel(channel_id)
    if channel:
        if status == "Online":
            await channel.edit(name=f"🟢┃{name_prefix}")
        else:
            await channel.edit(name=f"🔴┃{name_prefix}")

# ボット起動時
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

# メッセージ監視
@client.event
async def on_message(message):
    if message.author.bot:  # ボットからのメッセージのみ監視
        # バニラ鯖（DiscordSRV）のチャンネル
        if message.channel.id == VANILLA_CHANNEL_ID:
            if "Server has started" in message.content:
                await update_channel("Online", VANILLA_CHANNEL_ID, "paper")
            elif "Server has stopped" in message.content:
                await update_channel("Offline", VANILLA_CHANNEL_ID, "paper")
        # Forge鯖（DiscordIntegration）のチャンネル
        elif message.channel.id == FORGE_CHANNEL_ID:
            if "Server started" in message.content:
                await update_channel("Online", FORGE_CHANNEL_ID, "forge")
            elif "Server stopped" in message.content:
                await update_channel("Offline", FORGE_CHANNEL_ID, "forge")

client.run(TOKEN)
