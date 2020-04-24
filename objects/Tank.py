import pygame
pygame.init()

# character - tank
faceleft = pygame.image.load('tankBaseleft.png')
faceright = pygame.image.load('tankBaseright.png')
faceup = pygame.image.load('tankBaseup.png')
facedown = pygame.image.load('tankBasedown.png')
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

    def move(self, window):
        # testing
        print(f'{self.location[0]},{self.location[1]}')

        # constraint
        if abs(self.velX) < self.maxspeed:
            self.velX += self.accelerationX

        if abs(self.velY) < self.maxspeed:
            self.velY += self.accelerationY

        # move object
        updated_x = self.location[0] + self.velX
        if self.velX and 0 < updated_x < window[0] - self.width:  # left/right movement
            self.location[0] = updated_x
        else:
            self.velX = - self.velX
            self.accelerationX = 0

        updated_y = self.location[1] + self.velY
        if self.velY and 0 < updated_y < window[1] - self.height:  # up/down movement
            self.location[1] = updated_y
        else:
            self.velY = - self.velY
            self.accelerationY = 0

    def decelerate(self):
        if self.accelerationX == 0:
            self.velX *= 0.92

        if self.accelerationY == 0:
            self.velY *= 0.92

    def redrawtank(self, win):
        if self.dir == [-1, 0]:
            win.blit(faceleft, (self.location[0], self.location[1]))
        elif self.dir == [1, 0]:
            win.blit(faceright, (self.location[0], self.location[1]))
        elif self.dir == [0, -1]:
            win.blit(faceup, (self.location[0], self.location[1]))
        elif self.dir == [0, 1]:
            win.blit(facedown, (self.location[0], self.location[1]))