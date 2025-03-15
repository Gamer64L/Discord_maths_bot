import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import flask
from threading import Thread

# Inicializa Flask (para mantener Render activo)
app = flask.Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!", 200  

def run_flask():
    port = int(os.environ.get("PORT", 8080))  
    app.run(host="0.0.0.0", port=port)

Thread(target=run_flask).start()

# Cargar el token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Definir intents y prefijo del bot
intents = discord.Intents.default()
intents.message_content = True  # Asegura que el bot pueda leer mensajes

bot = commands.Bot(command_prefix="!", intents=intents)  # Ahora usa "!" como prefijo

@bot.event
async def on_ready():
    print(f'✅ Conectado como {bot.user}')

# Comandos del bot
@bot.command(name='suma')
async def sumar(ctx, num1: int, num2: int):
    response = f'Tu resultado de la suma es = {num1 + num2}'
    await ctx.send(response)

@bot.command(name='resta')
async def restar(ctx, num1: int, num2: int):
    response = f'Tu resultado de la resta es = {num1 - num2}'
    await ctx.send(response)

@bot.command(name='multiplicar')
async def multiplicar(ctx, num1: int, num2: int):
    response = f'Tu resultado de la multiplicación es = {num1 * num2}'
    await ctx.send(response)

@bot.command(name='dividir')
async def dividir(ctx, num1: int, num2: int):
    if num2 == 0:
        response = "❌ No se puede dividir entre 0."
    else:
        response = f'Tu resultado de la división es = {num1 / num2}'
    await ctx.send(response)

bot.run(DISCORD_TOKEN)
