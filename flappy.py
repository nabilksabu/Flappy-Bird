from pathlib import Path

import pygame

pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
running = True
dt = 2
player_pos = pygame.Vector2((screen.get_width() / 2) - 25, screen.get_height() / 2)

bg_img = pygame.image.load(Path("assets") / "Game Objects" / "background-day.png")

flappy_bird = pygame.image.load("assets/Game Objects/yellowbird-downflap.png").convert()

bird_width = flappy_bird.get_width()
bird_height = flappy_bird.get_height()
gravity = 0.5
ground = 512

pygame.display.set_caption("Flappy Bird")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img, (0, 0))
    character = screen.blit(flappy_bird, player_pos)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        player_pos.y -= 300 * dt
    if player_pos.x:
        player_pos.x = max(0, min(player_pos.x, screen.get_width() - bird_width))
        player_pos.y = max(0, min(player_pos.y, screen.get_height() - bird_height))

    dt = clock.tick(60) / 1000
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
