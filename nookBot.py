# File Name: nookBot.py
# Author: Stephen Montes De Oca
# Email: deocapaul@gmail.com

import csv
import discord
from discord.ext import commands

# Constants
BOT_PREFIX = '!'
BOT_TOKEN = 'NzQyODQyMTM0MzA1OTY0MDYz.XzL_pg.vOMLfoTWvW2axi0mx6MX9OUcRaM'
VILLAGERS_CSV = 'CSV/villagers.csv'
FISH_CSV = 'CSV/fish.csv'
SEACREATURES_CSV = 'CSV/seacreatures.csv'
BUGS_CSV = 'CSV/bugs.csv'
ART_CSV = 'CSV/art.csv'
NONE_FOUND = 'Dictionary has not been initialized'
NOT_FOUND = 'Request could not be found, perhaps check spelling'

# initialzing dictionaries
villagers = []
artwork = []
seacreatures = []
bugs = []
fishes = []

# initializing villager list of dictionaries
with open(VILLAGERS_CSV, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        villagers.append(row)

# initialzing artwork list of dictionaries
with open(ART_CSV, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        artwork.append(row)

# initialzing sea creatures list of dictionaries
with open(SEACREATURES_CSV, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        seacreatures.append(row)

# initialzing bugs list of dictionaries
with open(BUGS_CSV, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        bugs.append(row)

# initialzing bugs list of dictionaries
with open(FISH_CSV, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        fishes.append(row)


# creating instance of bot
bot = commands.Bot(command_prefix=BOT_PREFIX)


@bot.command(name="villager",
             description="Displays villager name, species, phrase, personality, and a photo",
             brief='Usage example: !villager "Tia"')
async def get_villager(ctx, arg):
    if len(villagers) == 0:
        await ctx.send(NONE_FOUND)
        return

    for villager in villagers:
        if arg.lower() != villager['name'].lower():
            continue

        embedVar = discord.Embed(title=villager['name'])
        embedVar.set_image(url=villager['photo_url'])
        embedVar.add_field(name='Species',
                           value=villager['species'], inline=True)
        embedVar.add_field(name='Personality',
                           value=villager['personality'], inline=True)
        embedVar.add_field(name='Catch phrase',
                           value=villager['catch_phrase'], inline=True)
        await ctx.send(embed=embedVar)
        return

    await ctx.send(NOT_FOUND)


@bot.command(name="art",
             description='Displays Art work from Red, outputs forgery and genuine',
             brief='Usage example: !art "Ancient statue"')
async def get_art(ctx, arg):
    if len(artwork) == 0:
        await ctx.send(NONE_FOUND)
        return

    for art in artwork:
        if arg.lower() != art['name'].lower():
            continue

        embedForgery = discord.Embed(title=art['name'], description='Forgery')
        embedGenuine = discord.Embed(title=art['name'], description='Genuine')

        if art['forgery'] != 'N/A':
            embedForgery.set_image(url=art['forgery'])
            await ctx.send(embed=embedForgery)

        embedGenuine.set_image(url=art['genuine'])
        await ctx.send(embed=embedGenuine)
        return

    await ctx.send(NOT_FOUND)


@bot.command(name="seacreature",
             description="Displays sea creature name, photo, and price",
             brief='Usage example: !seacreature "Sea grapes"')
async def get_seacreature(ctx, arg):
    if len(seacreatures) == 0:
        await ctx.send(NONE_FOUND)
        return

    for seacreature in seacreatures:
        if arg.lower() != seacreature['name'].lower():
            continue

        embedVar = discord.Embed(title=seacreature['name'],
                                 description=('Price: ' + seacreature['price']))
        embedVar.set_thumbnail(url=seacreature['image'])
        await ctx.send(embed=embedVar)
        return

    await ctx.send(NOT_FOUND)


@bot.command(name="bug",
             description="Displays bug name, photo, price, and location",
             brief='Usage example: !bug "Tiger butterfly"')
async def get_bug(ctx, arg):
    if len(bugs) == 0:
        await ctx.send(NONE_FOUND)
        return

    for bug in bugs:
        if arg.lower() != bug['name'].lower():
            continue

        embedVar = discord.Embed(title=bug['name'],
                                 description=('Price: ' + bug['price']))
        embedVar.add_field(name='Location', value=bug['location'])
        embedVar.set_thumbnail(url=bug['image'])
        await ctx.send(embed=embedVar)
        return

    await ctx.send(NOT_FOUND)


@bot.command(name="fish",
             description="Displays fish name, photo, price, and location",
             brief='Usage example: !fish "Black bass"')
async def get_fish(ctx, arg):
    if len(fishes) == 0:
        await ctx.send(NONE_FOUND)
        return

    for fish in fishes:
        if arg.lower() != fish['name'].lower():
            continue

        embedVar = discord.Embed(title=fish['name'],
                                 description=('Price: ' + fish['price']))
        embedVar.add_field(name='Location', value=fish['location'])
        embedVar.set_thumbnail(url=fish['image'])
        await ctx.send(embed=embedVar)
        return

    await ctx.send(NOT_FOUND)


@bot.command(name="stop",
             description="Terminates Nook Bot",
             brief="Terminates Nook Bot")
async def log_out(ctx):
    await bot.logout()

bot.run(BOT_TOKEN)
