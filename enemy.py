import pygame
import random
from main import SCREEN_WIDTH, SCREEN_HEIGHT
pygame.init()

# creating the enemy(s)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = Pygame.surface((20,20))
        self.rect = self.image.get_rect()

        self.origin_x = x
        self.origin_y = y

        self.rect.x = x
        self.rect.y = y

        self.x_speed = 1
        self.y_speed = 1

    def update(self):
