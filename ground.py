#Класс клеток для игры
import pygame
from globals import global_gd

class ground:
    global global_gd
    def __init__(self, x, y, display):
        self.x = x
        self.y = y
        self.display = display
        self.is_empty = True
        self.object = 0
        self.transperency = 0
    def draw(self):
        self.rect = pygame.draw.rect(self.display, (0,255,0,255), (self.x, self.y, 100, 100))
