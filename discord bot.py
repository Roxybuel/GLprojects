import random
import discord
from discord.ext import commands
import requests
from dbotapi import API_KEY

# stores my apikey in a different file
TOKEN = API_KEY

bot = commands.Bot(command_prefix="#")

# defines the funny messages
funny_messages = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I'm reading a book on the history of glue... I just can't seem to put it down!",
    "Why do chicken coops only have two doors? Because if they had four, they'd be a chicken sedan!",
    "I used to play piano by ear, but now I use my hands.",
    "What's the best thing about Switzerland? I don't know, but their flag is a huge plus!",
    "Why don’t oysters share their pearls? Because they’re shellfish!",
]


# helps me know if my bot is online or in the server
@bot.event
async def on_ready():
    print(f'{bot.user} successfully logged in!')


# the things I want my bot to do
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # type'#hi' to get a reaction and a start-up for something else
    if message.content == "#hi":
        await message.add_reaction('😶‍🌫️')
        await message.channel.send("Ready for a weird joke?...")

    # type '#weird' to get a funny picture
    if message.content.startswith('#weird'):
        with open('Funny meme.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
        return

    # type '#nice' to get a different funny picture
    if message.content.startswith('#nice'):
        with open('Funny meme2.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
        return

    # type '#cat' to get a random picture of a cat every time
    if message.content == "#cat":
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        data = response.json()
        image_url = data[0]['url']
        embed = discord.Embed(title="Random Cat Image", color=0xff00ff)
        embed.set_image(url=image_url)
        await message.channel.send(embed=embed)

    if message.channel.name == 'general' and not message.author.bot:
        await message.channel.send(random.choice(funny_messages))


# runs code
bot.run(TOKEN)
