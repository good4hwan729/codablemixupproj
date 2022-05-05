# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:48:30 2022

@author: denis
"""

import pygame
import sys
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)
class Pane(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((600,400), 0, 32)
        self.screen.fill((white))
        pygame.display.update()

    def addRect(self):
        self.rect = pygame.draw.rect(self.screen, (black), (10, 75, 100, 200), 2)
        pygame.display.update()

    def addText(self, x, y, string):
        self.screen.blit(self.font.render(string, True, (0, 100, 255, 155)), (x, y))
        pygame.display.update()