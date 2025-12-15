#При написании кода не использовалась нейросеть!
#© Иван Бурко, 2025 (может 2026)
import pygame, sys, random
from ground import ground
from cursor import cursor
from friend import friend
from unit_button import unit_button
from enemy import enemy
from bullet import bullet

pygame.init()

#Инициализация дисплея, 'часов' для управления фпс и курсора
display = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
cursor = cursor(display)

#Глобальные переменные для отслеживания ввода клавиатуры, мыши и других игровых событий
ml_cl = False
mr_cl = False
r_button = False
enemy_count = 0
enemy_cooldown = 500
enemies_to_kill = 30
#фон
background = pygame.image.load('assets/back1.png').convert_alpha()

#звуки
born_s = pygame.mixer.Sound('assets/born.mp3')
death_s = pygame.mixer.Sound('assets/death.mp3')
win_s = pygame.mixer.Sound('assets/win.mp3')
lose_s = pygame.mixer.Sound('assets/lose.mp3')
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
    global ml_cl, mr_cl, r_button, enemies_to_kill
    ml_cl = False
    mr_cl = False
    r_button = False
    cursor.draw()
    pygame.display.update()
    clock.tick(60)
    if enemies_to_kill == 0:
        win_s.play()
        enemies_to_kill -= 1



#Игровые объекты
grounds = []
enemies = []
friends = []
buttons = []
bullets = []

#Функции отображения игровых объектов
def draw_grounds():
    global unit_type, global_gd, to_remove
    if global_gd == False:
        for ground in grounds:
            ground.draw()
            if ground.is_empty == True:
                if cursor.cursor.colliderect(ground.rect) and ml_cl == True and unit_type != None:
                    friends.append(friend(unit_type,ground.x, ground.y, display, len(friends)))
                    born_s.play()
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
    global enemies_to_kill
    for enemy in enemies:
        enemy_attack = False
        enemy.draw()
        for bullet in bullets:
            if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'friend':
                enemy.hp -= 1
                bullets.pop(bullets.index(bullet))
                break
        for friend in friends:
            if enemy.rect.colliderect(friend.rect):
                enemy_attack = True
                friend.hp -= 1
        if enemy_attack == True:
            enemy.is_attacking = True
        else:
            enemy.is_attacking = False
        if enemy.hp == 0:
            enemies.pop(enemies.index(enemy))
            death_s.play()
            enemies_to_kill -= 1
def draw_friends():
    for friend in friends:
        friend.draw()
        if friend.type == 1:
            for enemy in enemies:
                if enemy.y == friend.y and friend.cooldown == 0:
                    friend.attack_sound.play()
                    bullets.append(bullet(friend.x,friend.y,'friend', display))
                    friend.cooldown = 600
                    break
        if friend.hp == 0:
            friends.pop(friends.index(friend))
            death_s.play()

def draw_bullets():
    for bullet in bullets:
        bullet.draw()
        if bullet.x > 1280 or bullet.x < -32:
            bullets.pop(bullets.index(bullet))
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

def spawn_enemies(count):
    global enemy_count, enemy_cooldown
    if enemy_count != count:
        if enemy_cooldown == 0:
            enemies.append(enemy(1280, 120 * random.randint(0, 5), random.randint(1, 3), display))
            enemy_cooldown = 500
            enemy_count += 1
        else:
            enemy_cooldown -= 1
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
    display.blit(background, (0,0))
    draw_grounds()
    draw_friends()
    draw_bullets()
    draw_enemies()
    draw_hud()
    spawn_enemies(30)
    draw()
    pygame.display.set_caption("ФПС = " + str(clock.get_fps()))
