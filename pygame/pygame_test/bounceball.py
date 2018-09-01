import pygame
from pygame.locals import *
import sys

width = 640
height = 480
screen_size = (width, height)
speed = [2,2]

pygame.init()
screen = pygame.display.set_mode(screen_size)

ball = pygame.image.load('ball.jpeg')
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill((255,255,255))
    screen.blit(ball,ballrect)
    pygame.display.update()
