import pygame
import settings


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((150, 20))
        self.image.fill(settings.COLOR_BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args, **kwargs):
        player = kwargs["player"]

        if player.rect.colliderect(self.rect) and player.is_falls():
            player.gravity = -10

