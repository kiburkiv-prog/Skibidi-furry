#Класс пули
import pygame
class bullet:
    def __init__(self, x, y, owner, display):
        self.x = x
        self.y = y
        self.owner = owner
        self.display = display
        self.image = pygame.image.load('assets/bullet.png')
        if self.owner == 'friend':
            self.speed = 2
        else:
            self.speed = -2
    def draw(self):
        self.rect = pygame.draw.rect(self.display, (255,0,0), (self.x, self.y, 32, 32))
        self.display.blit(self.image, (self.x, self.y))
        self.x += self.speed
