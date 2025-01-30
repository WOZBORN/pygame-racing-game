import pygame
from . import settings as sets


class Player:
    def __init__(self):
        self.image_original = pygame.image.load(sets.PLAYER_SPRITE).convert_alpha()
        self.image = self.image_original  # Копия изображения для трансформации
        self.width = self.image.get_width()
        self.rect = self.image.get_rect(midtop=(
            sets.PLAYER_LANES[1],
            sets.SCREEN_HEIGHT - 250
        ))
        self.speed = sets.PLAYER_SPEED
        self.lane_index = 1
        self.died = False

        self.target_x = self.rect.centerx  # Целевая координата X
        self.moving = False  # Флаг движения
        self.angle = 0  # Текущий угол поворота

    def move(self, direction):
        """Начинает плавное перемещение в указанную сторону."""
        if self.moving:  # Если уже двигается, не прерываем
            return

        if direction == "left" and self.lane_index > 0:
            self.lane_index -= 1
        elif direction == "right" and self.lane_index < len(sets.PLAYER_LANES) - 1:
            self.lane_index += 1
        else:
            return

        self.target_x = sets.PLAYER_LANES[self.lane_index]  # Назначаем новую цель
        self.moving = True  # Включаем анимацию

    def adjust_speed(self, delta):
        """Регулирует скорость игрока."""
        self.speed = max(sets.PLAYER_MIN_SPEED, min(sets.PLAYER_MAX_SPEED, self.speed + delta))

    def update(self):
        """Обновляет положение игрока и анимирует его движения."""
        if self.died:
            self.rect.y += self.speed
            return

        if self.moving:
            step = 10  # Скорость движения по X

            if abs(self.rect.centerx - self.target_x) < step:
                self.rect.centerx = self.target_x
                self.moving = False  # Достигли цели
                self.angle = 0  # Возвращаем в исходное положение
            else:
                if self.rect.centerx < self.target_x:
                    self.rect.centerx += step
                    self.angle = -15  # Поворот вправо
                else:
                    self.rect.centerx -= step
                    self.angle = 15  # Поворот влево

            # Постепенно возвращаем угол к 0
            if not self.moving:
                self.angle *= 0.9  # Плавное выравнивание

        # Применяем поворот
        self.image = pygame.transform.rotate(self.image_original, self.angle)

    def draw(self, screen):
        """Рисует игрока с учетом поворота."""
        rotated_rect = self.image.get_rect(center=self.rect.center)  # Центрируем повернутый спрайт
        screen.blit(self.image, rotated_rect.topleft)

    def die(self):
        """Обрабатывает смерть игрока."""
        self.image_original = pygame.image.load(sets.PLAYER_SPRITE_DIED).convert_alpha()
        self.image = self.image_original
        self.died = True
