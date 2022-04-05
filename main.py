from unittest import runner
import pygame
import time
import random 
import math
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("rega doep")
playerImg = pygame.image.load("spaceship.png")
bulletImg = pygame.image.load("bullet.png")
playerX = 370
playerY = 600
playerChange = 0

enemyImg = []
enemyX = []
enemyY = [] 
enemyY_Change = 30
enemyChange = 0.4

for i in range(6):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))


bulletX = 0
bulletY = 600
bulletState = "ready"

score = 0
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg,(x+16,y+10))
def isCollison(enemyx,enemyy,bulletx,bullety):
     distance = round(math.sqrt(math.pow(enemyx - bulletx, 2) + (math.pow(enemyy - bullety, 2))))
     if distance == 27:
        
        return True 
     else:
        return False
           



while runner:
    screen.fill((0,0,0))
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            runner = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChange = -0.7
            if event.key == pygame.K_RIGHT:
                playerChange = 0.7
            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    bulletX = playerX
                    fire(playerX,bulletY)

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChange = 0
    playerX += playerChange
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
        

    if bulletY <= 0:
        bulletY = 600
        bulletState = "ready"
    if bulletState == "fire":
        fire(bulletX,bulletY)
        bulletY -= 1
    
    for i in range(6):

        enemyX[i] += enemyChange
        if enemyX[i] <= 0:
            enemyChange = 0.4
            enemyY[i] += enemyY_Change 
        elif enemyX[i] >= 736:
            enemyChange = -0.4
            enemyY[i] += enemyY_Change  
        enemy(enemyX[i],enemyY[i],i)

        collison = isCollison(enemyX[i],enemyY[i],bulletX,bulletY)
        if collison == True:
            bulletY = 600
            print('score')
            score += 1
            bulletState = "ready"
            enemyX[i] = random.randint(0,700)
            enemyY[i] = random.randint(100,300)

    player(playerX,playerY)

   
    pygame.display.update()


























