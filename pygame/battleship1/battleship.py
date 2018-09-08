import pygame
from pygame.locals import *
import sys

SHIP_SPEED = 10


class Battleship():
    def __init__(self):
        ''' initiate the battleship '''
        # get current screen surface and screen size
        self.screen = pygame.display.get_surface()
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        # load spaceship picture, get the rect
        self.image = pygame.image.load('ship1.png').convert_alpha()
        self.rect = self.image.get_rect()
        # put the ship at the bottom_middle of the screen
        self.rect.centerx = self.screen_width / 2
        self.rect.bottom = self.screen_height
        # set the moving flags
        self.move_right = False
        self.move_left = False


    def update(self):
        ''' Move the ship (change its rect) according to moving flags'''
        pass
        
            
    def draw_ship(self):
        ''' draw the ship according to its current position'''
        pass
