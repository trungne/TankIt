from constants import *
from util.helper import has_reached_horizontal_boundary, has_reached_vertical_boundary


class Tank(pygame.sprite.Sprite):
    def __init__(self, position, vel):
        super(Tank, self).__init__()
        # attributes
        self.image = FACE_RIGHT
        self.original_image = self.image
        self.rect = self.image.get_rect(center=position)
        self.position = pygame.math.Vector2(position)
        self.direction = pygame.math.Vector2(1, 0)
        # basically, vel is not a vector but we will use it as a vector for convenience.
        # x and y of vel will always be the same
        self.vel = pygame.math.Vector2(vel)
        self.acceleration = 0
        self.angular_vel = 0
        self.angle = 0

    def update(self, event):
        if event == LEFT:
            self.angular_vel = -5
        elif event == RIGHT:
            self.angular_vel = 5
        elif event == UP:
            self.acceleration = ACCELERATION
        elif event == DOWN:
            self.acceleration = -ACCELERATION

        # update velocity
        if self.acceleration and abs(self.vel[0]) < MAX_SPEED:
            # increase both x and y of vel by acceleration
            self.vel = self.vel.elementwise() + self.acceleration

        if not self.acceleration:
            self.vel *= FRICTION  # decreasing by percent each time there is no acceleration
            if abs(self.vel[0]) < 0.001:
                self.vel.update(0, 0)  # if vel is too small, make it zero.

        # rotating
        if self.angular_vel:
            # Rotate the direction vector and then the image.
            self.direction.rotate_ip(self.angular_vel)
            self.angle += self.angular_vel
            self.image = pygame.transform.rotate(self.original_image, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        # TODO: fix object doesn't change angle when bouncing.

        # stop the tank and bounce it back when reaching screen boundaries
        new_rect = self.rect.move(self.direction.elementwise() * self.vel.elementwise())

        if has_reached_horizontal_boundary(new_rect):
            self.vel[0] = - self.vel[0]
            self.acceleration = 0

        if has_reached_vertical_boundary(new_rect):
            self.vel[1] = - self.vel[1]
            self.acceleration = 0

        self.rect.move_ip(self.direction.elementwise() * self.vel.elementwise())
