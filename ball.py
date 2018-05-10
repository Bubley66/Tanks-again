import pygame

def sum_vectors(v,w):
    return (v[0] + w[0], v[1] + w[1])




class Ball():
    def __init__(self, color, x, y):
        self.radius = 8
        self.pos = (x,y)
        self.velocity = (0, -20)
        self.color = color

    def bounce(self):
        self.y_velocity = -20
        self.velocity = (self.velocity[0], -20)
    def update(self):
        self.pos = sum_vectors(self.pos, self.velocity)
        self.velocity = sum_vectors(self.velocity, (0, 1))

    def draw(self, s):
        pygame.draw.circle(s, self.color, self.pos, self.radius)