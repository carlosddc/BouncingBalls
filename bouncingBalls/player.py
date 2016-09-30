#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 26/09/2016

@author: cddc
'''
import pygame
import bouncingBalls
from pygame.rect import Rect

class Player(pygame.sprite.Sprite):
    def __init__(self,limitx,limity):
        super(Player,self).__init__()
        self.height=50
        self.width=10
        self.limity = limity
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(bouncingBalls.colors.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 300 - self.height/2
        self.mov_x = 0
        self.mov_y = 0
        self.level = None
        
    def update(self):
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(bouncingBalls.colors.WHITE)
        self.rect.x += self.mov_x
        self.rect.y += self.mov_y
        self.rect = Rect(self.rect.x,self.rect.y,self.width,self.height)
        if self.rect.y < 0:
            self.stop_y()
        elif self.rect.y + self.height > self.limity:
            self.stop_y()
        """
        list_col_block = pygame.sprite.spritecollide(self, self.nivel.list_objects, False)
        for block in list_col_block:
            if self.mov_x > 0:
                self.rect.right = block.rect.left
            elif self.mov_x < 0:
                self.rect.left = block.rect.right
            if self.mov_y > 0:
                self.rect.bottom = block.rect.top 
            elif self.mov_y < 0:
                self.rect.top = block.rect.bottom
        """
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