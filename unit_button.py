#Класс кнопки юнита
import pygame


class unit_button:
    def __init__(self, x, y, type,display):
        self.x = x
        self.y = y
        self.type = type
        self.display = display
        self.cost_font = pygame.font.Font('assets/font.otf', 14)
        self.name_font = pygame.font.Font('assets/font.otf', 45)
        if self.type == 1:
            self.image = pygame.image.load('assets/toilet_regular.png').convert_alpha()
            self.cost = 50
            self.name = 'Скибиди-стрелок'
        elif self.type == 2:
            self.image = pygame.image.load('assets/toilet_armor.png').convert_alpha()
            self.cost = 25
            self.name = 'Скибиди-стена'
        elif self.type == 3:
            self.image = pygame.image.load('assets/toilet_bomb.png').convert_alpha()
            self.cost = 40
            self.name = 'Скибиди-бомба'
        if self.type == 4:
            pass
        self.cost_text = self.cost_font.render('СТОИМОСТЬ : ' + str(self.cost), True, (255, 223, 0))
        self.name_text = self.name_font.render('Вы выбрали : ' + str(self.name), True, (255, 255, 0))
    def draw(self):
        self.rect = pygame.draw.rect(self.display, (0,0,0), (self.x, self.y, 100, 100))
        self.display.blit(self.image, (self.x, self.y))
