import pygame
from pygame.locals import *
import sys

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600

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
        pass
    def draw_ship(self):
        self.screen.blit(self.image, self.rect)
def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type = KEYDOWN:
            if event.key == K_RIGHT:
                ship.move_right = True
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                ship.move_right = False

def update():
    pass

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

        event_handler()
        update()
        refresh_screen(screen, bg, ship)

run_game()
