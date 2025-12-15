#Класс тех, кого будет расставлять игрок
import pygame

class friend:
    global global_gd
    def __init__(self,type, x,y,display, index):
        self.x = x
        self.y = y
        self.display = display
        self.type = type
        self.cooldown = 300
        self.index = index
        self.hp = 300
        if self.type == 1:
            self.image = pygame.image.load('assets/toilet_regular.png').convert_alpha()
            self.cost = 50
            self.attack_sound = pygame.mixer.Sound('assets/sk_attack.mp3')
        if self.type == 2:
            self.image = pygame.image.load('assets/toilet_armor.png').convert_alpha()
            self.cost = 25
        if self.type == 3:
            self.image = pygame.image.load('assets/toilet_bomb.png').convert_alpha()
            self.cost = 40
        if self.type == 4:
            pass
    def draw(self):
        global global_gd
        self.rect = pygame.draw.rect(self.display, (0,0,255), (self.x, self.y, 100, 100))
        self.display.blit(self.image, (self.x, self.y))
        if self.cooldown != 0:
            self.cooldown -= 1
