import cmath
import pygame
from conf import WHITE, WIDTH, HEIGHT
from math import radians

class Bullet:
    def __init__(self, pos, vel, dir):
        self.pos = pos
        self.vel = vel
        self.dir = dir
        self.radius = 4
        self.color = WHITE

    def collides_with_player(self, p):
        a = self
        b = p
        d = b.pos - a.pos
        distance = abs(d)
        #print(distance)
        if distance < a.radius + b.radius:
            return True
        else:
            return False

    def is_outside_screen(self):
        return WIDTH <= self.pos.real + self.radius or \
               HEIGHT <= self.pos.imag + self.radius or \
               self.pos.real - self.radius < 0 or \
               self.pos.imag - self.radius < 0

    def draw(self, sur):
        pygame.draw.circle(sur, self.color, (int(self.pos.real), int(self.pos.imag)), self.radius)

    def update(self):
        step = cmath.rect(self.vel, radians(self.dir))
        self.pos += step
