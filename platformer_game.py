import sys

from platformer.entities import Mob
from platformer.tilemap import Tilemap
from platformer.util import load_img

import pygame

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('platformer')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320*2, 240*2))

        self.clock = pygame.time.Clock()
        
        self.movement = [False, False]
        
        self.assets = {
            'player': pygame.transform.scale(load_img('platformer/player.png'), (16,30)),
            'stone': pygame.transform.scale(load_img('platformer/shadow.png'), (32,32)),
            'grass': pygame.transform.scale(load_img('platformer/shadow.png'), (32,32)),

        }
        
        self.player = Mob(self, 'player', (100, 100), (16, 30))
        
        self.tilemap = Tilemap(self, tile_size=32)
        
    def run(self):
        while True:
            self.display.fill((156, 153, 78))
            
            self.tilemap.render(self.display)
            
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)
            
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
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()