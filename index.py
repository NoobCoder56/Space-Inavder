import pygame
pygame.init()
display_width = 1080
display_height = 1080

screen = pygame.display.set_mode((display_width,display_height))

Clock = pygame.time.Clock()
pygame.display.set_caption('DEMO')
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
screen.fill(white)

face=pygame.image.load('ufo.png')
def brain(x,y):
     screen.blit(face,(x,y))

x1 =(display_width*0.5)
y1 =(display_height*0.5)
x_change =0
y_change =0
gameExit = False

while not gameExit:
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
        gameExit = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = -5
        elif  event.key == pygame.K_RIGHT:
            x_change = 5
        elif event.key == pygame.K_DOWN:
            y_change = 5
        elif event.key == pygame.K_UP:
            y_change = -5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            y_change = 0

  x1 += x_change
  y1 += y_change
  print(event)
  brain(x1,y1)
  pygame.display.update()
  Clock.tick(100)
pygame.quit()
quit()