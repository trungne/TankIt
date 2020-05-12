import pygame

# game config
WIN = (640, 640)
ACCELERATION = 0.3
BG = pygame.image.load('assets/grass.png')

# pygame keys
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
UP = pygame.K_UP
DOWN = pygame.K_DOWN
A = pygame.K_a
W = pygame.K_w
S = pygame.K_s
D = pygame.K_d

# tank characters
FACE_LEFT = pygame.image.load('assets/tankBaseleft.png')
FACE_RIGHT = pygame.image.load('assets/tankBaseright.png')
FACE_UP = pygame.image.load('assets/tankBaseup.png')
FACE_DOWN = pygame.image.load('assets/tankBasedown.png')
MAX_SPEED = 6
FRICTION = 0.95
