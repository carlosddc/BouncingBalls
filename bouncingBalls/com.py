#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 28/09/2016

@author: cddc
'''
import pygame
import bouncingBalls
 
class COM(pygame.sprite.Sprite):
    def __init__(self,limitx,limity):
        super(COM,self).__init__()
        self.height=50
        self.width=10
        self.limity = limity
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(bouncingBalls.colors.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = limitx - 50
        self.rect.y = limity/2 - self.height/2
        self.mov_x = 0
        self.mov_y = 6
        self.level = None
        
    def update(self):
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(bouncingBalls.colors.WHITE)
        self.rect.x += self.mov_x
        self.rect.y += self.mov_y
    
    def AI(self,ball_y):
        bouncingBalls.AI.look(ball_y, self)
        
    def go_left(self):
        self.mov_x = 0
    
    def go_right(self):
        self.mov_x = 0
        
    def go_up(self):
        if self.rect.y > 0:
            self.mov_y = -6
        
    def go_down(self):
        if self.rect.y + self.height < self.limity:
            self.mov_y = 6
        
    def stop_x(self):
        self.mov_x = 0
    
    def stop_y(self):
        self.mov_y = 0