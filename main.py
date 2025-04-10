import pygame

class Food:
    def __init__(self, name_image, x, y):#конструктор, здесь создаются свойства, он вызывается при создании объекта
        self.jpg = pygame.image.load(name_image)#загружение картинки, ЭТО СВОЙСТВО
        self.rect = self.jpg.get_rect()#получение прямоугольника от картинки
        self.rect.x = x
        self.rect.y = y

    def draw_image(self):# метод отрисовки кортинки
        win.blit(self.jpg, (self.rect.x, self. rect.y))

fon = Food('kuhnya.jpg',0,0) #создание класса food
food1 = Food('pelmen.png', 0, 0)
plate = Food('plate.png', 400,500)
pygame.init()#обязательная команда
window_size=(1000, 643)#размеры окна
plate. size=(100,100)
win = pygame.display.set_mode(window_size) #создание экрана с размерами window_size
fps = pygame.time.Clock() #фпс_foo


while True:
    fon.draw_image() #применение метода отрисовки к объекту-класса food (фон)
    food1.draw_image() #применение метода отрисовки к объекту-класса food (еда)
    plate.draw_image()#применение метода отрисовки к объекту-класса food (тарелка)
    fps.tick(40)
    for event in pygame.event.get():#проходимся по событиям
        if event.type == pygame.QUIT:#если нажал на крестик
            pygame.QUIT()#выйти
    pygame.display.update()
