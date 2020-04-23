import pygame

pygame.init()
# basic display
window = (512, 512)
win = pygame.display.set_mode(window)
pygame.display.set_caption("TankIt")
clock = pygame.time.Clock()

# images file import:
bg = pygame.image.load('grass00.png')
faceleft = pygame.image.load('tankBaseleft.png')
faceright = pygame.image.load('tankBaseright.png')
faceup = pygame.image.load('tankBaseup.png')
facedown = pygame.image.load('tankBasedown.png')


# character - tank
class Tank:
    def __init__(self, location, width, height, vel, acceleration, dir=[0, -1]):
        # attributes
        self.location = location
        self.width = width
        self.height = height
        self.vel = vel
        self.acceleration = acceleration
        self.maxspeed = 10

        # facing
        self.dir = dir

    def move(self):
        if self.vel < self.maxspeed:
            self.vel += self.acceleration
        else:
            self.vel = self.maxspeed

        if self.dir == [-1, 0]:  # left
            self.location[0] -= self.vel

        elif self.dir == [1, 0]:  # right
            self.location[0] += self.vel

        elif self.dir == [0, -1]:  # up
            self.location[1] -= self.vel

        elif self.dir == [0, 1]:  # down
            self.location[1] += self.vel

MainTank = Tank([250, 250], 32, 32, 0, 0)


def redrawWindows():
    win.blit(bg, (0, 0))
    if MainTank.dir == [-1, 0]:
        win.blit(faceleft, (MainTank.location[0], MainTank.location[1]))
    elif MainTank.dir == [1, 0]:
        win.blit(faceright, (MainTank.location[0], MainTank.location[1]))
    elif MainTank.dir == [0, -1]:
        win.blit(faceup, (MainTank.location[0], MainTank.location[1]))
    elif MainTank.dir == [0, 1]:
        win.blit(facedown, (MainTank.location[0], MainTank.location[1]))

    pygame.display.update()


# main loop
run = True
while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and MainTank.location[0] > 0:
                MainTank.dir = [-1, 0]
                MainTank.acceleration = 0.2
            elif event.key == pygame.K_RIGHT and MainTank.location[0] < window[0] - MainTank.width:
                MainTank.dir = [1, 0]
                MainTank.acceleration = 0.2
            elif event.key == pygame.K_UP and MainTank.location[1] > 0:
                MainTank.dir = [0, -1]
                MainTank.acceleration = 0.2
            elif event.key == pygame.K_DOWN and MainTank.location[1] < window[1] - MainTank.height:
                MainTank.dir = [0, 1]
                MainTank.acceleration = 0.2
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                MainTank.acceleration = 0

    if MainTank.acceleration == 0:
        MainTank.vel *= 0.92

    MainTank.move()
    redrawWindows()
    clock.tick(60)

pygame.quit()
