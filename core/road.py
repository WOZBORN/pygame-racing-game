import pygame
from .settings import ROAD_SPRITE, SCREEN_HEIGHT, SCREEN_WIDTH


class Road:
    def __init__(self):
        self.image = pygame.image.load(ROAD_SPRITE)
        self.segment_height = self.image.get_height()

        # Начальные позиции трёх сегментов
        self.y1 = SCREEN_HEIGHT - self.segment_height
        self.y2 = self.y1 - self.segment_height
        self.y3 = self.y2 - self.segment_height

    def update(self, speed):
        self.y1 += speed
        self.y2 += speed
        self.y3 += speed

        # Перезапуск сегментов при уходе за экран
        if self.y1 >= SCREEN_HEIGHT:
            self.y1 = self.y3 - self.segment_height  # Перезапускаем в верхнем положении
        if self.y2 >= SCREEN_HEIGHT:
            self.y2 = self.y1 - self.segment_height
        if self.y3 >= SCREEN_HEIGHT:
            self.y3 = self.y2 - self.segment_height

    def draw(self, screen):
        x_position = SCREEN_WIDTH // 2 - self.image.get_width() // 2
        screen.blit(self.image, (x_position, self.y1))
        screen.blit(self.image, (x_position, self.y2))
        screen.blit(self.image, (x_position, self.y3))
