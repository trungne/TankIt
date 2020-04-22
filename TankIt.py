import pygame

pygame.init()
# basic display
window = (800, 800)
win = pygame.display.set_mode(window)
pygame.display.set_caption("TankIt")


# images file import:


# character - tank
class Tank:
    def __init__(self, location, size, vel):
        self.location = location
        self.size = size # default 0 = width, 1 = height
        self.vel = vel

    def move(self, left=False, right=False, up=False, down=False):
        if left:
            self.location[0] -= self.vel
        elif right:
            self.location[0] += self.vel
        elif up:
            self.location[1] -= self.vel
        elif down:
            self.location[1] += self.vel

    def turn(self):  # left + right
        self.location[0] = self.location[0] - (self.size[1] - self.size[0]) // 2  # x coordinate
        self.location[1] = self.location[1] + (self.size[1] - self.size[0]) // 2  # y coordinate

    #     else:  # up + down
    #         self.location[0] = self.location[0] + (self.size[1] - self.size[0])// 2  # x
    #         self.location[1] = self.location[1] - (self.size[1] - self.size[0])// 2  # y
    #         #self.size[0], self.size[1] = self.size[1], self.size[0]


MainTank = Tank([50, 50], [80, 100], 20)


def redrawWindows():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0),
                     (MainTank.location[0], MainTank.location[1], MainTank.size[0], MainTank.size[1]))
    pygame.display.update()


# main loop
run = True
while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and MainTank.location[0] > 0:
        MainTank.move(left=True)
        #MainTank.turn()
        # MainTank.turn(lr=True)

    if keys[pygame.K_RIGHT] and MainTank.location[0] < window[0] - MainTank.size[0]:
        MainTank.move(right=True)
        #MainTank.turn()

    if keys[pygame.K_UP] and MainTank.location[1] > 0:
        MainTank.move(up=True)
        # MainTank.turn(lr=False)

    if keys[pygame.K_DOWN] and MainTank.location[1] < window[1] - MainTank.size[1]:
        MainTank.move(down=True)
        # MainTank.turn(lr=False)

    redrawWindows()

pygame.quit()
