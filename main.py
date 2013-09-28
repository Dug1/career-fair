import pygame, sys, os

from random import choice
from pygame.local import *
from pygame.image import load

SCREEN_DIM = (700, 800)

floor_tile_light = pygame.image.load("/floor_tile_light.png")
floor_tile_dark = pygame.image.load("/floor_tile_dark.png")
person_limit = 30
tile_size = 16

#loading image files

os.chdir("images")
persons_images = [(load(directory + "/front.png"), directory + load("/back.png"),directory + load("/left.png"), directory + load("/left.png")) for directory in os.listdir if "person" in directory]



pygame.init()
surface =  pygame.display.set_mode(SCREEN_DIM)
clock = pygame.time.Clock()
floor = Floor(SCREEN_DIM)

#make stands 

#generate random people

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    time_passed = clock.tick(30)

    #reapply the background
    floor.flash_background(surface)



