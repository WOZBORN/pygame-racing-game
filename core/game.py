import time
from time import sleep

import pygame
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, NPC_COUNT, TIME_TO_CLOSE
from .player import Player
from .npc import NPC
from .road import Road
from .scoreboard import Scoreboard
from .event_handler import EventHandler


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Racing Game")

        self.clock = pygame.time.Clock()
        self.running = True
        self.game_is_over = False
        self.game_over_time = 0

        self.player = Player()
        self.npcs = [NPC() for _ in range(NPC_COUNT)]
        self.road = Road()
        self.scoreboard = Scoreboard()

    def check_collision(self):
        for npc in self.npcs:
            if self.player.rect.colliderect(npc.rect):
                npc.respawn()
                return True

        # Проверка столкновений между NPC
        for i, npc1 in enumerate(self.npcs):
            for j, npc2 in enumerate(self.npcs):
                if i != j and npc1.rect.colliderect(npc2.rect):
                    npc1.respawn()
                    npc2.respawn()

        return False

    def game_over(self):
        font = pygame.font.Font(None, 50)
        text = font.render(f"Game Over! Score: {int(self.scoreboard.score)}", True, "red")
        self.screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        pygame.display.flip()

    def run(self):
        while self.running:
            # Events
            self.running = EventHandler.handle_events(self.player)

            # Collision
            if self.check_collision():
                self.player.die()
                self.game_is_over = True
                self.game_over_time = pygame.time.get_ticks()

            # Update
            self.player.update()
            self.road.update(self.player.speed)
            for npc in self.npcs:
                npc.update()

            # Rendering
            self.screen.fill("#3c3a35")
            self.road.draw(self.screen)
            for npc in self.npcs:
                npc.draw(self.screen)
            self.player.draw(self.screen)
            self.scoreboard.draw(self.screen)

            if self.game_is_over:
                self.game_over()
                if pygame.time.get_ticks() - self.game_over_time > TIME_TO_CLOSE*1000:
                    self.running = False
            else:
                self.scoreboard.update(self.player.speed / 10)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
