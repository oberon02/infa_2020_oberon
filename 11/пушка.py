import numpy as np
import pygame as pg
from random import randint, gauss

pg.init()
pg.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_SIZE = (800, 800)


def rand_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


class GameObject:
    pass


class Shell(GameObject):
  
    def __init__(self, coord, is_bomb, vel, rad=20, color=None):
       
        self.coord = coord
        self.vel = vel
        self.is_bomb = is_bomb
        if color == None:
            color = rand_color()
        self.color = color
        self.rad = rad
        self.is_alive = True

    def check_corners(self, refl_ort=0.8, refl_par=0.9):
       
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)

    def move(self, time=1, grav=0):
       
        self.vel[1] += grav
        for i in range(2):
            self.coord[i] += time * self.vel[i]
        self.check_corners()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SCREEN_SIZE[1] - 2*self.rad:
            self.is_alive = False

    def draw(self, screen):
       
        pg.draw.circle(screen, self.color, self.coord, self.rad)
        
    def explosion(self):
        
        self.rad = self.rad*10
        
    def dead(self):
        
        self.is_alive = False

class Cannon(GameObject):
    
    def __init__(self, coord=[30, SCREEN_SIZE[1]//2], angle=0, max_pow=50, min_pow=10, color=RED):
       
        self.coord = coord
        self.angle = angle
        self.max_pow = max_pow
        self.min_pow = min_pow
        self.color = color
        self.active = False
        self.pow = min_pow
    
    def activate(self):
       
        self.active = True

    def gain(self, inc=2):
       
        if self.active and self.pow < self.max_pow:
            self.pow += inc

    def strike(self, bomb_strike):
       
        vel = self.pow
        angle = self.angle
        if bomb_strike == True:
            bomb = Shell(list(self.coord), [int(vel * np.cos(angle)), int(vel * np.sin(angle))], True)
            return bomb
        else:
            ball = Shell(list(self.coord), [int(vel * np.cos(angle)), int(vel * np.sin(angle))], False)
            return ball
        self.pow = self.min_pow
        self.active = False
        return ball
        
    def set_angle(self, target_pos):
        
        self.angle = np.arctan2(target_pos[1] - self.coord[1], target_pos[0] - self.coord[0])
        
    def movey(self, inc):
        
        if (self.coord[1] > 30 or inc > 0) and (self.coord[1] < SCREEN_SIZE[1] - 30 or inc < 0):
            self.coord[1] += inc
            
    def movex(self, inc):
       
        if (self.coord[0] > 30 or inc > 0) and (self.coord[0] < SCREEN_SIZE[0]/2 or inc < 0):
            self.coord[0] += inc

    def draw(self, screen):
       
        gun_shape = []
        vec_1 = np.array([int(5*np.cos(self.angle - np.pi/2)), int(5*np.sin(self.angle - np.pi/2))])
        vec_2 = np.array([int(self.pow*np.cos(self.angle)), int(self.pow*np.sin(self.angle))])
        gun_pos = np.array(self.coord)
        gun_shape.append((gun_pos + vec_1).tolist())
        gun_shape.append((gun_pos + vec_1 + vec_2).tolist())
        gun_shape.append((gun_pos + vec_2 - vec_1).tolist())
        gun_shape.append((gun_pos - vec_1).tolist())
        pg.draw.polygon(screen, self.color, gun_shape)


class StaticTarget(GameObject):
    
    def __init__(self, coord=None, color=None, rad=30):
        
        if coord == None:
            coord = [randint(rad, SCREEN_SIZE[0] - rad), randint(rad, SCREEN_SIZE[1] - rad)]
        self.coord = coord
        self.rad = rad

        if color == None:
            color = rand_color()
        self.color = color

    def check_collision(self, ball):
       
        dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
        min_dist = self.rad + ball.rad
        return dist <= min_dist

    def draw(self, screen):
       
        pg.draw.circle(screen, self.color, self.coord, self.rad)

class MovingTarget(GameObject):
    def __init__(self, coord=None, color=None, rad=30, vel=None):
        if coord == None:
            coord = [randint(rad, SCREEN_SIZE[0] - rad), randint(rad, SCREEN_SIZE[1] - rad)]
        self.coord = coord
        
        self.rad = rad

        if color == None:
            color = rand_color()
        self.color = color
        
        if vel == None:
            vel = [randint(1, 5), randint(1, 5)]
        self.vel = vel
        
    def move(self):
        for i in range(2):
            self.coord[i] += self.vel[i]
            
    def check_collision(self, ball):
        
        dist = sum([(self.coord[i] - ball.coord[i])**2 for i in range(2)])**0.5
        min_dist = self.rad + ball.rad
        return dist <= min_dist

    
    def check_corners(self, refl_ort=0.8, refl_par=0.9):
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)
                
    def draw(self, screen):
        
        pg.draw.circle(screen, self.color, self.coord, self.rad)
                



class ScoreTable:
  
    def __init__(self, t_destr=0, b_used=0):
        self.t_destr = t_destr
        self.b_used = b_used
        self.font = pg.font.SysFont("dejavusansmono", 25)

    def score(self):
       
        return self.t_destr - self.b_used

    def draw(self, screen):
        score_surf = []
        score_surf.append(self.font.render("Destroyed: {}".format(self.t_destr), True, WHITE))
        score_surf.append(self.font.render("Balls used: {}".format(self.b_used), True, WHITE))
        score_surf.append(self.font.render("Total: {}".format(self.score()), True, RED))
        for i in range(3):
            screen.blit(score_surf[i], [10, 10 + 30*i])


class Manager:
    
    def __init__(self, n_static_targets=1, n_moving_targets = 1):
        self.balls = []
        self.bombs = []
        self.gun = Cannon()
        self.targets = []
        self.score_t = ScoreTable()
        self.n_static_targets = n_static_targets
        self.n_moving_targets = n_moving_targets
        self.new_mission()

    def new_mission(self):
        
        '''for i in range(self.n_static_targets):
            self.targets.append(StaticTarget(rad=randint(max(1, 30 - 2*max(0, self.score_t.score())),
                30 - max(0, self.score_t.score()))))'''
        for i in range(self.n_moving_targets):
            self.targets.append(MovingTarget(rad=randint(max(1, 30 - 2 * max(0, self.score_t.score())),
                30 - max(0, self.score_t.score()))))
        
        
            
    def process(self, events, screen):
       
        done = self.handle_events(events)

        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
        
        self.move()
        self.collide()
        
        self.draw(screen)

        if len(self.targets) == 0 and len(self.balls) == 0:
            self.new_mission()

        return done

    def handle_events(self, events):
        
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.gun.movey(-5)
                elif event.key == pg.K_DOWN:
                    self.gun.movey(5)
                elif event.key == pg.K_RIGHT:
                    self.gun.movex(5)
                elif event.key == pg.K_LEFT:
                    self.gun.movex(-5)
                
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.activate()
                    for bomb in self.bombs:
                        bomb.explosion
                        
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    if randint(1,100) <= 10:
                        self.bombs.append(self.gun.strike(True))
                        self.score_t.b_used += 1
                    else:
                        self.balls.append(self.gun.strike(False))
                        self.score_t.b_used += 1
                    
        return done

    def draw(self, screen):
       
        for target in self.targets:
            target.move
        for ball in self.balls:
            ball.draw(screen)
        for bomb in self.bombs:
            bomb.draw(screen)
        
        for target in self.targets:
            target.draw(screen)
        self.gun.draw(screen)
        self.score_t.draw(screen)

    def move(self):
        
        dead_balls = []
        dead_bombs = []
        
        for i, ball in enumerate(self.balls):
            ball.move(grav=2)
            if not ball.is_alive:
                dead_balls.append(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)
            
        for i, bomb in enumerate(self.bombs):
            bomb.move(grav=2)
            if not bomb.is_alive:
                dead_bombs.append(i)
        for i in reversed(dead_bombs):
            self.bombs.pop(i)
        self.gun.gain()
        
        
    def collide(self):
       
        collisions = []
        targets_c = []
        for i, ball in enumerate(self.balls):
            for j, target in enumerate(self.targets):
                if target.check_collision(ball):
                    collisions.append([i, j])
                    targets_c.append(j)
                    
        for i, bomb in enumerate(self.bombs):
            for j, target in enumerate(self.targets):
                if target.check_collision(bomb):
                    collisions.append([i, j])
                    targets_c.append(j)
                    bomb.dead
        targets_c.sort()
        for j in reversed(targets_c):
            self.score_t.t_destr += 1
            self.targets.pop(j)


screen = pg.display.set_mode(SCREEN_SIZE)


done = False
clock = pg.time.Clock()

mgr = Manager(n_static_targets = 0,n_moving_targets = 3)

while not done:
    clock.tick(15)
    screen.fill(BLACK)
    
    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()


pg.quit()