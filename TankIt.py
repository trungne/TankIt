import pygame

pygame.init()
# basic display
window = (512, 512)
win = pygame.display.set_mode(window)
pygame.display.set_caption("TankIt")

# images file import:
bg = pygame.image.load('grass00.png')
faceleft = pygame.image.load('tankBaseleft.png')
faceright = pygame.image.load('tankBaseright.png')
faceup = pygame.image.load('tankBaseup.png')
facedown = pygame.image.load('tankBasedown.png')


# character - tank
class Tank:
    def __init__(self, location, width, height, vel, acceleration, left=False, right=False, up=False, down=False):
        # attributes
        self.location = location
        self.width = width
        self.height = height
        self.vel = vel
        self.acceleration = acceleration
        self.maxspeed = 15

        # facing
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def move(self):
        if self.left:
            self.vel += self.acceleration
            self.location[0] -= self.vel

        elif self.right:
            self.vel += self.acceleration
            self.location[0] += self.vel

        elif self.up:
            self.vel += self.acceleration
            self.location[1] -= self.vel

        elif self.down:
            self.vel += self.acceleration
            self.location[1] += self.vel

MainTank = Tank([250, 250], 32, 32, 0, 0, up=True)


def redrawWindows():
    win.blit(bg, (0, 0))
    if MainTank.left:
        win.blit(faceleft, (MainTank.location[0], MainTank.location[1]))
    elif MainTank.right:
        win.blit(faceright, (MainTank.location[0], MainTank.location[1]))
    elif MainTank.up:
        win.blit(faceup, (MainTank.location[0], MainTank.location[1]))
    elif MainTank.down:
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
                MainTank.left = True
                MainTank.right = False
                MainTank.up = False
                MainTank.down = False
                MainTank.acceleration = 0.2
            elif event.key == pygame.K_RIGHT and MainTank.location[0] < window[0] - MainTank.width:
                MainTank.left = False
                MainTank.right = True
                MainTank.up = False
                MainTank.down = False
                MainTank.acceleration = 0.2
            elif event.key == pygame.K_UP and MainTank.location[1] > 0:
                MainTank.left = False
                MainTank.right = False
                MainTank.up = True
                MainTank.down = False
                MainTank.acceleration = 0.2
            elif event.key == pygame.K_DOWN and MainTank.location[1] < window[1] - MainTank.height:
                MainTank.left = False
                MainTank.right = False
                MainTank.up = False
                MainTank.down = True
                MainTank.acceleration = 0.2
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                MainTank.acceleration = 0

    MainTank.vel += MainTank.acceleration
    if MainTank.vel >= MainTank.maxspeed:
        MainTank.vel = MainTank.maxspeed

    if MainTank.acceleration == 0:
        MainTank.vel *= 0.92

    MainTank.move()
    redrawWindows()

pygame.quit()
