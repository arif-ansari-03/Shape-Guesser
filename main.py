import pygame
import neunet
import numpy

pygame.init()

h = 100
w = 200
grid = [[(255, 0, 0, 0) for x in range(w)] for y in range(h)]

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


running = True

screen.fill("black")

while running:
    for i in range(h):
        for j in range(w):
            pygame.draw.rect(screen, i * 255 + j * 255, pygame.Rect(i, j, i+5, j+5))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, "white", pos, 5)
                
            except:
                pass

    pygame.display.flip()

    clock.tick(1)

pygame.quit()
