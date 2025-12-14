#При написании кода не использовалась нейросеть!
#© Иван Бурко, 2025 (может 2026)
import pygame, sys
from ground import ground
from cursor import cursor
from friend import friend
from unit_button import unit_button
from globals import global_gd
pygame.init()

#Инициализация дисплея, 'часов' для управления фпс и курсора
display = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
cursor = cursor(display)

#Глобальные переменные для отслеживания ввода клавиатуры, мыши и других игровых событий
ml_cl = False
mr_cl = False
r_button = False

#Параметры выбранного игроком юнита
unit_type = None
global_gd = True
to_remove = False
unit_name = ''
#Шрифты
font_ui = pygame.font.Font('assets/font.otf', 36)


#Текст
change_unit = font_ui.render('Выберите клетку', (0,0,0), True)
remove_text = font_ui.render('Выберите клтеку для удаления юнита', True, (255,0,0))
#Функция отображения необходимых для игры вещей
def draw():
    global ml_cl, mr_cl, r_button
    ml_cl = False
    mr_cl = False
    r_button = False
    cursor.draw()
    pygame.display.update()
    clock.tick(60)



#Игровые объекты
grounds = []
enemies = []
friends = []
buttons = []

#Функции отображения игровых объектов
def draw_grounds():
    global unit_type, global_gd, to_remove
    if global_gd == False:
        for ground in grounds:
            ground.draw()
            if ground.is_empty == True:
                if cursor.cursor.colliderect(ground.rect) and ml_cl == True and unit_type != None:
                    friends.append(friend(unit_type,ground.x, ground.y, display, len(friends)))
                    ground.index = len(friends) - 1
                    ground.is_empty = False
                    unit_type = None
                    global_gd = True
            if to_remove == True:
                if mr_cl == True and cursor.cursor.colliderect(ground.rect) and ground.is_empty == False:
                    friends.pop(delete_friend(ground.index))
                    ground.is_empty = True
                    global_gd = True
                    to_remove = False
                elif mr_cl == True and cursor.cursor.colliderect(ground.rect) and ground.is_empty == True:
                    global_gd = True
                    to_remove = False


def draw_enemies():
    pass

def draw_friends():
    for friend in friends:
        friend.draw()
#Функции спавна игровых объектов
def spawn_grounds():
    curr_x = 100
    curr_y = 0
    for i in range(6):
        for x in range(10):
            grounds.append(ground(curr_x,curr_y,display))
            curr_x += 120
        curr_x = 100
        curr_y += 120

def delete_friend(n):
    for i in range(len(friends)):
        if friends[i].index == n:
            return i


#Отображение игрового интерфейса
buttons.append(unit_button(0,0,1, display))
buttons.append(unit_button(0,110,2,display))
buttons.append(unit_button(0,220,3,display))
def draw_hud():
    global unit_type, global_gd, to_remove, unit_name
    pygame.draw.rect(display, (0,0,0), (0,0, 100, 720))
    if r_button == True and unit_type == None:
        to_remove = True
    for button in buttons:
        button.draw()
        if cursor.cursor.colliderect(button.rect):
            display.blit(button.cost_text, (pygame.mouse.get_pos()[0] + 20, pygame.mouse.get_pos()[1]))
    if to_remove == False:
        for button in buttons:
            if cursor.cursor.colliderect(button.rect):
                if ml_cl == True and unit_type == None:
                    unit_type = button.type
                    unit_name = button.name_text
                    global_gd = False
        if unit_type != None:
            display.blit(change_unit, (100,100))
            display.blit(unit_name, (0,0))
        if unit_type != None and mr_cl == True:
            unit_type = None
            global_gd = True
    else:
        global_gd = False
        display.blit(remove_text, (0,0))


spawn_grounds()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                ml_cl = True
            if event.button == 3:
                mr_cl = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                r_button = True
    display.fill((255,255,255))
    draw_grounds()
    draw_friends()
    draw_hud()
    draw()
    pygame.display.set_caption("ФПС = " + str(clock.get_fps()))
