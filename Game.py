import pygame
from constants import WIN, BG
from objects.Tank import Tank


class Game:
    """Game's core, controls how the game functions.

    Attributes:
        tank_group (pygame.Spirte):  Sprite group, store all the Tanks.
        win (pygame.Surface): Game's screen.
        bg (pygame.Surface): Game's background as a pygame.Surface instance.
        num_tanks (int): Number of tanks are in the game.
        clock (pygame.time.Clock): pygame.Clock instance, useful for tracking time.
        run (bool): Boolean variable to keep the game's loop running.
    """

    def __init__(self, size=WIN, title='TankIt', background=BG):
        """Set game configurations.

        Args:
            size (tuple of int): A tuple containing:
                width (int): The width of game window. Defaults to 640.
                height (int): The height of game window. Defaults to 640.

            title (string): Game's title. Defaults to 'TankIt'.
            background (object): Game's background.
        """
        self.tank_group = pygame.sprite.Group()
        self.win = pygame.display.set_mode(size)
        self.bg = background
        self.num_tanks = 0
        # loop elements
        self.clock = pygame.time.Clock()
        self.run = False
        pygame.display.set_caption(title)

    def start(self):
        self.run = True
        self.main_loop()

    def restart(self):
        pass

    def over(self):
        pass

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.tank_group.draw(self.win)
        pygame.display.flip()

    def main_loop(self):
        """Game main loop.

        References:
            https://www.pygame.org/docs/tut/tom_games2.html
        """
        while self.run:
            self.clock.tick(60)

            for event in pygame.event.get():
                self.event_loop(event)

            # update all the tanks
            for tank in self.tank_group:
                tank.update(key=None)

            # re-draw window
            self.draw()

        pygame.quit()
        pygame.display.quit()

    def event_loop(self, event):
        """Loop for handling event.

        Args:
            event: pygame's event.
        """

        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            self.run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            for tank in self.tank_group:
                tank.update(key=event.key)
        elif event.type == pygame.KEYUP:
            for tank in self.tank_group:
                # tank.keys[:2] = left, right keys pressed                
                if event.key in tank.keys[:2]:
                    tank.angular_vel = 0
                # tank.keys[:2] = up, down keys pressed
                if event.key in tank.keys[-2:]:
                    tank.acceleration = 0

    def add_tank(self, position, image, keys=()):
        """Add new tank to the game.
        Args:
            position (tuple of int): List of x-coordinate and y-coordinate of the tank.
            image (pygame.Surface): Tank image as a pygame.Surface instance.
            keys (tuple of int): Tuple with size of 4 contains keys for controlling the tank.
                The order of keys should be (LEFT, RIGHT, UP, DOWN).
        """
        self.num_tanks += 1

        tank = Tank(position, image, keys)
        tank._id = self.num_tanks

        self.tank_group.add(tank)
