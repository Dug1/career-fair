import pygame, sys, os
from floor import *
from stand import *

from random import choice
from pygame.image import load

SCREEN_DIM = (832, 400)

floor_tile = pygame.image.load("images/floor/floor_tile.png")
stand_left = pygame.image.load("images/stands/stand_left.png")
stand_right =pygame.image.load("images/stands/stand_right.png")
person_limit = 30
tile_size = 16

#loading image files

persons_images = [(load("images/" + directory + "/front.png"), load("images/" + directory + "/back.png"), load("images/" + directory + "/left.png"), load("images/" + directory + "/left.png")) for directory in os.listdir("images") if "person" in directory]

pygame.init()
surface =  pygame.display.set_mode(SCREEN_DIM)
clock = pygame.time.Clock()
floor = Floor(SCREEN_DIM, floor_tile)

#make stands 
def makeStands():
    import pygame
    from pygame import Rect
    tilesize = 16
    width = 2 * tilesize
    height = 3 * tilesize
    intermittentspace = 10 * tilesize
    vspace = 5 * tilesize
    a = []
    x = intermittentspace
    while x <= (width * 3 + intermittentspace * 3):
        #True is left, False is right
        for y in range(vspace + height, vspace + 5 * height + 1, height):
            a.append(Stand(Rect((x, y), (width, height)), True))
        x += width
        for y in range(vspace + height, vspace + 5 * height + 1, height):
            a.append(Stand(Rect((x, y), (width, height)), False))
        x += intermittentspace
    return a

#generate random people

while True: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	time_passed = clock.tick(30)

	#reapply the background
	floor.flash_background(surface)
	for i in range(0, len(stands)):
		surface.blit(stands[i].image, stands[i].rect)
	pygame.display.flip()



