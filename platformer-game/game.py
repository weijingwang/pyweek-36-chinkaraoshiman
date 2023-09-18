import sys

import pygame

from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('pyweek36')
        self.screen = pygame.display.set_mode((1280, 720))
        # self.display = pygame.Surface((1280, 720))

        self.clock = pygame.time.Clock()
        
        self.movement = [False, False]
        
        self.assets = {
            # 'decor': load_images('tiles/decor'),
            'grass': load_images(''),
            # 'large_decor': load_images('tiles/large_decor'),
            'stone': load_images(''),
            'player': load_image('player.png')
        }
        
        self.player = PhysicsEntity(self, 'player', (50*5, 50*5), (8*5, 15*5))
        
        self.tilemap = Tilemap(self, tile_size=16*5)
        self.scroll = [0, 0]

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            
            self.scroll[0] += (self.player.rect().centerx - self.screen.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.screen.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            self.tilemap.render(self.screen, offset=render_scroll)
            
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen, offset=render_scroll)
            
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
                        self.player.jump()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            # self.screen.blit(pygame.transform.scale(self.screen, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()