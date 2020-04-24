import pygame
from objects.Tank import Tank
pygame.init()

# basic display
window = (640, 640)
win = pygame.display.set_mode(window)
pygame.display.set_caption("TankIt")
clock = pygame.time.Clock()

# images file import:
bg = pygame.image.load('grass.png')

MainTank = Tank([250, 250], 32, 32, 0, 0, 0, 0)


def redrawWindows():
    win.blit(bg, (0, 0))
    MainTank.redrawtank(win)
    pygame.display.update()


# main loop
run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                MainTank.dir = [-1, 0]
                MainTank.accelerationX = -0.3
            if event.key == pygame.K_RIGHT:
                MainTank.dir = [1, 0]
                MainTank.accelerationX = 0.3
            if event.key == pygame.K_UP:
                MainTank.dir = [0, -1]
                MainTank.accelerationY = -0.3
            if event.key == pygame.K_DOWN:
                MainTank.dir = [0, 1]
                MainTank.accelerationY = 0.3
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                MainTank.accelerationX = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                MainTank.accelerationY = 0

    # deceleration
    MainTank.decelerate()

    # check boundaries
    MainTank.move(window)

    redrawWindows()

pygame.quit()
