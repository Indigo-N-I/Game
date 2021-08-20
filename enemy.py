import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
pygame.init()

# creating the enemy(s)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((20,20))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.x = x
        self.rect.y = y

        self.dist_away = 20

        self.x_speed = 1
        self.y_speed = 1

    def update(self):
        x_dir = random.randint(0, 2)
        y_dir = random.randint(0, 2)

        if x_dir == 0 and self.x - self.rect.x < self.dist_away:
            self.rect.x -= self.x_speed
        elif x_dir == 1 and self.rect.x - self.x < self.dist_away:
            self.rect.x += self.x_speed

        if y_dir == 0 and self.y - self.rect.y < self.dist_away:
            self.rect.y -= self.y_speed
        elif y_dir == 1 and self.rect.y - self.y < self.dist_away:
            self.rect.y += self.y_speed
