import pygame

class Scoreboard:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.score = 0

    def update(self, delta):
        self.score += delta

    def draw(self, screen):
        text = self.font.render(f"Score: {int(self.score)}", True, "white")
        screen.blit(text, (10, 10))
