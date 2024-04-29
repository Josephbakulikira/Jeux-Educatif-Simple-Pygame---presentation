import pygame
from constants import *
from Player import Player
from enemy import Enemy
from utils import RenderText

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("JEUX INTERACTIF - TECHNOFILE")
    clock = pygame.time.Clock()
    game = Game(screen, clock)
    # game loop 
    game.Run()



class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.fps = 30

        self.gameOver = 0
        self.score = 0
        self.mainMenu = True

        self.scoreFont = pygame.font.Font("./assets/fonts/dpcomic.ttf", 70)
        self.font = pygame.font.SysFont("consolas", 25)
        self.player = Player(WIDTH//2, HEIGHT - 50)
    
    def SetCaption(self, frame_rate):
        # Set Frame rate of the screen
        pygame.display.set_caption(f"JEUX INTERACTIF - FPS: {frame_rate}")

    def GenerateEnemies(self, n_enemies=4):
        self.player.enemies = []
        offset_value = (WIDTH - 20) // n_enemies
        for i in range(n_enemies):
            x = (i * offset_value) + offset_value // 2
            y = 0
            new_enemy = Enemy(x, y)
            self.player.enemies.append(new_enemy)
    
    def HandleEvent(self):
        # Handle user Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.player.Shoot()
    def Run(self):
        self.GenerateEnemies()
        self.player.currentValue = self.player.GetValue()
        while self.running:
            # set Frame rate
            self.clock.tick(self.fps)
            self.SetCaption(int(self.clock.get_fps()))
            self.HandleEvent()
            # Draw background
            self.screen.fill(BLACK)

            self.player.update(self.screen)
            self.player.render(self.screen, self.font)

            for enemy in self.player.enemies:
                enemy.render(self.screen, self.font)
                enemy.update()

            
            RenderText(self.screen, str(self.player.score), self.scoreFont, (255, 255, 0), WIDTH-50, HEIGHT-50)
            pygame.display.update()


if __name__ == "__main__":
    main()