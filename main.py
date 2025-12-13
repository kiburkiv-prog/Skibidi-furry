#При написании кода не использовалась нейросеть!
#© Иван Бурко, 2025 (может 2026)
import pygame, sys
from ground import ground
from cursor import cursor
from friend import friend
pygame.init()

#Инициализация дисплея, 'часов' для управления фпс и курсора
display = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
cursor = cursor(display)

#Глобальные переменные для отслеживания ввода клавиатуры, мыши и других игровых событий
ml_cl = False
mr_cl = False

#Функция отображения необходимых для игры вещей
def draw():
    global ml_cl, mr_cl
    ml_cl = False
    mr_cl = False
    cursor.draw()
    pygame.display.update()
    clock.tick(60)



#Игровые объекты
grounds = []
enemies = []
friends = []

#Функции отображения игровых объектов
def draw_grounds():
    for ground in grounds:
        ground.draw()
        if ground.is_empty == True:
            if cursor.cursor.colliderect(ground.rect) and ml_cl == True:
                friends.append(friend("",ground.x, ground.y, display, len(friends)))
                ground.index = len(friends) - 1
                ground.is_empty = False
        else:
            if cursor.cursor.colliderect(ground.rect) and mr_cl == True:
                friends.pop(delete_friend(ground.index))
                ground.is_empty = True

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
def draw_hud():
    pygame.draw.rect(display, (0,0,0), (0,0, 100, 720))

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
    display.fill((255,255,255))
    draw_grounds()
    draw_friends()
    draw_hud()
    draw()
    pygame.display.set_caption("ФПС = " + str(clock.get_fps()))
