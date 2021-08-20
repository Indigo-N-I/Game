import pygame
import random
from enemy import Enemy
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
pygame.init()

if __name__ == "__main__":
    # main game loop
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Platformer")

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
