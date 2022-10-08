import pygame
import random as Random

from pygame.locals import *
from game import Game

#Level Class
def Level(home,cars,logs,frog,game):
    if len(home) == 5:
        home[:] = []
        frog.setPositionToInitialPosition()
        game.increaseLevel()
        game.increaseSpeed()
        game.increasePoints(100)
        game.resetTime()

