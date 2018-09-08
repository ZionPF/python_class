import pygame
from pygame.locals import *
import sys
from battleship import *
from bullet import *

# set the screen height and width
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600

def event_handler():
    ''' handle all the keyboard events'''
    
    for event in pygame.event.get():
        # handle QUIT event, must have
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        

def update():
    '''update everything (ship, bullets, enemies) '''
    # change the objects' position/flag/status
    pass

def refresh_screen():
    ''' draw everything on the screen'''
    pass

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
    pygame.display.set_caption('My Game')
    bg = pygame.image.load('space.jpg').convert_alpha()
    # the main loop of the game:
    while True:
        # handle events:
        event_handler()
        # update everything's status
        update()
        # draw everything
        refresh_screen()

run_game()
