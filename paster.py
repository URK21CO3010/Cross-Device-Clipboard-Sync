import discord
import pyperclip
import configparser

config = configparser.ConfigParser()
config.read('details.ini')

client_token = config['discord']['client_token']

bot = discord.Client(intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Ready")

@bot.event
async def on_message(msg):
    pyperclip.copy(msg.content)

bot.run(client_token)
