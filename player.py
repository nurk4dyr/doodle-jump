import pygame
import settings


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))
        self.image.fill(settings.COLOR_BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (settings.WINDOW_WIDTH / 2, settings.WINDOW_HEIGHT / 2)

        self.speed = settings.PLAYER_SPEED
        self.gravity = 0
        self.gravity_force = settings.GRAVITY_FORCE

    def is_falls(self):
        return self.gravity > 10

    def update(self, *args, **kwargs):
        keystroke = pygame.key.get_pressed()

        if keystroke[pygame.K_a] or keystroke[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keystroke[pygame.K_d] or keystroke[pygame.K_RIGHT]:
            self.rect.x += self.speed

        self.gravity += self.gravity_force
        self.rect.y += self.gravity

        if self.rect.left > settings.WINDOW_WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = settings.WINDOW_WIDTH
