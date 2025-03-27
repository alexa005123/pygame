import pygame

class Food():
    def __init__(self,a,b,c):
        self.jpg = pygame.image.load(a)
        self.rect = self.jpg.get_rect()
        self.x = b
        self.y = c

fon = Food()

pygame.init()
win_size = (500, 1000)
win = pygame.display.set_mode(win_size)
fps = pygame.time.Clock()
C = 250
V = 250
background_color = (255, 255, 255)
screen=pygame.display.set_mode(win_size)
while True:
    screen.blit(image,(0,0))

    fps.tick(40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        V -= 10
    elif keys[pygame.K_DOWN]:
        V += 10
    elif keys[pygame.K_RIGHT]:
        C += 10
    elif keys[pygame.K_LEFT]:
        C -= 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
    pygame.draw.circle(win, (0, 255, 255), (C, V), 52)
    pygame.display.update()







