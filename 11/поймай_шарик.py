import pygame
from pygame.draw import *
from random import randint
import turtle as tu
import numpy as np
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]



def new_ball(x,y,Vx,Vy,r):
    '''global new__ball'''

    new__ball = pygame.Surface((2*r,2*r))
    color = COLORS[randint(0, 5)]
    circle(new__ball, color, (r, r), r)
    new__ball.set_colorkey(BLACK)
    new__ball.set_alpha(255)
    screen.blit(new__ball, (x-r,y-r))
    
    

def new_rect(x1, y1, dx1,dy1):
    '''global new__rect'''
    
    new__rect = pygame.Surface((dx1,dy1))
    color = COLORS[randint(0, 5)]
    rect(new__rect, color, (0,0,dx1,dy1))
    new__rect.set_colorkey(BLACK)
    new__rect.set_alpha(255)
    screen.blit(new__rect, (x1,y1))
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

score = int(0)
misses= int(0)

x = randint(100, 1100)
y = randint(100, 900)
Vx = randint(9, 12)
Vy = randint(9, 12)
r = randint(10, 100)

x1 = randint(100, 1100)
y1 = randint(100, 900)
dx1 = randint(7, 21)
dy1 = randint(7, 21)
Vx1 = randint(1, 10)
Vy1 = randint(1, 10)
   

x2 = randint(100, 1100)
y2 = randint(100, 900)
Vx2 = randint(14, 20)
Vy2 = randint(14, 20)
r2 = randint(7, 70)
k = 0
m = 0
c = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(score)
            print(misses)
            print(score/(score + misses))
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ((event.pos[0] - x)*(event.pos[0] - x) + (event.pos[1] - y)*(event.pos[1] - y)) <= r*r:
                score += 1
            elif x1<=event.pos[0]<=x1+dx1 and y1<=event.pos[1]<=y1+dy1:
                score += 8
            elif ((event.pos[0] - x2)*(event.pos[0] - x2) + (event.pos[1] - y2)*(event.pos[1] - y2)) <= r2*r2:
                score += 8
            else:
                misses += 1
                    
    k += 1
    if k == 100:
        x = randint(100, 1100)
        y = randint(100, 900)
        Vx = randint(9, 12)
        Vy = randint(9, 12)
        r = randint(10, 100)
        k = 0
        
    m += 1
    if m == 60:
        x2 = randint(100, 1100)
        y2 = randint(100, 900)
        Vx2 = randint(14, 20)
        Vy2 = randint(14, 20)
        r2 = randint(7, 70)
        m = 0
    
    c += 1
    if c == 20:
        x1 = randint(100, 1100)
        y1 = randint(100, 900)
        dx1 = randint(7, 21)
        dy1 = randint(7, 21)
        Vx1 = randint(1, 2)
        Vy1 = randint(1, 2) 
        c = 0
        
    new_ball(x,y,Vx,Vy,r)
    x += Vx 
    y += Vy
    
    new_ball(x2,y2,Vx2,Vy2,r2)
    x2 += Vx2 
    y2 += Vy2
    
    new_rect(x,y,dx1,dy1)
    
    if r>= x+Vx or x+Vx >= (1200-r):
        Vx = -Vx
    elif r+Vy >= y+Vy or y+Vy >= (900-r):
        Vy = -Vy
        
    if r2 >= x2+Vx2 or x2+Vx2 >= (1200-r2):
        Vx2 = -Vx2
    elif r2 >= y2+Vy2 or y2+Vy2 >= (900-r2):
        Vy2 = -Vy2
        
        
    
        
    pygame.display.update()               
    screen.fill(BLACK)

pygame.quit()