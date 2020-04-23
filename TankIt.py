import pygame

pygame.init()
# basic display
window = (800, 800)
win = pygame.display.set_mode(window)
pygame.display.set_caption("TankIt")


# images file import:


# character - tank
class Tank:
    def __init__(self, location, size, vel, left=False, right=False, up=False, down=False):
        self.location = location
        self.size = size  # default 0 = width, 1 = height
        self.vel = vel
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def move(self):
        if self.left:
            self.location[0] -= self.vel
        elif self.right:
            self.location[0] += self.vel
        elif self.up:
            self.location[1] -= self.vel
        elif self.down:
            self.location[1] += self.vel

    def turn(self):  # left + right
        if not self.left:
            self.location[0] = self.location[0] - abs(self.size[1] - self.size[0]) // 2  # x coordinate
            self.location[1] = self.location[1] + abs(self.size[1] - self.size[0]) // 2  # y coordinate
            if self.size[0] < self.size[1]:
                self.size[0], self.size[1] = self.size[1], self.size[0]
        if not self.right:
            self.location[0] = self.location[0] - abs(self.size[1] - self.size[0]) // 2  # x coordinate
            self.location[1] = self.location[1] + abs(self.size[1] - self.size[0]) // 2  # y coordinate\
            if self.size[0] < self.size[1]:
                self.size[0], self.size[1] = self.size[1], self.size[0]

    def turnupdown(self):
        self.location[0] = self.location[0] + abs(self.size[1] - self.size[0]) // 2
        self.location[1] = self.location[1] - abs(self.size[1] - self.size[0]) // 2
        # if self.size[0] > self.size[1]:
        #    self.size[0], self.size[1] = self.size[1], self.size[0]


MainTank = Tank([250, 250], [80, 100], 10)


def redrawWindows():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (MainTank.location[0], MainTank.location[1], MainTank.size[0], MainTank.size[1]))
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
        if not MainTank.left:
            MainTank.turn()
        MainTank.left = True
        MainTank.right = False
        MainTank.up = False
        MainTank.down = False
        MainTank.move()




    if keys[pygame.K_RIGHT] and MainTank.location[0] < window[0] - MainTank.size[0]:
        MainTank.left = False
        MainTank.right = True
        MainTank.up = False
        MainTank.down = False
        #MainTank.turn()
        MainTank.move()

    if keys[pygame.K_UP] and MainTank.location[1] > 0:
        MainTank.left = False
        MainTank.right = False
        MainTank.up = True
        MainTank.down = False
        #MainTank.turnupdown()
        MainTank.move()
        # MainTank.turn(lr=False)

    if keys[pygame.K_DOWN] and MainTank.location[1] < window[1] - MainTank.size[1]:
        MainTank.left = False
        MainTank.right = False
        MainTank.up = False
        MainTank.down = True
        #MainTank.turnupdown()
        MainTank.move()
        # MainTank.turn(lr=False)

    redrawWindows()

pygame.quit()
