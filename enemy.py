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

if __name__ == "__main__":
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Enemy Testing")

    all_sprites = pygame.sprite.Group()
    e1 = Enemy(200,200)
    all_sprites.add(e1)

    screen.fill((0,0,0))
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        all_sprites.update()
        screen.fill((0,0,0))
        all_sprites.draw(screen)
        pygame.display.flip()
