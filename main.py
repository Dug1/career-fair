import pygame, sys, os
from floor import *

from random import choice
#from pygame.local import *
from pygame.image import load

SCREEN_DIM = (700, 800)

floor_tile = pygame.image.load("images/floor/floor_tile.png")
person_limit = 30
tile_size = 16

#loading image files

persons_images = [(load("images/" + directory + "/front.png"), load("images/" + directory + "/back.png"), load("images/" + directory + "/left.png"), load("images/" + directory + "/left.png")) for directory in os.listdir("images") if "person" in directory]

pygame.init()
surface =  pygame.display.set_mode(SCREEN_DIM)
clock = pygame.time.Clock()
floor = Floor(SCREEN_DIM, floor_tile)

#make stands 

#generate random people

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    time_passed = clock.tick(30)

    #reapply the background
    floor.flash_background(surface)
    pygame.display.flip()



