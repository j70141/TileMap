import random
import pygame, sys
from pygame.locals import *
from xml.dom import minidom

class TileSet():
    def __init__(self, filename="tileset.png", tilesize=32, tilecolumns=32, tilerows=16):
        self.filename = filename                # future use?
        self.tilesize = int(tilesize)
        self.tilecolumns = int(tilecolumns)
        self.tilerows = int(tilerows)
        self.tileset = []

        # create an indexed tileset list
        for y in range(self.tilerows):
            for x in range(self.tilecolumns):
                self.tileset.append(pygame.Rect( x * self.tilesize, y * self.tilesize, self.tilesize, self.tilesize))
                
    def tile(self, tilenum = 0):
        return self.tileset[tilenum]

class MapSet():
    def __init__(self, filename="map.xml"):

        # open map file and parse the XML data; height, width, and map data
        doc = minidom.parse(filename)
        self.width = int(doc.getElementsByTagName("layer")[0].getAttribute("width"))
        self.height = int(doc.getElementsByTagName("layer")[0].getAttribute("height"))

        # grab map values and split/convert to integer array; get childNodes[0].nodeValue
        strMap = doc.getElementsByTagName("layer")[0].getElementsByTagName("data")[0].firstChild.data
        self.map = [int(x.strip()) for x in strMap.split(',')]

# Timer Clock; Game Speed Set
fpsClock = pygame.time.Clock()

# Dictionary of Common Tiles/Sprites
tilevalue = {
    "PLAYER"   : 284,
    "PLAYER_1" : 364,
    "PLAYER_2" : 365,
    "PLAYER_3" : 366,
    "PLAYER_4" : 367
}

# initiate TileSet Sprite Class
tileset = TileSet()

# initiate MapSet Data Class
mapset = MapSet()

# game dimensions
TILESIZE  = tileset.tilesize
MAPWIDTH  = mapset.width
MAPHEIGHT = mapset.height

Px = 8
Py = 8
player = 364

# set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
SHEET = pygame.image.load('tileset.png').convert()

while True:
    # get user events
    for event in pygame.event.get():
        print(event)
        print(pygame.QUIT)
        print(pygame.K_RIGHT)
        # check if user wants to quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif (event.type == KEYDOWN and event.key == K_RIGHT ):
            Px += 1
        elif (event.type == KEYDOWN and event.key == K_LEFT ):
            Px -= 1
        elif (event.type == KEYDOWN and event.key == K_UP ):
            Py -= 1
        elif (event.type == KEYDOWN and event.key == K_DOWN ):
            Py += 1

    for y in range(MAPHEIGHT):
        for x in range(MAPWIDTH):
            # Grab and Print the Tile from the TileSet that Corresponds to the INT value of the MapSet:  TILE[MAP#]
            DISPLAYSURF.blit(SHEET, ( x * TILESIZE, y * TILESIZE), tileset.tile(mapset.map[y * MAPWIDTH + x]-1))

    #Px += random.randrange(3) - 1
    #Py += random.randrange(3) - 1

    if Px < 0: Px = 0
    if Px >= MAPWIDTH: Px = MAPWIDTH - 1
    if Py < 0: Py = 0
    if Py >= MAPHEIGHT: Py = MAPHEIGHT - 1

    player += 1
    if (player > 335): player = 332

    DISPLAYSURF.blit(SHEET, ( Px * TILESIZE, Py * TILESIZE), tileset.tile(player))
    pygame.display.update()
    fpsClock.tick(5)