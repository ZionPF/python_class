import pygame
from pygame.locals import *
import sys

SHIP_SPEED = 10


class Battleship(pygame.sprite.Sprite):
    def __init__(self):
        ''' initiate the battleship '''
        super().__init__()
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
        self.move_up = False
        self.move_down = False


    def update(self):
        ''' Move the ship (change its rect) according to moving flags'''
        if self.move_right and self.rect.right < self.screen_width:
            self.rect.centerx += SHIP_SPEED
        if self.move_left and self.rect.left > 0:
            self.rect.centerx -= SHIP_SPEED
        if self.move_up and self.rect.bottom > 20:
            self.rect.bottom -= SHIP_SPEED
        if self.move_down and self.rect.bottom < self.screen_height:
            self.rect.bottom += SHIP_SPEED
            
    def draw_ship(self):
        ''' draw the ship according to its current position'''
        self.screen.blit(self.image, self.rect)
