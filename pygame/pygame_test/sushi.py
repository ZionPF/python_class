import pygame
from pygame.locals import *
import sys

width = 640
height = 480
screen_size = (width, height)
speed = [2,2]

pygame.init()
screen = pygame.display.set_mode(screen_size)

plate = pygame.image.load('sushiplate.jpeg').convert()
fish = pygame.image.load('fish.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    xpos, ypos = pygame.mouse.get_pos()
    xpos = xpos - fish.get_width()/2
    ypos = ypos - fish.get_height()/2

    #screen.blit(plate, (0,0))
    screen.blit(fish,(xpos,ypos))

    pygame.display.update()
