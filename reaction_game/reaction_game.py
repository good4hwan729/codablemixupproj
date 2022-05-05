# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:49:25 2022

@author: denis
"""

import pygame
import pygame.font
import pygame.freetype
import text_maker
import random
from pygame.locals import *
import pygame.time


pygame.init()
ob1 = text_maker.Pane()

WINWIDTH = 700
WINHEIGHT = 700
WINSIZE = (WINWIDTH, WINHEIGHT)

CELLWIDTH = 150
CELLHEIGHT = 150
CELLSIZE = (CELLWIDTH, CELLHEIGHT)

CELLMARGINX = 50
CELLMARGINY = 50

SCREENPADX = 78
SCREENPADY = 70

WHITE = (255, 255, 255)
TR = (0, 100, 255, 155)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

DONE = False
WINDOW = pygame.display.set_mode(WINSIZE)
pygame.display.set_caption('My Game')
CLOCK = pygame.time.Clock()
CURRENTCOLOR = RED 

GRID = []
grade_list = [1,2,3,4,5,6,7,8,9]
numbers = [1,2,3,4,5,6,7,8,9]
string_numbers = []
random.shuffle(numbers)




time_since_enter = 0
grid_pos = []
count = 0
for i in range(0, 3):
    arr = []
    for j in range(0, 3):
        arr.append(count)
        count = count + 1
    grid_pos.append(arr)

for i in range(len(numbers)):
    string_numbers.append(str(numbers[i]))


for y in range(3):
     row = []
     for x in range(3):
         row.append([x * (CELLWIDTH + CELLMARGINX) + SCREENPADX, y * (CELLHEIGHT + CELLMARGINY) + SCREENPADY, WHITE])
     GRID.append(row)


print_seconds = False
time_since_enter = 0

if __name__ == '__main__':
    start_time = pygame.time.get_ticks()
    x_x = 0
    
    for row in GRID:
        for x, y, color in row:
            pygame.draw.rect(WINDOW, color, (x, y, CELLWIDTH, CELLHEIGHT))
    
    
    number_index = 0
    for j in range(130, 531, 200):
        for i in range(145, 546, 200):
            ob1.addText(i , j, string_numbers[number_index])
            number_index = number_index + 1
            
    
    clicked = False
    
    count2 = 0
    while not DONE:
        go = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            
            if event.type == MOUSEBUTTONDOWN:
                mpos_x, mpos_y = event.pos
               
                mpos_x -= SCREENPADX
                mpos_y -= SCREENPADY

                col = mpos_x // (CELLWIDTH + CELLMARGINX)
                row = mpos_y // (CELLHEIGHT + CELLMARGINY)
                
                
                if row >= 0 and col >= 0:
                    try:
                        cell_x_min, cell_y_min =  col * (CELLHEIGHT + CELLMARGINY), row * (CELLWIDTH + CELLMARGINX)
                        cell_x_max = cell_x_min + CELLWIDTH
                        cell_y_max = cell_y_min + CELLHEIGHT
                        if cell_x_min <= mpos_x <= cell_x_max and cell_y_min <= mpos_y <= cell_y_max:
                            x_x = cell_x_min + 78
                            y_y = cell_y_min + 70
                            clicked_cell = grid_pos[row][col]
                            if numbers[clicked_cell] == grade_list[count2]:
                                go = True
                                count2 = count2 + 1
                                if count2 == 9:
                                    print_seconds = True
                                    time_since_enter = pygame.time.get_ticks() - start_time
                                    DONE = True
                            else:
                                continue
                            
                        else:
                            pass
                    except IndexError:
                        pass                        
        
        if go:
            pygame.draw.rect(WINDOW, GREEN, (x_x, y_y, CELLWIDTH, CELLHEIGHT))
        
        
        pygame.display.flip()
        CLOCK.tick(60)
        
    while print_seconds:
        str2 = " secs"
        strr = str(time_since_enter/1000) + str2
        ob1.addText(310,20, strr)
        for event in pygame.event.get():
            if event.type == QUIT:
                print_seconds = False
        
    pygame.quit()

