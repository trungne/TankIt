from constants import *
from util.helper import out_of_horizontal_axis, out_of_vertical_axis


class Tank(pygame.sprite.Sprite):
    """Tank objects, inherit from pygame.sprite.Sprite.

    Attributes:
        image (pygame.Surface): Tank's image. Default direction of the image is to the right.
        keys (tuple, optional): A tuple of 4 keys to control the tank. Defaults to pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
        original_image (pygame.Surface): The same as image attribute.
        rect (pygame.Rect): The rect object of image attribute.
        direction (pygame.math.Vector2()): Tank's current direction. Defaults to (1, 0).
        vel (pygame.math.Vector2()): Tank's current velocity.
        acceleration (float): Tank's current acceleration. Defaults to 0.
        angular_vel (float): Tank's angular velocity, useful for rotating the tank.
        angle (float): Tank's angle, useful for rotating the tank and its image.
    """

    def __init__(self, position, image=FACE_RIGHT, keys=(LEFT, RIGHT, UP, DOWN)):
        """
        Args:
            position (tuple of int): List of x-coordinate and y-coordinate of the tank.
            image (pygame.Surface): Tank image as a pygame.Surface instance.
            keys (tuple of int): Tuple with size of 4 contains keys for controlling the tank.
                The order of keys should be (LEFT, RIGHT, UP, DOWN).
        """
        super(Tank, self).__init__()
        self.image = image
        self.keys = keys
        self.original_image = self.image
        self.rect = self.image.get_rect(center=position)

        self.direction = pygame.math.Vector2(1, 0)

        self.vel = 0
        self.acceleration = 0
        self.angular_vel = 0
        self.angle = 0

    def update(self, key):
        """Update tank's attribute.

        Notes:
            Usually, this function will run in the main loop of the game.
            Heavy stuff should be avoided.

        Args:
            key: Controlling key code.
        """

        # update angular velocity and acceleration
        l, r, u, d = self.keys

        if key == l:
            self.angular_vel = 5
        elif key == r:
            self.angular_vel = -5
        elif key == u:
            self.acceleration = ACCELERATION
        elif key == d:
            self.acceleration = -ACCELERATION

        self.update_velocity()
        self.update_rotation()
        self.update_position()

    def update_velocity(self):
        """Update tank's velocity.

        Notes:
            This function increases the velocity if there is non-zero acceleration and tank has not reached it maximum speed
            Otherwise, it will decay the tank's velocity until it becomes 0.
        """
        if self.acceleration and abs(self.vel) < MAX_SPEED:
            # increase both x and y of vel by acceleration
            self.vel = self.vel + self.acceleration

        if not self.acceleration:
            self.vel *= FRICTION  # decreasing by percent each time there is no acceleration
            if abs(self.vel) < 0.001:
                self.vel = 0  # if vel is too small, make it zero.

    def update_rotation(self):
        """Update tank's direction, angle and rotate the tank's image and rect."""
        if self.angular_vel:
            # Rotate the direction vector and then the image.
            self.direction.rotate_ip(-self.angular_vel)
            self.angle = (self.angle + self.angular_vel) % 360
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)

    def update_position(self):
        """Update tank's position.

        Notes:
            This functions first compute the position of the tank after it moves with the current direction and velocity.
            If tank's position reached the boundary, the tank is bounced back.
        """

        # stop the tank and bounce it back when reaching screen boundaries
        new_rect = self.rect.move(self.direction * self.vel)

        if out_of_vertical_axis(new_rect):
            self.angle = 180 - self.angle
            self.direction.rotate_ip(180 - self.angle*2)
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.acceleration = 0

        if out_of_horizontal_axis(new_rect):
            self.angle = - self.angle
            self.direction.rotate_ip(-2*self.angle)
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.acceleration = 0

        self.rect.move_ip(self.direction * self.vel)
        print(self.angle)

    def draw(self, win):
        win.blit(self.image, self.rect)
