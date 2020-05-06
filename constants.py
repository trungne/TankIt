import pygame

# board config
WIN = (640, 640)
ACCELERATION = 0.3

# pygame keys
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
UP = pygame.K_UP
DOWN = pygame.K_DOWN

# tank characters
FACE_LEFT = pygame.image.load('assets/tankBaseleft.png')
FACE_RIGHT = pygame.image.load('assets/tankBaseright.png')
FACE_UP = pygame.image.load('assets/tankBaseup.png')
FACE_DOWN = pygame.image.load('assets/tankBasedown.png')
MAX_SPEED = 6
FRICTION = 0.95
