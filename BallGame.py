import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode( [500,500] )

circlePos = [250,250]
circleVos = [0,0]
radius = 30

badGuyPos = [40,40]
badGuyRad = 5

running = True
while running == True:
    #Getting input of the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                circleVos[0] -= 0.5
            if event.key == pygame.K_RIGHT:
                circleVos[0] += 0.5
            if event.key == pygame.K_UP:
                circleVos[1] -= 0.5
            if event.key == pygame.K_DOWN:
                circleVos[1] += 0.5
    #Actions
    circlePos[0] = circlePos[0] + circleVos[0]
    circlePos[1] += circleVos[1]

    #circlePos[0] = circlePos[0] + 2
    if(circlePos[0] > 500 - radius):
        circleVos[0] *= -0.5
    if(circlePos[0] < radius):
        circleVos[0] *= -0.5
    if(circlePos[1] > 500 - radius):
        circleVos[1] *= -0.5
    if(circlePos[1] < radius):
        circleVos[1] *= -0.5

    #Check to see if circle touches the badGuy
    #Distance = sqrt((X2-X1)^2 + (Y2-Y1)^2)
    distance = math.sqrt( (badGuyPos[0] - circlePos[0])**2 + (badGuyPos[0] - circlePos[0])**2)
    radTotal = badGuyRad + radius

    if(distance <= radTotal):
        print("Touching")
        badGuyPos[0] = random.randint(5, 495)
        badGuyPos[1] = random.randint(5, 495)

    screen.fill( (255,255,255) )

    pygame.draw.circle(screen, (0,0,255), (circlePos[0], circlePos[1]), radius)
    pygame.draw.circle(screen, (255,0,0), (badGuyPos[0], badGuyPos[1]), badGuyRad)

    pygame.display.flip()

pygame.quit()