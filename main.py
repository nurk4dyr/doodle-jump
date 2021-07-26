import pygame
import settings
import random

from player import Player
from platform import Platform


# Init and Setup pygame
pygame.init()
pygame.display.set_caption(settings.WINDOW_TITLE)

screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
clock = pygame.time.Clock()
game_loop = True

player = Player()

sprites = pygame.sprite.Group()
sprites.add(player)

# Adding 7 platform with random positions to sprites group
for index in range(7):
    x = random.randint(0, settings.WINDOW_WIDTH - 100)
    y = random.randint(0, settings.WINDOW_HEIGHT - 20)
    platform = Platform(x, y)

    sprites.add(platform)


while game_loop:
    # SET FRAME UPDATE TIME
    clock.tick(settings.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    # Updating
    sprites.update(player=player)

    # Drawing
    screen.fill(settings.COLOR_GREEN)
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
