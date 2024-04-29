import pygame
from constants import *
import random
from utils import RenderText

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.radius = 60
        self.speed = 0.008
        
        self.v1 = random.randint(-100, 100)
        self.v2 = random.randint(-100, 100)
        self.value = self.v1 + self.v2
        self.equation = f"{self.v1}" + (f"{self.v2}"  if self.v2 < 0 else f"+{self.v2}")

    def update(self):
        self.dx += random.uniform(-1, 1) / 50
        self.dy += self.speed

        self.x += self.dx
        self.y += self.dy

        if self.x < 0 :
            self.x = 0
            self.dx = 0
        elif self.x > WIDTH:
            self.x = WIDTH
            self.dx = 0
    
    def render(self, screen, font):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

        RenderText(screen, self.equation, font, WHITE, self.x, self.y)
