import pygame
from pygame.locals import *
import sys
from battleship import *
from bullet import *

SCREEN_WIDTH = 800
SCREEN_HIGHT = 600

def event_handler(ship, bullets):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                ship.move_right = True
            elif event.key == K_LEFT:
               ship.move_left = True
            elif event.key == K_UP:
                ship.move_up = True
            elif event.key == K_DOWN:
                ship.move_down = True
            elif event.key == K_SPACE:
                new_b = Bullet(ship)
                bullets.append(new_b)
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                ship.move_right = False
            elif event.key == K_LEFT:
               ship.move_left = False
            elif event.key == K_UP:
                ship.move_up = False
            elif event.key == K_DOWN:
                ship.move_down = False

def update(ship, bullets):
    ship.update()
    for b in bullets:
        if b.removed == True:
            bullets.remove(b)
        else:
            b.update()

def refresh_screen(screen, bg, ship, bullets):
    screen.blit(bg, (0,0))
    ship.draw_ship()
    for b in bullets:
        b.draw_bullet()
    pygame.display.update()

def run_game():
    bullets = []
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
    pygame.display.set_caption('My Game')
    bg = pygame.image.load('space.jpg').convert_alpha()
    ship = Battleship()
    while True:

        event_handler(ship, bullets)
        update(ship, bullets)
        refresh_screen(screen, bg, ship, bullets)

run_game()
