import pygame
from main import SCREEN_WIDTH, SCREEN_HEIGHT
pygame.init()


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w = 40, h = 10):
        pygame.sprite.Sprite.__init__(self)

        self.image = Pygame.surface((w,h))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
