import pygame



BULLET_SPEED = 5
BULLET_OFFSET = 20


class Bullet():
    def __init__(self,ship):
        self.screen = pygame.display.get_surface()

        self.image = pygame.image.load('bullet.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top + BULLET_OFFSET

        self.removed = False

    def update(self):
        if self.rect.bottom <= 0:
            self.removed = True
        else:
            self.rect.bottom = self.rect.bottom - BULLET_SPEED
            
    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)

