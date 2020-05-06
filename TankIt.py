import pygame
from objects.Tank import Tank
from constants import *

pygame.init()

# basic display
win = pygame.display.set_mode(WIN)
pygame.display.set_caption("TankIt")

# images file import:
bg = pygame.image.load('assets/grass.png')
MainTank = Tank([250, 250], 0)
MainTankSprite = pygame.sprite.Group(MainTank)
clock = pygame.time.Clock()


def redrawWindows():
    win.blit(bg, (0, 0))
    MainTankSprite.draw(win)
    pygame.display.flip()


# main loop
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            MainTank.update(event.key)
        elif event.type == pygame.KEYUP:
            if event.key in (LEFT, RIGHT):
                MainTank.angular_vel = 0
            if event.key in (UP, DOWN):
                MainTank.acceleration = 0

    MainTank.update(event=None)
    redrawWindows()

pygame.quit()
