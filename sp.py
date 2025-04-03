import pygame

class Food():

    def __init__(self,a,b,c):
        self.jpg = pygame.image.load(a)#загружение картинки
        self.rect = self.jpg.get_rect()#получение прямоугольника от картинки
        self.x = b
        self.y = c

    def draw_image(self):
        win.blit(self.jpg, (self.x, self.y))

def draw_image(self):
    screen.blit(self.image,(self.y))

fon = Food('кухня.jpg',0,0)
fon1 = Food('pelmen (2).png', 0, 0)
pygame.init()#обязательная команда
window_size=(500, 800)#размеры окна
win = pygame.display.set_mode(window_size) #создание экрана с размерами window_size
fps = pygame.time.Clock() #фпс

while True:
    fon.draw_image() #рименение метода отрисовки к объекту-картинке
    fon1.draw_image()
    fps.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
    pygame.display.update()






