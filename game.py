import pygame
import sys
import math

# ---------- INIT ----------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First AI Game")
clock = pygame.time.Clock()

# ---------- COLORS ----------
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# ---------- PLAYER ----------
player_x = 400
player_y = 300
player_size = 50
player_speed = 5

# ---------- ENEMY ----------
enemy_x = 100
enemy_y = 100
enemy_size = 50
enemy_speed = 2

# ---------- SCORE ----------
score = 0
font = pygame.font.SysFont(None, 36)

# ---------- GAME LOOP ----------
running = True
while running:
    clock.tick(60)  # 60 FPS

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # PLAYER MOVEMENT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # ENEMY AI (CHASE PLAYER)
    if enemy_x < player_x:
        enemy_x += enemy_speed
    if enemy_x > player_x:
        enemy_x -= enemy_speed
    if enemy_y < player_y:
        enemy_y += enemy_speed
    if enemy_y > player_y:
        enemy_y -= enemy_speed

    # RECTANGLES
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    # COLLISION
    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        running = False

    # SCORE UPDATE
    score += 1

    # DRAW
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
sys.exit()


