import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import flask
from threading import Thread

# Inicializa Flask (para que Render no cierre el servicio)
app = flask.Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!", 200

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# Ejecuta Flask en un hilo separado
Thread(target=run_flask).start()

# Cargar variables de entorno
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Cambia discord.Client a commands.Bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')

# Comandos del bot
@bot.command(name='suma')
async def sumar(ctx, num1: int, num2: int):
    await ctx.send(f'Tu resultado de la suma es = {num1 + num2}')

@bot.command(name='resta')
async def restar(ctx, num1: int, num2: int):
    await ctx.send(f'Tu resultado de la resta es = {num1 - num2}')

@bot.command(name='multiplicar')
async def multiplicar(ctx, num1: int, num2: int):
    await ctx.send(f'Tu resultado de la multiplicación es = {num1 * num2}')

@bot.command(name='dividir')
async def dividir(ctx, num1: int, num2: int):
    if num2 == 0:
        await ctx.send("No se puede dividir entre 0.")
    else:
        await ctx.send(f'Tu resultado de la división es = {num1 / num2}')

bot.run(DISCORD_TOKEN)
