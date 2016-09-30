#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 25/09/2016

@author: cddc
'''

import pygame
import bouncingBalls
from pygame.sprite import Sprite

def main():
    EXIT = False
    FPS=60
    no_frames=0
    dimensions=(800,600)
    pygame.init()
    screen = pygame.display.set_mode(dimensions)
    pygame.display.set_caption("Bouncing Balls")
    FPSClock = pygame.time.Clock()
    SB_font=bouncingBalls.board.ScoreBoard()
    pointsP1 = 0
    pointsP2 = 0
    list_items = pygame.sprite.Group()
    list_coll = pygame.sprite.Group()
    P1 = bouncingBalls.player.Player(dimensions[0],dimensions[1])
    P2 = bouncingBalls.com.COM(dimensions[0],dimensions[1])
    ball = bouncingBalls.ball.Ball(dimensions[0],dimensions[1])
    list_coll.add(P1)
    list_coll.add(P2)
    list_items.add(P1)
    list_items.add(P2)
    list_items.add(ball)
    inc = 0
    while not EXIT:
        EXIT = bouncingBalls.controls.control_event(P1,EXIT)
        for event in pygame.event.get():
            print event
            if event.type == pygame.QUIT:
                EXIT = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    EXIT = True
        list_items.update()
        FPSClock.tick(FPS)
        screen.fill(bouncingBalls.colors.BLACK)
        list_items.draw(screen)
        P2.AI(ball.rect.y)
        if no_frames == 120:
            ball.speedup()
            no_frames=0
        SB_font.draw(screen,pointsP1,pointsP2,dimensions[0])
        pygame.display.flip()
        no_frames +=1
        ball.coll_with = list_coll
        if ball.rect.x < 0:
            pointsP2 += 1
        elif ball.rect.x + ball.width > dimensions[0]:
            pointsP1 += 1
            if P1.height + inc < dimensions[1] - 5:
                P1.height += inc 
                if P1.rect.y + P1.height > P1.limity:
                    P1.rect.y = P1.limity - P1.height
        list_cont = pygame.sprite.spritecollide(ball, list_coll, False)
        for cont in list_cont:
            ball.mov_x *= -1
        
    pygame.quit()
    
if __name__ == "__main__":
    main()