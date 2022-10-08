import pygame
import random as Random

from pygame.locals import *
from objects import Objects

#Car Class
class Car(Objects):
    def __init__(self,position,sprite_car,way,factor):
        self.sprite = sprite_car
        self.position = position
        self.way = way
        self.factor = factor

    def move(self,speed):
        if self.way == "right":
            self.position[0] = self.position[0] + speed * self.factor
        elif self.way == "left":
            self.position[0] = self.position[0] - speed * self.factor


