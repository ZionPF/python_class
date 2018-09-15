import pygame
import random

ENEMY_SPEED = 2

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        # call father cass init function
        super().__init__()
        # get game surface screen
        self.screen = pygame.display.get_surface()
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        # Load enemy picture, get rect
        self.image = pygame.image.load('enemy1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        # init enemy place: top of the screen, random x

        self.rect.left = random.randrange(0, self.screen_width - self.rect.width)
        self.rect.bottom = 0


    def update(self):
        ## update enemy status
        # is out of boarder, remove this enemy
        if self.rect.top >= self.screen_height:
            self.kill()
        else:
            self.rect.bottom = self.rect.bottom + ENEMY_SPEED

