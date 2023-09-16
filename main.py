import pygame
import neunet
import numpy

''' === functions defn === '''

def startPygame(h, w, input_h, input_w):
    pygame.init()

    startColor = (0, 0, 0, 0)

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

    boxSide = 5 #side of each pixel on the screen
    boxDist = 0 #dist btw each pixel on the screen
    s = boxDist+boxSide
    for i in range(h):
        for j in range(w):
            t = []
            for k in range(4):
                t.append(255-grid[i][j][k])

            pygame.draw.rect(screen, tuple(t), pygame.Rect(boxDist+i*s, boxDist+j*s, boxSide, boxSide))

def applyBlur(pos):
    t = [ [0.05, 0.1, 0.05], [0.1, 0.4, 0.1], [0.05, 0.1, 0.05] ]
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]

    color = [0, 0, 0, 0]
    
    for i in range(8):
        for k in range(4):
            x = pos[0]+dx[i]
            y = pos[1]+dy[i]
            if x < 0 or x >= 70 or y < 0 or y >= 70:
                continue
            color[k] += t[1+dx[i]][1+dy[i]]*grid[x][y][k]
            
    return tuple(color)

def updatePixel(pos, color):
    global grid
    x, y = pos

    if x < 0 or x >= 70 or y < 0 or y >= 70 or grid[x][y] == (255, 255, 255, 0):
        return 0

    grid[x][y] = color

def updateGrid(pos):
    x, y = pos
    x = int(x/5) #divide the x and y coordinate by sum of boxDist and boxSide in updatePygame function
    y = int(y/5)
    updatePixel((x, y), (255, 255, 255, 0))
    dx = [1, 0, -1, 0, 1, -1, 1, -1]
    dy = [0, 1, 0, -1, 1, -1, -1, 1]

    for i in range(-2, 3):
        for j in range(-2, 3):
            updatePixel((x+i, y+j), applyBlur((x+i, y+j)))
    

''' ================ '''




startPygame(425, 600, 70, 70)

t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            updateGrid((x, y))
            updateGrid((x-5, y))

    updatePygame()
    pygame.display.flip()

    clock.tick(1000) #the argument is max fps

    
N = neunet.Network()
N.readWeights("out.txt")

grid = [[list(x) for x in y] for y in grid]
print(N.calc_out(numpy.array(grid).flatten()))

pygame.quit()
