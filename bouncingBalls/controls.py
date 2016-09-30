#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 26/09/2016

@author: cddc
'''
import bouncingBalls
import pygame

def control_event(Player,EXIT):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
            elif event.key == pygame.K_UP:
                Player.go_up()
            elif event.key == pygame.K_DOWN:
                Player.go_down()
            elif event.key == pygame.K_LEFT:
                Player.go_left()
            elif event.key == pygame.K_RIGHT:
                Player.go_right()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Player.stop_y()
            elif event.key == pygame.K_DOWN:
                Player.stop_y()
            elif event.key == pygame.K_RIGHT:
                Player.stop_x()
            elif event.key == pygame.K_LEFT:
                Player.stop_x()
    return False