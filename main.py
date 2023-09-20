import sys

from util import load_img
from entities import Mob
from tilemap import Tilemap
import pygame

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('platformer')
        self.screen = pygame.display.set_mode((640, 480))
        

        self.clock = pygame.time.Clock()
        
        self.movement = [False, False]
        
        self.assets = {
            'player': pygame.transform.scale(load_img('player.png'), (15,20)),
            'stone': pygame.transform.scale(load_img('shadow.png'), (32,32))
        }
        
        self.player = Mob(self, 'player', (50, 50), (15, 20))
        
        self.tilemap = Tilemap(self, tile_size=16)
        
    def run(self):
        while True:
            self.screen.fill((156, 153, 78))
            
            self.tilemap.render(self.screen)
            
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.vel[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()