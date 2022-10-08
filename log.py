import pygame
import random as Random

from pygame.locals import *
from objects import Objects

#Log Class
class Log(Objects):
    def __init__(self,position,sprite_log,way):
        self.sprite = sprite_log
        self.position = position
        self.way = way

    def move(self,speed):
        if self.way == "right":
            self.position[0] = self.position[0] + speed
        elif self.way == "left":
            self.position[0] = self.position[0] - speed

#The logs are the presents

