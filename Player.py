import pygame
from constants import *
from bullet import Bullet
from utils import GetDistance
import random
from utils import RenderText

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 30
        self.bullets = []
        self.enemies = []
        self.speed = 30
        self.score = 0
        self.currentValue = 0 
        
    
    def update(self, screen):
        dx, dy = 0, 0
        keys = pygame.key.get_pressed()

            # Calculate the new player position
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            # Player move to the left
            dx -= self.speed
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # Player move to the right
            dx += self.speed


        self.x += dx
        self.y += dy

        for b in self.bullets:
            b.render(screen)
            b.update()
            if b.y < 0:
                self.bullets.remove(b)
            
            for enem in self.enemies:
                distance = GetDistance(b.x, b.y, enem.x, enem.y)
                if distance < enem.radius:
                    # self.enemies.remove(enem)
                    # self.currentValue = self.GetValue()
                    if self.currentValue == enem.value:
                        self.enemies.remove(enem)
                        self.currentValue = self.GetValue()
                        self.score += 1
    
    def Shoot(self):
        new_bullet = Bullet(self.x, self.y)
        self.bullets.append(new_bullet)


    def GetValue(self):
        myChoic = random.choice(self.enemies)
        
        return myChoic.value


    def render(self, screen, font):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

        # Arme
        pygame.draw.rect(screen, WHITE, pygame.Rect(self.x - self.radius//4, self.y - self.radius * 2, self.radius//2, self.radius))

        # Valeur
        RenderText(screen, str(self.currentValue), font, BLACK, self.x, self.y)
