import pygame, sys, os

from random import choice
#from pygame.local import *
#from pygame.image import load

SCREEN_DIM = (700, 800)
person_limit = 30
tile_size = 16 

#loading image files

os.chdir("images")
persons_images = [(load(directory + "/front.png"), directory + load("/back.png"),directory + load("/side.png")) for directory in os.listdir if "person" in directory]


pygame.init()
surface =  pygame.display.set_mode(SCREEN_DIM)
clock = pygame.time.Clock()
floor = Floor(SCREEN_DIM)

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
	while x <= (width * 3 + intermittentspace * 3):																	#True is left, False is right
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



