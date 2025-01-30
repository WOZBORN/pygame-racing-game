import pygame

from settings import SCREEN_HEIGHT
from settings import PLAYER_SPEED, PLAYER_LANES, PLAYER_MIN_SPEED, PLAYER_MAX_SPEED, PLAYER_SPRITE

class Player:
    def __init__(self):
        self.image = pygame.image.load(PLAYER_SPRITE)
        self.rect = self.image.get_rect(bottomleft=(PLAYER_LANES[1], SCREEN_HEIGHT-150))
        self.speed = PLAYER_SPEED
        self.lane_index = 1

    def move(self, direction):
        if direction == "left" and self.lane_index > 0:
            self.lane_index -= 1
        elif direction == "right" and self.lane_index < len(PLAYER_LANES) - 1:
            self.lane_index += 1
        self.rect.x = PLAYER_LANES[self.lane_index]

    def adjust_speed(self, delta):
        self.speed = max(PLAYER_MIN_SPEED, min(PLAYER_MAX_SPEED, self.speed + delta))

    def update(self):
        pass  # Игрок движется только по полосам

    def draw(self, screen):
        screen.blit(self.image, self.rect)
