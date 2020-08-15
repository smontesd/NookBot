# File Name: nookBot.py
# Author: Stephen Montes De Oca
# Email: deocapaul@gmail.com

import csv
from discord.ext import commands

# Constants
BOT_PREFIX = '!'
BOT_TOKEN = 'NzQyODQyMTM0MzA1OTY0MDYz.XzL_pg.0djmvnWNdDDECuEMoWqCOyuDvCU'
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
        if arg != villager['name']:
            continue

        await ctx.send('Name: ' + villager['name'])
        await ctx.send(villager['photo_url'])
        await ctx.send('Species: ' + villager['species'])
        await ctx.send('Personality: ' + villager['personality'])
        await ctx.send('Catch phrase: "' + villager['catch_phrase'] + '"')
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
        if arg != art['name']:
            continue

        await ctx.send('Name: ' + art['name'])
        if art['forgery'] == 'N/A':
            await ctx.send('Forgery: N/A')
        else:
            await ctx.send('Forgery:')
            await ctx.send(art['forgery'])

        await ctx.send('Genuine:')
        await ctx.send(art['genuine'])
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
        if arg != seacreature['name']:
            continue

        await ctx.send('Name: ' + seacreature['name'])
        await ctx.send(seacreature['image'])
        await ctx.send('Price: ' + seacreature['price'])
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
        if arg != bug['name']:
            continue

        await ctx.send('Name: ' + bug['name'])
        await ctx.send(bug['image'])
        await ctx.send('Price: ' + bug['price'])
        await ctx.send('Location: ' + bug['location'])
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
        if arg != fish['name']:
            continue

        await ctx.send('Name: ' + fish['name'])
        await ctx.send(fish['image'])
        await ctx.send('Price: ' + fish['price'])
        await ctx.send('Location: ' + fish['location'])
        return

    await ctx.send(NOT_FOUND)


@bot.command(name="stop",
             description="Terminates Nook Bot",
             brief="Terminates Nook Bot")
async def log_out(ctx):
    await bot.logout()

bot.run(BOT_TOKEN)
