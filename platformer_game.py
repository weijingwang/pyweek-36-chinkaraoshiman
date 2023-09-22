import sys

from platformer.entities import Object
from platformer.tilemap import Tilemap
from utils import load_image

import pygame

class Game:
    def __init__(self, screen):
        pygame.init()

        pygame.display.set_caption('platformer')
        
        self.screen = screen
        #i think this is a good resolution 3:1 ratio
        self.display = pygame.Surface((1280/3, 720/3))
        #or maybe this one
        #can change this for testing code
        self.display = pygame.Surface((1280/2, 720/2))
        
        self.clock = pygame.time.Clock()
        
        self.assets = {
            'player': pygame.transform.scale(load_image('platformer/player.png'), (16,30)),
            'stone': pygame.transform.scale(load_image('platformer/shadow.png'), (32,32)),
            'grass': pygame.transform.scale(load_image('platformer/shadow.png'), (32,32)),

        }
    
        self.tilemap = Tilemap(self, tile_size=32)
        
        self.scroll = [0,0]

        self.movement = [False, False]

        self.player = Object(self, 'player', (100, 100), (16, 30))

    def run(self):
        self.display.fill((156, 153, 78))
        
        self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 20
        self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 20
        camera = (int(self.scroll[0]), int(self.scroll[1]))

        self.tilemap.render(self.display, offset=camera)
        
        self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
        self.player.render(self.display, offset=camera)
        
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


