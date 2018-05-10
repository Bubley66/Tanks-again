import pygame

from conf import WIDTH, HEIGHT
from player import Player
from bullet import Bullet

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

RED = (255, 0, 102)
GREEN = (0, 0, 0)
BLUE = (102, 204, 255)

p1 = Player(20, 20, RED)
p2 = Player(780, 580, BLUE)
b = Bullet(400 + 300j, 1, 18)

while running:
    # 1. Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p1.start_moving()
            if event.key == pygame.K_DOWN:
                p1.start_moving_backwards()
            if event.key == pygame.K_w:
                p2.start_moving()
            if event.key == pygame.K_LEFT:
                p1.start_rotating_left()
            if event.key == pygame.K_RIGHT:
                p1.start_rotating_right()
            if event.key == pygame.K_KP1:
                p1.fire_bullet()
            if event.key == pygame.K_a:
                p2.start_rotating_left()
            if event.key == pygame.K_d:
                p2.start_rotating_right()
            if event.key == pygame.K_s:
                p2.start_moving_backwards()
            if event.key == pygame.K_f:
                p2.fire_bullet()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                p1.stop_moving()
            if event.key == pygame.K_DOWN:
                p1.stop_moving()
            if event.key == pygame.K_w:
                p2.stop_moving()
            if event.key == pygame.K_s:
                p2.stop_moving()
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                p1.stop_rotating()
            if event.key == pygame.K_d or event.key == pygame.K_a:
                p2.stop_rotating()

    # 2. Update game
    p1.update(p2)
    p2.update(p1)
    if p1.bullet is not None:
        p1.bullet.update()
    if p2.bullet is not None:
        p2.bullet.update()
    if p1.health <= 0 or p2.health <= 0:
        running = False

    # 3. Render screen (draw things)
    screen.fill(GREEN)

    # Draw things here
    p1.draw(screen)
    p2.draw(screen)
    if p1.bullet is not None:
        p1.bullet.draw(screen)
    if p2.bullet is not None:
        p2.bullet.draw(screen)
    pygame.display.update()

    # 4. Wait some time
    clock.tick(60)




