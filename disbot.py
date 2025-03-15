import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#Credenciales
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix='!',intents=intents)

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

bot.run(TOKEN)
