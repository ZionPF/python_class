import pygame
from pygame.locals import *
import sys

SHIP_SPEED = 10


class Battleship():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()

        self.image = pygame.image.load('spaceship.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_width / 2
        self.rect.bottom = self.screen_height

        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right and self.rect.right < self.screen_width:
            self.rect.centerx += SHIP_SPEED
        elif self.move_left and self.rect.left > 0:
            self.rect.centerx -= SHIP_SPEED
        
            
    def draw_ship(self):
        self.screen.blit(self.image, self.rect)

