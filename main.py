import pygame
import neunet

pygame.init()

screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()


running = True

screen.fill("black")

while running:

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
