import pygame, sys, os
from pygame.local import *
from pygame.image import load

SCREEN_DIM = (700, 800)

floor_tile = pygame.image.load("")

#loading image files


os.chdir("images")
persons_images = [(load(directory + "/front.png"), directory + load("/back.png"),directory + load("/side.png")) for directory in os.listdir if "person" in directory]


pygame.init()
surface =  pygame.display.set_mode(SCREEN_DIM)
clock = pygame.time.Clock()
floor = Floor(SCREEN_DIM)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    time_passed = clock.tick(30)

    #reapply the background


