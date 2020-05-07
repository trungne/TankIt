import pygame
from constants import *

pygame.init()


class Tank(pygame.sprite.Sprite):
    def __init__(self, position, vel):
        super(Tank, self).__init__()
        # attributes
        self.image = FACE_RIGHT
        self.original_image = self.image
        self.rect = self.image.get_rect(center=position)
        self.position = pygame.math.Vector2(position)
        self.direction = pygame.math.Vector2(1, 0)
        self.vel = vel
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
        if self.acceleration and abs(self.vel) < MAX_SPEED:
            self.vel += self.acceleration

        if not self.acceleration:
            self.vel *= FRICTION  # decreasing by percent each time there is no acceleration
            if abs(self.vel) < 0.001:
                self.vel = 0  # if vel is too small, make it zero.

        # rotating
        if self.angular_vel:
            # Rotate the direction vector and then the image.
            self.direction.rotate_ip(self.angular_vel)
            self.angle += self.angular_vel
            self.image = pygame.transform.rotate(self.original_image, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

        # Update the position vector and the rect
        # TODO: fix object doesn't change angle when bouncing.
        updated_position = self.position + self.direction * self.vel
        w, h = self.image.get_size()
        if w // 2 < updated_position[0] < WIN[0] - w // 2:  # check x axis
            self.position[0] += self.direction[0] * self.vel
        else:
            self.vel = - self.vel
            self.position[0] += self.direction[0] * self.vel
            # change y
            self.acceleration = 0

        if h // 2 < updated_position[1] < WIN[1] - h // 2:  # check y axis
            self.position[1] += self.direction[1] * self.vel
        else:
            self.vel = - self.vel
            self.position[1] += self.direction[1] * self.vel
            # change x
            self.acceleration = 0

        self.rect.center = self.position

        # testing
        # print(self.position)
        # print(self.rect.center)
