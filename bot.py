import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

DATA_FILE = "counter.json"

def load_counter():
    if not os.path.exists(DATA_FILE):
        return {"count": 0}

    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_counter(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

counter_data = load_counter()

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}")

@bot.command()
async def krypat(ctx):
    counter_data["count"] += 1
    save_counter(counter_data)

    await ctx.send(
        f"Krypat oszukal swoich po raz {counter_data['count']}"
    )

TOKEN = os.getenv("TOKEN")

bot.run(TOKEN)
