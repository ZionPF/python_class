import pygame
from pygame.locals import *
import sys
from battleship import *

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600

def event_handler(ship):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                ship.move_right = True
            elif event.key == K_LEFT:
               ship.move_left = True
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                ship.move_right = False
            elif event.key == K_LEFT:
               ship.move_left = False

def refresh_screen(screen, bg, ship):
    screen.blit(bg, (0,0))
    ship.draw_ship()
    pygame.display.update()

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
    pygame.display.set_caption('My Game')
    bg = pygame.image.load('space.jpg').convert_alpha()
    ship = Battleship()
    while True:

        event_handler(ship)
        ship.update()
        refresh_screen(screen, bg, ship)

run_game()
