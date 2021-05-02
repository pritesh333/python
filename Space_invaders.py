import pygame
import random

pygame.init()

screen = pygame.display.set_mode((415, 500))

icon = pygame.image.load("spaceship.png")

pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(icon)

# Player icon
player1 = pygame.image.load("player.png")
playerX = 180
playerY = 420
playerX_change = 0

# Enemy icon
enemyImg = pygame.image.load("ufo.png")
enemyX = random.randint(0, 415)
enemyY = random.randint(0, 300)
enemyX_change = 0
enemyY_change = 0


def player(x, y):
    screen.blit(player1, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


running = True
# Game Loop which holds the screen together
while running:
    screen.fill((0, 0, 0))
    # playerX+=0.069
    # playerY-=0.069
    enemyX+=0.069
    # enemyY+= 0.069

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 355:
        playerX = 355

    enemyX += enemyX_change


    if enemyX <= 0:
        enemyX_change = 0.05
    elif enemyX >= 355:
        enemyX_change = -1


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
