import pygame, sys
from pygame.locals import *
from PIL import Image
from enum import Enum # Can use Enum instead of some other things

# constants representing colors
BLACK = (  0,   0,   0)
BROWN = (153,  76,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# constants represeint the different resources
DIRT  = 0
GRASS = 1
WATER = 2
COAL  = 3

# dictionary represting our tilemap
colors = {
    DIRT  : BROWN,
    GRASS : GREEN,
    WATER : BLUE,
    COAL  : BLACK
}

# list representing tilemap
tilemap = [
    [ GRASS, COAL,  DIRT ],
    [ WATER, WATER, GRASS],
    [ COAL,  GRASS, WATER],
    [ DIRT,  GRASS, COAL ],
    [ GRASS, WATER, DIRT ],
]

map = ( "14,14,14,13,13,13,12,6,6,6,6,7,9,11,11,11,"
        "14,14,13,13,13,13,16,6,6,6,6,6,9,11,11,11,"
        "14,13,13,13,12,16,6,6,6,6,6,6,7,9,11,11,"
        "13,13,24,12,16,6,6,6,6,6,6,6,6,7,9,11,"
        "12,12,16,6,6,6,6,6,6,6,6,6,6,6,7,9,"
        "16,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,"
        "6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,"
        "6,6,6,6,6,6,6,6,6,6,6,6,44,109,6,6,"
        "6,6,6,6,6,6,6,6,6,6,112,98,98,105,6,6,"
        "6,6,6,6,6,6,6,6,6,6,6,6,6,97,6,6,"
        "6,6,6,6,6,6,6,6,6,6,6,6,6,97,6,6,"
        "6,6,6,6,6,6,6,6,6,6,6,6,6,107,6,6,"
        "6,6,6,6,6,6,6,6,162,6,6,6,6,97,6,17,"
        "6,6,6,21,6,6,51,51,51,51,51,51,51,97,51,51,"
        "6,6,6,6,6,55,3,3,3,3,3,3,3,3,3,3,"
        "6,6,6,6,50,72,290,3,3,3,3,3,3,3,3,3")

tiles = {
    DIRT  : pygame.Rect(225,0,32,32),
    GRASS : pygame.Rect(161,0,32,32),
    WATER : pygame.Rect(33,0,32,32),
    COAL  : pygame.Rect(385,0,32,32)
}

# game dimensions
TILESIZE  = 32
MAPWIDTH  =  3
MAPHEIGHT =  5

# set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
SHEET = pygame.image.load('tileset.png').convert()

while True:
    # get user events
    for event in pygame.event.get():
 
        # check if user wants to quit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                DISPLAYSURF.blit(SHEET, (column*TILESIZE, row*TILESIZE), tiles[tilemap[row][column]])
        
        pygame.display.update()