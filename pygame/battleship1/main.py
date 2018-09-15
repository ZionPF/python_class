import pygame
from pygame.locals import *
import sys
from battleship import *
from bullet import *
from enemy import *

# set the screen height and width
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
BULLET_COUNT = 10
ENEMY_INTERVAL = 50

def event_handler(ship, bullet_group):
    ''' handle all the keyboard events'''
    
    for event in pygame.event.get():
        # handle QUIT event, must have
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
                if len(bullet_group) < BULLET_COUNT:
                    new_b = Bullet(ship)
                    bullet_group.add(new_b)
 
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                ship.move_right = False
            elif event.key == K_LEFT:
                ship.move_left = False
            elif event.key == K_UP:
                ship.move_up = False
            elif event.key == K_DOWN:
                ship.move_down = False
        

def update(ship, bullet_group, enemy_group):
    '''update everything (ship, bullets, enemies) '''
    # change the objects' position/flag/status
    for b in bullet_group:
        for e in enemy_group:
            result = pygame.sprite.collide_mask(b,e)
            if result != None:
                b.kill()
                e.kill()
    
    ship.update()
    bullet_group.update()
    enemy_group.update()
    

def refresh_screen(screen, bg, ship, bullet_group, enemy_group):
    ''' draw everything on the screen'''
    screen.blit(bg,(0,0))
    ship.draw_ship()
    bullet_group.draw(screen)
    enemy_group.draw(screen)
    pygame.display.update()

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
    pygame.display.set_caption('My Game')
    bg = pygame.image.load('space.jpg').convert_alpha()
    ship = Battleship()
    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    frame_no = 0
    # the main loop of the game:
    while True:
        # handle events:
        event_handler(ship, bullet_group)
        
        # create enemy every INTERVAL frames:
        if frame_no >= ENEMY_INTERVAL:
            new_e = Enemy()
            enemy_group.add(new_e)
            frame_no = 0
        else:
            frame_no += 1
        
        # update everything's status
        update(ship, bullet_group, enemy_group)
        # draw everything
        refresh_screen(screen, bg, ship, bullet_group, enemy_group)

run_game()
