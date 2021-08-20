import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
pygame.init()


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w = 40, h = 10):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((w,h))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.image.fill((0,0,255))

    def update(self):
        pass
