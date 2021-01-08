import pygame
import random
pygame.init()

class Ball:
    def __init__(self, radius, color, startingx, startingy, friction, weight):
        self.radius = radius
        self.diameter = radius*2
        self.color = color
        self.x = startingx
        self.y = startingy
        self.vx = friction
        self.vy = weight
        self.yspeed = 0
        self.xspeed = 0

    def draw(self, win, width, height):
        minimumx = self.radius
        maximumx = width - self.radius
        minimumy = self.radius
        maximumy = height - self.radius
        
        if self.xspeed >= 0 and self.xspeed != 0:
            self.xspeed -= self.vx
        elif self.xspeed < 0 and self.xspeed != 0:
            self.xspeed += self.vx
        self.x += self.xspeed
        
        self.yspeed += self.vy
        self.y += self.yspeed

        self.collision(width, height, minimumx, maximumx, minimumy, maximumy)

        if self.x >= maximumx:
            self.x = maximumx
        if self.y >= maximumy:
            self.y = maximumy

        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def collision(self, width, height, xmin, xmax, ymin, ymax):
        if self.x <= xmin or self.x >= xmax:
            self.xspeed *= -1
            if self.xspeed >= 0 and self.xspeed != 0:
                self.xspeed -= self.vx
            elif self.xspeed < 0 and self.xspeed != 0:
                self.xspeed += self.vx           
            self.x += self.xspeed
        elif self.y >= ymax:
            self.yspeed *= -1
            self.yspeed += self.vy
            self.y += self.yspeed
    
    def addForce(self, pos):
        if (pos[0] <= self.x + self.radius and pos[0] >= self.x - self.radius) and (pos[1] <= self.y + self.radius and pos[1] >= self.y - self.radius):
            if self.xspeed <= 0: 
                self.xspeed -= random.randint(5,10)
            else:
                self.xspeed += random.randint(5,10)
            if self.yspeed <= 0:
                self.yspeed -= random.randint(10,20)
            else:
                self.yspeed += random.randint(10,20)