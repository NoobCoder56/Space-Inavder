from unittest import runner
import pygame
import time
import random 
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("rega doep")
enemyImg = pygame.image.load("ufo.png")
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 600
playerChange = 0


enemyX = random.randint(0,700)
enemyY = random.randint(100,300)

enemyChange = 0.5
enemyY_Change = 0
def player(x,y):
      screen.blit(playerImg,(x,y))
def enemy(x,y):
    screen.blit(enemyImg,(x,y))
while runner:
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            runner = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChange = -0.5
            if event.key == pygame.K_RIGHT:
                playerChange = 0.5
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChange = 0
    enemyX += enemyChange
    playerX += playerChange
    if playerX >= 736 or playerX <=0:
        playerChange = 0
    if enemyX <= 0:
        enemyChange = 0.5
        enemyY += 30
    if enemyX >= 736:
        enemyChange = -0.5
        enemyY += 30
        
    print(enemyX,enemyY)
    enemy(enemyX,enemyY)
    player(playerX,playerY)
    pygame.display.update()



























