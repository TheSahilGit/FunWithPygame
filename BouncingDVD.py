### This code generates the old DVD screensaver. ###
### Sahil Islam ###
### Date: 29/05/2020 ###

import pygame

black = [0, 0, 0]
displayWidth = 900
displayHeight = 650
imageWidth = 221
imageHeight = 106
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("DVD")
dvdImage = pygame.image.load('DVD.jpg')         # This file is in the same repasitory. Should download that too.
screen.fill(black)
clock = pygame.time.Clock()


def dvd(xPos, yPos):
    screen.blit(dvdImage, (int(xPos), int(yPos)))


xVel = +5
yVel = -5

x = displayWidth / 2.
y = displayHeight / 2.

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    x += xVel
    y += yVel
    dvd(x, y)
    if x < 0 or x + imageWidth > displayWidth:
        xVel *= -1
    if y < 0 or y + imageHeight > displayHeight:
        yVel *= -1

    pygame.display.update()
    clock.tick(50)
