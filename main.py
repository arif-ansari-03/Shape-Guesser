import pygame
import neunet
import numpy

def startPygame(h, w, input_h, input_w):
    pygame.init()

    startColor = (255, 255, 255, 0)

    global screen, clock, grid, running
    screen = pygame.display.set_mode((w, h))
    clock = pygame.time.Clock()
    grid = [[startColor for x in range(input_h)] for y in range(input_w)]
    running = True
    screen.fill("black")

def updatePygame():
    global screen, grid
    screen.fill("black")

    h = len(grid)
    w = 0
    if h > 0:
        w = len(grid[0])

    if h == 0 or w == 0:
        return -1

    boxSide = 7 #side of each pixel on the screen
    boxDist = 0 #dist btw each pixel on the screen
    s = boxDist+boxSide
    for i in range(h):
        for j in range(w):
            pygame.draw.rect(screen, grid[i][j], pygame.Rect(boxDist+i*s, boxDist+j*s, boxSide, boxSide))


startPygame(500, 500, 38, 38)

t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if t == 0:
        updatePygame()
        t = 1

    pygame.display.flip()

    clock.tick(1) #the argument is max fps

pygame.quit()
