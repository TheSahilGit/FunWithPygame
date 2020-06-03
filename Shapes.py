'''Code for dynamically drawing different shapes with their parmetric equations(using pygame).
'''

### Sahil Islam ###
### 02/06/2020 ###

import pygame
import numpy as np

pygame.init()

display_width = 900
display_height = 650

black = [0, 0, 0]
white = [255, 255, 255]
red = [200, 0, 0]
blue = (0, 0, 255)
green = (0, 255, 0)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Shapes")
clock = pygame.time.Clock()


def point(x, y, color):
    pygame.draw.circle(game_display, color, (int(x), int(y)), 2)


def circle(r):
    x = []
    y = []
    t = np.linspace(0, 100, 500)
    for i in range(len(t)):
        xs = r * np.cos(t[i] * 180 / np.pi)
        ys = r * np.sin(t[i] * 180 / np.pi)
        x.append(xs)
        y.append(ys)
    return x, y


def heart(scale):
    x = []
    y = []
    t = np.linspace(0, 100, 500)
    for i in range(len(t)):
        xs = scale * 16 * np.sin(t[i] * 180 / np.pi) * np.sin(t[i] * 180 / np.pi) * np.sin(t[i] * 180 / np.pi)
        ys = -scale * (13 * np.cos(t[i] * 180 / np.pi) - 5 * np.cos(2 * t[i] * 180 / np.pi) - 2 * np.cos(
            3 * t[i] * 180 / np.pi) - np.cos(4 * t[i] * 180 / np.pi))
        x.append(xs)
        y.append(ys)
    return x, y


xo = display_width / 2.0
yo = display_height / 2.0

game_display.fill(black)
gameExit = False
while not gameExit:

    x, y = heart(10)

    for i in range(len(x)):
        point(x[i] + xo, y[i] + yo, red)

        pygame.display.update()
        clock.tick(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
