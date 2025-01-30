import random
import pygame
from .settings import NPC_SPRITES, NPC_SPEED_MIN, NPC_SPEED_MAX, PLAYER_LANES, SCREEN_HEIGHT


class NPC:
    def __init__(self):
        self.image = pygame.image.load(random.choice(NPC_SPRITES))
        self.width = self.image.get_width()
        self.rect = self.image.get_rect(midtop=(
            random.choice(PLAYER_LANES),
            -100
        ))
        self.speed = random.randint(NPC_SPEED_MIN, NPC_SPEED_MAX)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        self.image = pygame.image.load(random.choice(NPC_SPRITES))
        self.rect = self.image.get_rect()
        self.rect.y = -200
        self.rect.centerx = random.choice(PLAYER_LANES)
        self.speed = random.randint(NPC_SPEED_MIN, NPC_SPEED_MAX)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
