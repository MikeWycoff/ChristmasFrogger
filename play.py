"""
Christmas Frogger
Author: Mike Wycoff
"""

import pygame
import random as Random

from pygame.locals import *
from sys import exit

from objects import Objects
from frog    import Frog
from car     import Car
from log     import Log
from game    import Game
from level   import Level

pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, 32, 2, 4096)

font_name = pygame.font.get_default_font()
game_font = pygame.font.SysFont(font_name, 72)
score_font= pygame.font.SysFont(font_name, 35) 
info_font = pygame.font.SysFont(font_name, 24)
menu_font = pygame.font.SysFont(font_name, 36)

screen = pygame.display.set_mode((448,546), 0, 32)

#Opens Images
background_filename = './images/winterbg.png'
frog_filename       = './images/sprite_sheets_up.png'
arrived_filename    = './images/frog_home.png'
car1_filename       = './images/car1.png'
car2_filename       = './images/car2.png'
car3_filename       = './images/xmas_car3.png'
car4_filename       = './images/xmas_car4.png'
car5_filename       = './images/sled02.png'
log_filename        = './images/present5.png'

#Upper left corner PyGame Icon
icon = pygame.image.load('images/santafrogger.png')
pygame.display.set_caption('Christmas Frogger')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

background  = pygame.image.load(background_filename).convert()
sprite_frog = pygame.image.load(frog_filename).convert_alpha()
sprite_arrived = pygame.image.load(arrived_filename).convert_alpha()
sprite_car1 = pygame.image.load(car1_filename).convert_alpha()
sprite_car2 = pygame.image.load(car2_filename).convert_alpha()
sprite_car3 = pygame.image.load(car3_filename).convert_alpha()
sprite_car4 = pygame.image.load(car4_filename).convert_alpha()
sprite_car5 = pygame.image.load(car5_filename).convert_alpha()
sprite_log  = pygame.image.load(log_filename).convert_alpha()

#Opens Audio
hit_sound    = pygame.mixer.Sound('./sounds/boom.wav')
water_sound  = pygame.mixer.Sound('./sounds/agua.wav')
safe_sound   = pygame.mixer.Sound('./sounds/success.wav')
#Background Audio
chime_sound  = pygame.mixer.Sound('./sounds/Jingle Bells.mp3')
0
#General Functions
def DrawList(list):
    for i in list:
        i.draw()

def MoveList(list,speed):
    for i in list:
        i.move(speed)

def DestroyCars(list):
    for i in list:
        if i.position[0] < -80:
            list.remove(i)
        elif i.position[0] > 516:
            list.remove(i)

#Logs are the presents
def DestroyLogs(list):
    for i in list:
        if i.position[0] < -100:
            list.remove(i)
        elif i.position[0] > 448:
            list.remove(i)

#Logs are the presents
def CreateLogs(list,logs,game):
    for i, tick in enumerate(list):
        list[i] = list[i] - 1
        if tick <= 0:
            if i == 0:
                list[0] = (30*game.speed)/game.level
                position_init = [-100,200]
                log = Log(position_init,sprite_log,"right")
                logs.append(log)
            elif i == 1:
                list[1] = (30*game.speed)/game.level
                position_init = [448, 161]
                log = Log(position_init,sprite_log,"left")
                logs.append(log)
            elif i == 2:
                list[2] = (40*game.speed)/game.level
                position_init = [-100, 122]
                log = Log(position_init,sprite_log,"right")
                logs.append(log)
            elif i == 3:
                list[3] = (40*game.speed)/game.level
                position_init = [448, 83]
                log = Log(position_init,sprite_log,"left")
                logs.append(log)
            elif i == 4:
                list[4] = (20*game.speed)/game.level
                position_init = [-100, 44]
                log = Log(position_init,sprite_log,"right")
                logs.append(log)

def CreateCars(list,cars,game):
    for i, tick in enumerate(list):
        list[i] = list[i] - 1
        if tick <= 0:
            if i == 0:
                list[0] = (40*game.speed)/game.level
                position_init = [-55,436]
                car = Car(position_init,sprite_car1,"right",1)
                cars.append(car)
            elif i == 1:
                list[1] = (30*game.speed)/game.level
                position_init = [506, 397]
                car = Car(position_init,sprite_car2,"left",2)
                cars.append(car)
            elif i == 2:
                list[2] = (40*game.speed)/game.level
                position_init = [-80, 357]
                car = Car(position_init,sprite_car3,"right",2)
                cars.append(car)
            elif i == 3:
                list[3] = (30*game.speed)/game.level
                position_init = [516, 318]
                car = Car(position_init,sprite_car4,"left",1)
                cars.append(car)
            elif i == 4:
                list[4] = (50*game.speed)/game.level
                position_init = [-56, 280]
                car = Car(position_init,sprite_car5,"right",1)
                cars.append(car)

def CarChangeLanes(cars):
    car = Random.choice(cars)
    initialPosition = car.position[1]
    choice = Random.randint(1,2)
    if(choice % 2 == 0):
        car.position[1] = car.position[1] + 39
    else:
        car.position[1] = car.position[1] - 39
    if car.position[1] > 436:
        car.position[1] = initialPosition
    elif car.position[1] < 280:
        car.position[1] = initialPosition

def FrogCrossTheRoad(frog,cars,game):
    for i in cars:
        carRect = i.rect()
        frogRect = frog.rect()
        if frogRect.colliderect(carRect):
            hit_sound.play()
            frog.deadFrog(game)

def FrogInTheWater(frog,logs,game):
    secure = 0
    wayLog = ""
    for i in logs:
        logRect = i.rect()
        frogRect = frog.rect()
        if frogRect.colliderect(logRect):
            secure = 1
            wayLog = i.way

    if secure == 0:
        water_sound.play()
        frog.deadFrog(game)

    elif secure == 1:
        if wayLog == "right":
            frog.position[0] = frog.position[0] + game.speed

        elif wayLog == "left":
            frog.position[0] = frog.position[0] - game.speed

def FrogsHome(frog,home,game):
    if frog.position[0] > 33 and frog.position[0] < 53:
        position_init = [43,7]
        createArrived(frog,home,game,position_init)

    elif frog.position[0] > 115 and frog.position[0] < 135:
        position_init = [125,7]
        createArrived(frog,home,game,position_init)

    elif frog.position[0] > 197 and frog.position[0] < 217:
        position_init = [207,7]
        createArrived(frog,home,game,position_init)

    elif frog.position[0] > 279 and frog.position[0] < 299:
        position_init = [289,7]
        createArrived(frog,home,game,position_init)

    elif frog.position[0] > 361 and frog.position[0] < 381:
        position_init = [371,7]
        createArrived(frog,home,game,position_init)

    else:
        frog.position[1] = 46
        frog.animation_counter = 0
        frog.animation_tick = 1
        frog.can_move = 1


def FrogsLocation(frog):
    #If the frog hasn't crossed the road
    if frog.position[1] > 240 :
        FrogCrossTheRoad(frog,cars,game)

    #If the frog fell in the river
    elif frog.position[1] < 240 and frog.position[1] > 40:
        FrogInTheWater(frog,logs,game)

    #The frog hasn't arrived home
    elif frog.position[1] < 40 :
        FrogsHome(frog,home,game)


def createArrived(frog,home,game,position_init):
    frog_arrived = Objects(position_init,sprite_arrived)
    home.append(frog_arrived)
    safe_sound.play()
    frog.setPositionToInitialPosition()
    game.increasePoints(10 + game.time)
    game.resetTime()
    frog.animation_counter = 0
    frog.animation_tick = 1
    frog.can_move = 1

chime_sound.play(-1)
text_info = menu_font.render(('Press any button to start!'),1,(0,0,0))
gameInit = 0

while gameInit == 0:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            gameInit = 1

    screen.blit(background, (0, 0))
    screen.blit(text_info,(80,150))
    pygame.display.update()

while True:
    gameInit = 1
    game = Game(3,1)
    key_up = 1
    frog_initial_position = [207,475]
    frog = Frog(frog_initial_position,sprite_frog)

    cars = []
    logs = []
    home = []
    ticks_cars = [30, 0, 30, 0, 60]
    ticks_logs = [0, 0, 30, 30, 30]
    ticks_time = 30
    pressed_keys = 0
    key_pressed = 0

    while frog.lives > 0:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYUP:
                key_up = 1
            if event.type == KEYDOWN:
                if key_up == 1 and frog.can_move == 1 :
                    key_pressed = pygame.key.name(event.key)
                    frog.moveFrog(key_pressed,key_up)
                    frog.cannotMove()
        if not ticks_time:
            ticks_time = 30
            game.decreaseTime()
        else:
            ticks_time -= 1

        if game.time == 0:
            frog.deadFrog(game)

        CreateCars(ticks_cars,cars,game)
        CreateLogs(ticks_logs,logs,game)

        MoveList(cars,game.speed)
        MoveList(logs,game.speed)
        
        FrogsLocation(frog)

        Level(home,cars,logs,frog,game)

        text_info1 = info_font.render(('Level: {0}        Points: {1}'.format(game.level,game.points)),1,(0,0,0))
        text_info2 = info_font.render(('Time: {0}        Lifes: {1}'.format(game.time,frog.lives)),1,(0,0,0))
        screen.blit(background, (0, 0))
        screen.blit(text_info1,(10,520))
        screen.blit(text_info2,(250,520))

        random = Random.randint(0,100)
        if(random % 100 == 0):
            CarChangeLanes(cars)

        DrawList(cars)
        DrawList(logs)
        DrawList(home)

        frog.animateFrog(key_pressed,key_up)
        frog.draw()

        DestroyCars(cars)
        DestroyLogs(logs)

        pygame.display.update()
        time_passed = clock.tick(30)

    while gameInit == 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                gameInit = 0

        screen.blit(background, (0, 0))
        text = game_font.render('GAME OVER', 1, (255, 0, 0))
        text_points = score_font.render(('You Scored!: {0} Points'.format(game.points)),1,(255,0,0))
        text_restart = info_font.render('Press Any Key To Play Again',1,(255,0,0))
        screen.blit(text, (75, 65))
        screen.blit(text_points,(90,170))
        screen.blit(text_restart,(110,250))

        pygame.display.update()
