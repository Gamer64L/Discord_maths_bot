import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import flask
from threading import Thread

# Inicializa Flask (aunque no lo uses realmente)
app = flask.Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!", 200  # Responde con un mensaje para evitar que Render cierre el servicio.

def run_flask():
    port = int(os.environ.get("PORT", 8080))  # Render asigna un puerto dinámico.
    app.run(host="0.0.0.0", port=port)

# Inicia Flask en un hilo separado para que no bloquee el bot.
Thread(target=run_flask).start()

# Tu código del bot de Discord
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {disbot}')
#-----------------------------------------------------------
@bot.command(name='suma')
async def sumar(ctx,num1,num2):
    response = f'Tu resultado de la suma es = {int(num1) + int(num2)}'
    await ctx.send(response)

@bot.command(name='resta')
async def restar(ctx,num1,num2):
    response = f'Tu resultado de la resta es = {int(num1) - int(num2)} '
    await ctx.send(response)

@bot.command(name='multiplicar')
async def restar(ctx,num1,num2):
    response = f'Tu resultado de la multiplicación es = {int(num1) * int(num2)} '
    await ctx.send(response)

@bot.command(name='dividir')
async def restar(ctx,num1,num2):
    response = f'Tu resultado de la división es = {int(num1) / int(num2)} '
    await ctx.send(response)

bot.run(DISCORD_TOKEN)
