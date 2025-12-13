#Класс курсора
import pygame

class cursor:
    def __init__(self, display):
        self.display = display
        self.cursor = pygame.draw.rect(self.display, (0,0,0), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10,10))
    def draw(self):
        self.cursor = pygame.draw.rect(self.display, (0,0,0), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10,10))
