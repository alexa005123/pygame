import pygame
from random import *

class Food:
    def __init__(self, name_image, x, y):#конструктор, здесь создаются свойства, он вызывается при создании объекта
        self.jpg = pygame.image.load(name_image)#загружение картинки, ЭТО СВОЙСТВО
        self.rect = self.jpg.get_rect()#получение прямоугольника от картинки
        self.rect.x = x
        self.rect.y = y

    def draw_image(self):# метод отрисовки кортинки
        win.blit(self.jpg, (self.rect.x, self. rect.y))

    def move_food(self):  # метод движения еды вниз
        self.rect.y += 5

    def move_plate(self):# метод отрисовки картинки
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5
a = randint(-300,0 )
b = randint(-300,0 )
c = randint(-300, 0)
d = randint(-300,0 )
e = randint(-300, 0)
fon = Food('kuhnya.jpg',0,0) #создание класса food
food1 = Food('pelmen.png', 0, a)
food2 = Food('pelmen.png', 200,b )
food3 = Food('pelmen.png', 400,c )
food4 = Food('pelmen.png', 600,d )
food5 = Food('pelmen.png', 850,e )
food_list = [food1, food2, food3, food4, food5]
plate = Food('plate (2).png', 400,500)
pygame.init()#обязательная команда
window_size=(1000, 643)#размеры окна
plate. size=(100,100)
win = pygame.display.set_mode(window_size) #создание экрана с размерами window_size
fps = pygame.time.Clock() #фпс

while True:
    fps.tick(40)
    fon.draw_image() #применение метода отрисовки к объекту-класса food (фон)
    plate.draw_image()#применение метода отрисовки к объекту-класса food (тарелка)
    for i in food_list:
        i.move_food()
        i.draw_image()
        if plate.rect.colliderect(i.rect):
            food_list.remove(i)
        if i.rect.y > 700:
            i.rect.y = 0
    if food_list == []:
        pygame.QUIT()
    plate.move_plate()
    for event in pygame.event.get():#проходимся по событиям
        if event.type == pygame.QUIT:#если нажал на крестик
            pygame.QUIT()#выйти
    pygame.display.update()


