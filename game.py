import pygame
import time
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, NPC_COUNT
from player import Player
from npc import NPC
from road import Road
from scoreboard import Scoreboard
from event_handler import EventHandler

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Racing Game")

        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player()
        self.npcs = [NPC() for _ in range(NPC_COUNT)]
        self.road = Road()
        self.scoreboard = Scoreboard()

    def check_collision(self):
        for npc in self.npcs:
            if self.player.rect.colliderect(npc.rect):
                return True
        return False

    def game_over(self):
        font = pygame.font.Font(None, 50)
        text = font.render(f"Game Over! Score: {int(self.scoreboard.score)}", True, "red")
        self.screen.fill((0, 0, 0))
        self.screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        time.sleep(2)
        self.running = False

    def run(self):
        while self.running:
            # Events
            self.running = EventHandler.handle_events(self.player)

            # Collision
            if self.check_collision():
                self.game_over()
                break

            # Update
            self.road.update(self.player.speed)
            for npc in self.npcs:
                npc.update()

            self.scoreboard.update(self.player.speed / 10)

            # Rendering
            self.screen.fill("#3c3a35")
            self.road.draw(self.screen)
            for npc in self.npcs:
                npc.draw(self.screen)
            self.player.draw(self.screen)
            self.scoreboard.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
