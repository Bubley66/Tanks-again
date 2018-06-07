import pygame
import conf
from conf import WIDTH, HEIGHT
from player import Player
from gamestate import GameState


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
conf.running = True



state = GameState()


while conf.running:
    # 1. Process input
    state.process_input()

    # 2. Update game
    state.update()

    # 3. Render screen (draw things)
    state.draw(screen)

    # 4. Wait some time
    clock.tick(60)