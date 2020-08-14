# File Name: scraper.py
# Author: Stephen Montes De Oca
# Email: deocapaul@gmail.com

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

VILLAGERS_CSV = "CSV/villagers.csv"
BUGS_CSV = "CSV/bugs.csv"
FISH_CSV = "CSV/fish.csv"
SEACREATURES_CSV = "CSV/seacreatures.csv"
ART_CSV = "CSV/art.csv"

COMMA = ','
NEWLINE = '\n'
EMPTY_STRING = ''
NOT_AVAILAVLE = 'N/A'


def getVillagerList():
    # creating a CSV file to store all villagers
    f = open(VILLAGERS_CSV, "w")

    # formatting csv file
    csv_headers = "name,photo_url,personality,species,catch_phrase\n"
    f.write(csv_headers)

    # link to scrape from
    url = 'https://animalcrossing.fandom.com/wiki/Villager_list_(New_Horizons)'

    # getting html source code from url
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    # parsing html source code with a Beautiful Soup object
    page_soup = soup(page_html, "html.parser")

    # retrieving all table rows
    villagers = page_soup.findAll("tr")

    # extracting each villager's attributes from each table entry
    for i in range(len(villagers)):
        # skipping first 5 table row elements in result set (not villagers)
        if i < 5:
            continue

        # retrieving table row with villager
        villager = villagers[i]

        # extracting each attribute of villager from table row contents
        contents = villager.contents

        name = contents[1].a.text
        photo_url = contents[2].a['href']
        personality = contents[3].a['title']
        species = contents[4].a.text
        catch_phrase = contents[6].i.text

        # writing to CSV file
        f.write(name + COMMA)
        f.write(photo_url + COMMA)
        f.write(personality + COMMA)
        f.write(species + COMMA)
        f.write(catch_phrase)
        f.write(NEWLINE)

    f.close()


def getBugList():
        # creating a CSV file to store all bugs
    f = open(BUGS_CSV, "w")

    # formatting csv file
    csv_headers = 'name,image,price,location\n'
    f.write(csv_headers)

    # link to scrape from
    url = 'https://animalcrossing.fandom.com/wiki/Bugs_(New_Horizons)'

    # parsing html source code from url
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, 'html.parser')

    # table containing the bug entries of Northern Hemisphere
    tables = page_soup.findAll('table', {'class': 'roundy'})

    north_bugs = tables[1]
    north_bugs = north_bugs.table
    bugs = north_bugs.contents

    # iterating over each fish (table row entries)
    for i in range(3, len(bugs), 2):
        bug = bugs[i]
        bug_properties = bug.contents

        name = bug_properties[1].a.text
        image = bug_properties[2].a['href']
        price = bug_properties[3].text
        location = bug_properties[4].text

        # cleaning up strings
        price = price.replace(NEWLINE, EMPTY_STRING)
        price = price.strip()
        price = price.replace(COMMA, EMPTY_STRING)
        location = location.replace(NEWLINE, EMPTY_STRING)
        location = location.strip()

        # writing to csv file
        f.write(name + COMMA)
        f.write(image + COMMA)
        f.write(price + COMMA)
        f.write(location)
        f.write(NEWLINE)

    f.close()


def getFishList():
    # creating a CSV file to store all fishes
    f = open(FISH_CSV, "w")

    # formatting csv file
    csv_headers = 'name,image,price,location\n'
    f.write(csv_headers)

    # link to scrape from
    url = 'https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons)#Northern%20Hemisphere'

    # parsing html source code from url
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, 'html.parser')

    # extracting tables and searching for entries
    tables = page_soup.findAll('table', {'class': 'roundy'})

    # table containing the fish entries of Northern Hemisphere
    north_fish = tables[1]
    north_fish = north_fish.table
    fishes = north_fish.contents

    # iterating over each fish (table row entries)
    for i in range(3, len(fishes), 2):
        fish = fishes[i]
        fish_properties = fish.contents

        name = fish_properties[1].a.text
        image = fish_properties[2].a['href']
        price = fish_properties[3].text
        location = fish_properties[4].text

        # cleaning up strings
        price = price.replace(NEWLINE, EMPTY_STRING)
        price = price.strip()
        price = price.replace(COMMA, EMPTY_STRING)
        location = location.replace(NEWLINE, EMPTY_STRING)
        location = location.strip()
        # writing to csv file
        f.write(name + COMMA)
        f.write(image + COMMA)
        f.write(price + COMMA)
        f.write(location)
        f.write(NEWLINE)

    f.close()


def getSeaCreaturesList():
    # creating a csv file to store deep sea creatures list
    f = open(SEACREATURES_CSV, 'w')

    # formatting csv file
    csv_headers = 'name,image,price\n'
    f.write(csv_headers)

    # link to scrape from
    url = 'https://animalcrossing.fandom.com/wiki/Deep-sea_creatures_(New_Horizons)'

    # parsing html source code from url
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, 'html.parser')

    # extracting table from html and searching for entries
    tables = page_soup.findAll('table', {'class': 'roundy'})

    # table containing the sea creature entries are from Northern Hemisphere
    north_sea = tables[3]
    north_sea = north_sea.table
    sea_creatures = north_sea.contents

    # iterating over each sea creature
    for i in range(3, len(sea_creatures), 2):
        sea_creature = sea_creatures[i]
        sea_creature_props = sea_creature.contents

        name = sea_creature_props[1].a.text
        image = sea_creature_props[2].a['href']
        price = sea_creature_props[3].text

        # cleaning up strings
        price = price.replace(NEWLINE, EMPTY_STRING)
        price = price.strip()
        price = price.replace(COMMA, EMPTY_STRING)

        # writing to csv
        f.write(name + COMMA)
        f.write(image + COMMA)
        f.write(price)
        f.write(NEWLINE)

    f.close()


def getArtList():
    # creating a csv to store art work list
    f = open(ART_CSV, 'w')

    # formatting csv file
    f.write("name,forgery,genuine\n")

    # link for html source code
    url = 'https://animalcrossing.fandom.com/wiki/Art_(New_Horizons)'

    # parsing html source code
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, 'html.parser')

    # extracting tables from html and searching for entries
    tables = page_soup.findAll('table', {'class': 'wikitable'})

    # iterating over each tables (paintings and scultures)
    for table in tables:
        table_contents = table.contents

        for i in range(3, len(table_contents), 2):
            art = table_contents[i]
            art_properties = art.contents

            name = art_properties[1].a.text
            forgery = ''
            genuine = art_properties[3].a['href']

            try:
                forgery = art_properties[2].a['href']
            except:
                forgery = NOT_AVAILAVLE

            # writing to csv file
            f.write(name + COMMA)
            f.write(forgery + COMMA)
            f.write(genuine)
            f.write(NEWLINE)

    f.close()


if __name__ == '__main__':
    getVillagerList()
    getFishList()
    getBugList()
    getSeaCreaturesList()
    getArtList()
