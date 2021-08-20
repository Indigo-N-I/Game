import pygame
import random
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

if __name__ == "__main__":
    # main game loop
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Platformer")



    # game loop
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()
