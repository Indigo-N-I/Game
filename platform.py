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

if __name__ == "__main__":
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Platform testing")

    all_sprites = pygame.sprite.Group()
    e1 = Platform(200,200)
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
