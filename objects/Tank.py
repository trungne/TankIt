from constants import *


class Tank:
    def __init__(self, location, width, height, velX, velY, aX, aY, dir=pygame.K_UP):
        # attributes
        self.location = location
        self.width = width
        self.height = height
        self.vel = [velX, velY]
        self.acceleration = [aX, aY]
        self.max_speed = MAX_SPEED

        # facing
        self.dir = dir

    def set_dir(self, direction):
        self.dir = direction

    def move(self):
        # testing
        # print(f'{self.location[0]},{self.location[1]}')

        # constraint
        if abs(self.vel[0]) < self.max_speed:
            self.vel[0] += self.acceleration[0]

        if abs(self.vel[1]) < self.max_speed:
            self.vel[1] += self.acceleration[1]

        # move object
        self.update_location(axis=0)  # left/right movement
        self.update_location(axis=1)  # up/down movement

    def update_location(self, axis=0):
        updated = self.location[axis] + self.vel[axis]

        # if the tank haven't reach board limit, update its location
        if self.vel[axis] and 0 < updated < WIN[axis] - self.width:
            self.location[axis] = updated
        # else bounce it back
        else:
            self.bounce_back(axis)

    def bounce_back(self, axis=0):
        self.vel[axis] = - self.vel[axis]
        self.acceleration[axis] = 0

    def update_movement(self, direction):
        if direction == LEFT or direction == UP:
            acceleration = -ACCELERATION
        else:
            acceleration = ACCELERATION

        self.set_dir(direction)
        self.accelerate(acceleration, self.get_current_axis())

    def get_current_axis(self):
        return 0 if self.dir == LEFT or self.dir == RIGHT else 1

    # TODO: (?) Change the name of this function. In the case that
    #  the amount given is 0, it is not really "accelerate", it just stops the tank.
    def accelerate(self, amount, axis=0):
        self.acceleration[axis] = amount

    def decelerate(self):
        if self.acceleration[0] == 0:
            self.vel[0] *= FRICTION

        if self.acceleration[1] == 0:
            self.vel[1] *= FRICTION

    def redraw(self, win):
        if self.dir == LEFT:
            win.blit(FACE_LEFT, (self.location[0], self.location[1]))
        elif self.dir == RIGHT:
            win.blit(FACE_RIGHT, (self.location[0], self.location[1]))
        elif self.dir == UP:
            win.blit(FACE_UP, (self.location[0], self.location[1]))
        elif self.dir == DOWN:
            win.blit(FACE_DOWN, (self.location[0], self.location[1]))
