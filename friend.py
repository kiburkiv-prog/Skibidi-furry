#Класс тех, кого будет расставлять игрок
import pygame

class friend:
    def __init__(self,type, x,y,display, index):
        self.x = x
        self.y = y
        self.display = display
        self.type = type
        self.index = index
    def draw(self):
        self.rect = pygame.draw.rect(self.display, (0,0,255), (self.x, self.y, 100, 100))
