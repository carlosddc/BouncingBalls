#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 28/09/2016

@author: cddc
'''
import pygame
import bouncingBalls
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self,limitx,limity):
        super(Ball,self).__init__()
        self.height = 10
        self.width = 10
        self.limity=limity
        self.limitx=limitx
        self.image=pygame.Surface([self.height,self.width])
        self.image.fill(bouncingBalls.colors.WHITE)
        self.rect = self.image.get_rect()
        self.mov_x = -4
        self.mov_y = 4
        Ball.pos_default(self)
    
    def pos_default(self):
        self.rect.x = self.limitx/2 - self.width/2
        self.rect.y = random.randrange(50, 500)
        if self.mov_x > 0:
            self.mov_x = 4
        else:
            self.mov_x = -4
        if self.mov_y > 0:
            self.mov_y = 4
        else:
            self.mov_y = -4
        
    def update(self):
        self.image=pygame.Surface([self.height,self.width])
        self.image.fill(bouncingBalls.colors.WHITE)
        if self.rect.x < 0 or self.rect.x + self.width > self.limitx:
            Ball.pos_default(self)
        self.rect.x+=self.mov_x
        if self.rect.y < 0 or self.rect.y + self.height > self.limity:
            self.mov_y *= -1
        self.rect.y+=self.mov_y
    
    def speedup(self):
        if self.mov_x > 0:
            self.mov_x+=1
        else:
            self.mov_x-=1
        
        if self.mov_y > 0:
            self.mov_y+=1
        else:
            self.mov_y-=1