import pygame
from objects.Tank import Tank
from constants import *

pygame.init()

# basic display
win = pygame.display.set_mode(WIN)
pygame.display.set_caption("TankIt")
clock = pygame.time.Clock()

# images file import:
bg = pygame.image.load('assets/grass.png')

MainTank = Tank([250, 250], 32, 32, 0, 0, 0, 0)


def redrawWindows():
    win.blit(bg, (0, 0))
    MainTank.redraw(win)
    pygame.display.update()


# main loop
run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            MainTank.update_movement(event.key)
        elif event.type == pygame.KEYUP:
            if event.key in (LEFT, RIGHT):
                MainTank.accelerate(0, axis=0)
            if event.key in (UP, DOWN):
                MainTank.accelerate(0, axis=1)

    # deceleration
    MainTank.decelerate()

    # check boundaries
    MainTank.move()

    redrawWindows()

pygame.quit()
