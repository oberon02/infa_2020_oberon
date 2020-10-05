import pygame
from pygame.draw import *

pygame.init()

FPS = 6
screen = pygame.display.set_mode((1200, 800))
screen.fill((179, 156, 183))


rect(screen, (255, 214, 160), (0, 0, 1200, 185))

rect(screen, (255, 220, 200), (0, 185, 1200, 185))

rect(screen, (255, 214, 160), (0, 370, 1200, 185))

circle(screen, (255, 255, 0), (600, 185), 60)

polygon(screen, [255, 138, 0], ((10, 350), (5, 390), (1200 ,300),(1100,260),(1050,280),(950,240),(910,255),(800,200),(707,190),
                                (650,290),(635,280),(600,320),(560,325),(520,349),(485,330),(350,340),(200,150)))


ellipse(screen, (255, 220, 200), (0, 0, 220, 350))

rect(screen, (255, 214, 160), (0, 0, 220, 185))

ellipse(screen, (255, 220, 200), (800, 90, 100, 170))

ellipse(screen, [255, 138, 0], (703, 125, 100, 160))

rect(screen, (255, 214, 160), (800, 0, 220, 185))

ellipse(screen, (172, 81, 0), (-10, 400, 200, 300))

ellipse(screen, (172, 81, 0), (710, 400, 140, 300))

polygon(screen, (172, 81, 0), ((0, 555),(190, 550),(260,410),(330,470),(370,360),(490,380),(610,500),(710,480),(820,430),(880,460)
                               ,(940,410),(1000,360),(1100,420),(1200,300)
                               ,(1200,555)))

rect(screen, (179, 156, 183), (0, 555, 1200, 300))

polygon(screen, [53, 4, 51],[[0, 800], [0, 480], [150, 600], [200, 799], 
                             [500, 750], [700, 799], [800, 799], [950, 730], [1000, 799],
                             [1100, 600], [1200, 500], [1200, 800]])




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()