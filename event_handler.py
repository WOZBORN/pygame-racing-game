import pygame


class EventHandler:
    @staticmethod
    def handle_events(player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move("left")
                elif event.key == pygame.K_RIGHT:
                    player.move("right")
                elif event.key == pygame.K_UP:
                    player.adjust_speed(1)
                elif event.key == pygame.K_DOWN:
                    player.adjust_speed(-1)

        return True
