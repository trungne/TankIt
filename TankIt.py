import pygame

pygame.init()
# basic display
window = (640, 640)
win = pygame.display.set_mode(window)
pygame.display.set_caption("TankIt")
clock = pygame.time.Clock()

# images file import:
bg = pygame.image.load('grass.png')
faceleft = pygame.image.load('tankBaseleft.png')
faceright = pygame.image.load('tankBaseright.png')
faceup = pygame.image.load('tankBaseup.png')
facedown = pygame.image.load('tankBasedown.png')


# character - tank
class Tank:
    def __init__(self, location, width, height, velX, velY, accelerationX, accelerationY, dir=[0, -1]):
        # attributes
        self.location = location
        self.width = width
        self.height = height
        self.velX = velX
        self.velY = velY
        self.accelerationX = accelerationX
        self.accelerationY = accelerationY
        self.maxspeed = 6

        # facing
        self.dir = dir

    def move(self):
        print(f'{self.location[0]},{self.location[1]}')

        # boundaries
        if int(self.location[0]) < 0 or int(self.location[0]) > window[0] - self.width:
            self.accelerationX = 0  # TODO: Fix
            self.velX = - self.velX
        if int(self.location[1]) < 0 or int(self.location[1]) > window[1] - self.height:
            self.accelerationY = 0
            self.velY = - self.velY

        # constraint
        if abs(self.velX) < self.maxspeed:
            self.velX += self.accelerationX

        if abs(self.velY) < self.maxspeed:
            self.velY += self.accelerationY

        # move object
        if self.velX:  # left/right movement
            self.location[0] += self.velX

        if self.velY:  # up/down movement
            self.location[1] += self.velY

    def decelerate(self):
        if self.accelerationX == 0:
            self.velX *= 0.92

        if self.accelerationY == 0:
            self.velY *= 0.92

    def redrawtank(self):
        if self.dir == [-1, 0]:
            win.blit(faceleft, (self.location[0], self.location[1]))
        elif self.dir == [1, 0]:
            win.blit(faceright, (self.location[0], self.location[1]))
        elif self.dir == [0, -1]:
            win.blit(faceup, (self.location[0], self.location[1]))
        elif self.dir == [0, 1]:
            win.blit(facedown, (self.location[0], self.location[1]))


MainTank = Tank([250, 250], 32, 32, 0, 0, 0, 0)


def redrawWindows():
    win.blit(bg, (0, 0))
    MainTank.redrawtank()
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

    MainTank.move()
    redrawWindows()

pygame.quit()
