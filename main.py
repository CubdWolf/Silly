import os
from dotenv import load_dotenv
import discord
from discord import app_commands


load_dotenv(dotenv_path="token.env")
token = os.environ["token"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f"logged in as {client.user}")



client.run(token)