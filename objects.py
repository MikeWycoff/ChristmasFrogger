import pygame
import random as Random

from pygame.locals import *

screen = pygame.display.set_mode((448,546), 0, 32)

#Objects Class
class Objects():
    def __init__(self,position,sprite):
        self.sprite = sprite
        self.position = position

    def draw(self):
        screen.blit(self.sprite,(self.position))

    def rect(self):
        return Rect(self.position[0],self.position[1],self.sprite.get_width(),self.sprite.get_height())
