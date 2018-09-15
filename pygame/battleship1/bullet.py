import pygame
BULLET_SPEED = 5
BULLET_OFFSET = 20

class Bullet(pygame.sprite.Sprite):
    def __init__(self,ship):
        # call father class __init__()
        super().__init__()
        ## load image, get rect
        self.image = pygame.image.load('bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        # set starting place
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top + BULLET_OFFSET

    def update(self):
        # When out of boarder, remove
        if self.rect.bottom <= 0:
            self.kill()
        else:
            self.rect.bottom = self.rect.bottom - BULLET_SPEED
            
