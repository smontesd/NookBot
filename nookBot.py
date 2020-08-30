# File Name: nookBot.py
# Author: Stephen Montes De Oca
# Email: deocastephen@gmail.com

import csv
import discord
import math
from discord.ext import commands

# Constants
BOT_PREFIX = '!'
BOT_TOKEN = 'BOT TOKEN HERE'
VILLAGERS_CSV = 'CSV/villagers.csv'
FISH_CSV = 'CSV/fish.csv'
SEACREATURES_CSV = 'CSV/seacreatures.csv'
BUGS_CSV = 'CSV/bugs.csv'
ART_CSV = 'CSV/art.csv'
NONE_FOUND = 'Dictionary has not been initialized'
NOT_FOUND = 'Request could not be found, perhaps check spelling'
INVALID_LIST = 'Invalid request. List options are: villagers, artwork, fishes, bugs, seacreatures'

# initialzing lists
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


# defining bot commands
@bot.command(name="villager",
             description="Displays villager name, species, phrase, personality, and a photo",
             brief='Usage example: !villager "Tia"')
async def get_villager(ctx, arg):
    if len(villagers) == 0:
        await ctx.send(NONE_FOUND)
        return

    arg_lower = arg.lower()

    for villager in villagers:
        if arg_lower != villager['name'].lower():
            continue

        embedVar = discord.Embed(title=villager['name'],
                                 colour=0xffb500)
        embedVar.set_thumbnail(url=villager['photo_url'])
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

    arg_lower = arg.lower()

    for art in artwork:
        if arg.lower() != art['name'].lower():
            continue

        embedForgery = discord.Embed(title=art['name'],
                                     description='Forgery',
                                     colour=0xff1b00)
        embedGenuine = discord.Embed(title=art['name'],
                                     description='Genuine',
                                     colour=0x00ff00)

        embedGenuine.set_thumbnail(url=art['genuine'])
        await ctx.send(embed=embedGenuine)

        if art['forgery'] != 'N/A':
            embedForgery.set_thumbnail(url=art['forgery'])
            await ctx.send(embed=embedForgery)
        return

    await ctx.send(NOT_FOUND)


@bot.command(name="seacreature",
             description="Displays sea creature name, photo, and price",
             brief='Usage example: !seacreature "Sea grapes"')
async def get_seacreature(ctx, arg):
    if len(seacreatures) == 0:
        await ctx.send(NONE_FOUND)
        return

    arg_lower = arg.lower()

    for seacreature in seacreatures:
        if arg_lower != seacreature['name'].lower():
            continue

        embedVar = discord.Embed(title=seacreature['name'],
                                 description=(
                                     'Price: ' + seacreature['price']),
                                 colour=0x0020ff)
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

    arg_lower = arg.lower()

    for bug in bugs:
        if arg_lower != bug['name'].lower():
            continue

        embedVar = discord.Embed(title=bug['name'],
                                 description=('Price: ' + bug['price']),
                                 colour=0x059200)
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

    arg_lower = arg.lower()

    for fish in fishes:
        if arg_lower != fish['name'].lower():
            continue

        embedVar = discord.Embed(title=fish['name'],
                                 description=('Price: ' + fish['price']),
                                 colour=0x0095ff)
        embedVar.add_field(name='Location', value=fish['location'])
        embedVar.set_thumbnail(url=fish['image'])
        await ctx.send(embed=embedVar)
        return

    await ctx.send(NOT_FOUND)


@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji != '➡' and reaction.emoji != '⬅':
        print("hello")
        return

    msg = reaction.message
    contents = msg.content

    # splitting message by new lines if in list format
    entries = contents.split('\n')

    if len(entries) <= 1:
        return

    # if in list format the first entry will specify which list is being used
    first_entry = entries[0]
    list_used = []
    message = None

    # checking which option to list
    if (first_entry == 'Villagers'):
        list_used = villagers
        message = "Villagers\n"
    elif (first_entry == 'Fishes'):
        list_used = fishes
        message = "Fishes\n"
    elif (first_entry == 'Sea Creatures'):
        list_used = seacreatures
        message = "Sea Creatures\n"
    elif (first_entry == 'Bugs'):
        list_used = bugs
        message = "Bugs\n"
    elif (first_entry == 'Artwork'):
        list_used = artwork
        message = "Artwork\n"
    else:
        return

    pageCount = math.ceil(len(list_used) / 25)
    if (pageCount == 0):
        return

    # checking for page index
    second_entry = entries[1]
    second_entry = second_entry.split(".")
    pageIndex = math.ceil(int(second_entry[0]) / 25)

    if reaction.emoji == '➡':
        pageIndex += 1
    elif reaction.emoji == '⬅':
        pageIndex -= 1

    # checking if page index is valid
    if pageIndex < 1 or pageIndex > pageCount:
        return

    # printing next page
    start = (pageIndex - 1) * 25
    end = pageIndex * 25

    if pageIndex == pageCount:
        end = len(list_used)

    for i in range(start, end):
        entry = list_used[i]
        message += "{index}. {name}\n".format(
            index=(i + 1), name=entry['name'])

    await msg.edit(content=message)


@ bot.command(name="list",
              description="Outputs a list for a given category: art, bugs, fishes, seacreatures, villagers",
              brief='Usage example: !list "villagers"')
async def list(ctx, arg):
    list_used = []
    arg_lower = arg.lower()
    message = None

    # checking which option to list
    if (arg_lower == 'villagers'):
        list_used = villagers
        message = "Villagers\n"
    elif (arg_lower == 'fishes'):
        list_used = fishes
        message = "Fishes\n"
    elif (arg_lower == 'seacreatures'):
        list_used = seacreatures
        message = "Sea Creatures\n"
    elif (arg_lower == 'bugs'):
        list_used = bugs
        message = "Bugs\n"
    elif (arg_lower == 'artwork'):
        list_used = artwork
        message = "Artwork\n"
    else:
        await ctx.send(INVALID_LIST)
        return

    count = len(list_used)
    if (count == 0):
        await ctx.send(NONE_FOUND)
        return

    msg = await ctx.send("Listing...")
    await msg.add_reaction('⬅')
    await msg.add_reaction('➡')

    # generating list contents
    if (count > 25):
        count = 25

    for i in range(count):
        entry = list_used[i]
        message += "{index}. {name}\n".format(index=(i + 1),
                                              name=entry['name'])

    await msg.edit(content=message)


@ bot.command(name="stop",
              description="Terminates Nook Bot",
              brief="Terminates Nook Bot")
async def log_out(ctx):
    await bot.logout()

bot.run(BOT_TOKEN)
