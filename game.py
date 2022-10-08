import pygame
import random as Random

from pygame.locals import *

#Game Class
class Game():
    def __init__(self,speed,level):
        self.speed = speed
        self.level = level
        self.points = 0
        self.time   = 30
        self.gameInit = 0

    def increaseLevel(self):
        self.level = self.level + 1

    def increaseSpeed(self):
        self.speed = self.speed + 1

    def increasePoints(self,points):
        self.points = self.points + points

    def decreaseTime(self):
        self.time = self.time - 1

    def resetTime(self):
        self.time = 30
