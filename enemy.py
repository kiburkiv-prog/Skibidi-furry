#Класс врагов
import pygame
class enemy:
    def __init__(self, x, y, type,display):
        self.x = x
        self.y = y
        self.type = type
        self.display = display
        self.hp = 3
        self.is_attacking = False
        if self.type == 1:
            self.image = pygame.image.load('assets/furry1.png').convert_alpha()
            self.speed = 0.25
            self.last_speed = self.speed
        if self.type == 2:
            self.image = pygame.image.load('assets/furry2.png').convert_alpha()
            self.speed = 0.25
            self.last_speed = self.speed
        if self.type == 3:
            self.image = pygame.image.load('assets/furry3.png').convert_alpha()
            self.speed = 0.25
            self.last_speed = self.speed
    def draw(self):
        self.rect = pygame.draw.rect(self.display, (255,0,0), (self.x, self.y, 100,100))
        self.display.blit(self.image, (self.x, self.y))
        self.x -= self.speed
        if self.is_attacking == False:
            self.speed = self.last_speed
            self.last_speed = self.speed
        if self.is_attacking == True:
            self.speed = 0
