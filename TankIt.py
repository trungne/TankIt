import pygame

pygame.init()
# basic display
window = (700, 700)
win = pygame.display.set_mode((window))
pygame.display.set_caption("TankIt")


# images file import:


# character - tank
class Tank:
    def __init__(self, location, size, vel):
        self.location = location
        self.size = size
        self.vel = vel

    def move(self):
        pass

    def turn(self, lr=True):  # left + right
        if lr:
            self.location[1] = self.location[1] + abs(self.size[1] - self.size[0]) // 2
            self.location[0] = self.location[0] - abs(self.size[1] - self.size[0]) // 2
            if self.size[0] < self.size[1]:
                self.size[0], self.size[1] = self.size[1], self.size[0]
        else:
            self.location[0] = self.location[0] + abs(self.size[1] - self.size[0]) // 2 # x
            self.location[1] = self.location[1] - abs(self.size[1] - self.size[0]) // 2 # y
            if self.size[0] > self.size[1]:
                self.size[0], self.size[1] = self.size[1], self.size[0]

MainTank = Tank([50, 50], [80, 100], 0)

def redrawWindows():
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0),
                     (MainTank.location[0], MainTank.location[1], MainTank.size[0], MainTank.size[1]))
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
        MainTank.turn(True)
        MainTank.location[0] -= MainTank.vel

    if keys[pygame.K_RIGHT] and MainTank.location[0] < window[0] - MainTank.size[0]:
        MainTank.turn(True)
        MainTank.location[0] += MainTank.vel

    if keys[pygame.K_UP] and MainTank.location[1] > 0:
        MainTank.turn(False)
        MainTank.location[1] -= MainTank.vel

    if keys[pygame.K_DOWN] and MainTank.location[1] < window[1] - MainTank.size[1]:
        MainTank.turn(False)
        MainTank.location[1] += MainTank.vel

    redrawWindows()

pygame.quit()
