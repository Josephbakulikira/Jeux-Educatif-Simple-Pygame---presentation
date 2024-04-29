import pygame
from constants import *

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.speed = 60
    
    def update(self):
        self.y -= self.speed

    def render(self, screen):
        pygame.draw.circle(screen, GREEN, (self.x, self.y), self.radius)