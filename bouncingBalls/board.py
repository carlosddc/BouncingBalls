#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 25/09/2016

@author: cddc
'''
import pygame
import bouncingBalls

class ScoreBoard():
    def __init__(self):
        self.SB_font = pygame.font.Font(None,25)
    
    def draw(self,screen,pointsP1,pointsP2,width):
        padding = self.SB_font.size("P1: " + str(pointsP1) + " COM: " + str(pointsP2))
        self.scoreboard = self.SB_font.render("P1: " + str(pointsP1) + " COM: " + str(pointsP2), True, bouncingBalls.colors.WHITE)
        screen.blit(self.scoreboard,(width/2 - padding[0]/2,10))