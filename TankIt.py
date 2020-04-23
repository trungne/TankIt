import pygame

pygame.init()
# basic display
window = (512, 512)
win = pygame.display.set_mode(window)
pygame.display.set_caption("TankIt")

# images file import:
bg = pygame.image.load('grass00.png')
facesideway = pygame.image.load('tankBasesideway.png')
faceupdown = pygame.image.load('tankBase.png')


# character - tank
class Tank:
    def __init__(self, location, width, height, vel, left=False, right=False, up=False, down=False):
        self.location = location
        self.width = width
        self.height = height
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


MainTank = Tank([250, 250], 32, 32, 10, up=True)
def redrawWindows():
    win.blit(bg, (0, 0))
    if MainTank.left or MainTank.right:
        win.blit(facesideway, (MainTank.location[0], MainTank.location[1]))

    if MainTank.up or MainTank.down:
        win.blit(faceupdown, (MainTank.location[0], MainTank.location[1]))

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
        MainTank.left = True
        MainTank.right = False
        MainTank.up = False
        MainTank.down = False

        MainTank.move()

    if keys[pygame.K_RIGHT] and MainTank.location[0] < window[0] - MainTank.width:
        MainTank.left = False
        MainTank.right = True
        MainTank.up = False
        MainTank.down = False

        MainTank.move()

    if keys[pygame.K_UP] and MainTank.location[1] > 0:
        MainTank.left = False
        MainTank.right = False
        MainTank.up = True
        MainTank.down = False

        MainTank.move()

    if keys[pygame.K_DOWN] and MainTank.location[1] < window[1] - MainTank.height:
        MainTank.left = False
        MainTank.right = False
        MainTank.up = False
        MainTank.down = True

        MainTank.move()

    redrawWindows()

pygame.quit()
