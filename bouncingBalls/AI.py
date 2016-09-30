#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 29/09/2016

@author: cddc
'''

import pygame
import bouncingBalls

'''
    #y=mov_y*t
    #t=y/mov_y
    t=(dimensions[0]/2 - com.rect.x)/ball.mov_x
    goal_x = com.rect.x
    goal_y = 
    '''

def look(ball_y,com):
    if ball_y - com.rect.y-com.height/2 > 0:
        com.go_down()
    else:
        com.go_up()
        
def up_down(com,dimensions):
    if com.rect.y < 0 or com.rect.y + com.height > com.dimension[1]:
            com.mov_y *= -1