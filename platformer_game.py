import sys

from platformer.entities import Player, Rat, Item
from platformer.tilemap import Tilemap
from utils import load_image
from utils import CounterText

import pygame

class Game:
    def __init__(self, screen):
        self.can_play_music = False
        # pygame.init()

        # pygame.display.set_caption('platformer')
        
        self.screen = screen
        #i think this is a good resolution 3:1 ratio
        self.display = pygame.Surface((1280/3, 720/3))
        
        self.clock = pygame.time.Clock()
        
        self.assets = {
            'player': pygame.transform.scale(load_image('platformer/player.png'), (16,30)),
            'stone': pygame.transform.scale(load_image('platformer/shadow.png'), (32,32)),
            'checkpoint': pygame.transform.scale(load_image('platformer/shadow.png'), (32,32)),
            'grass': pygame.transform.scale(load_image('platformer/shadow.png'), (32,32)),
            'rat': load_image('platformer/rat.png'),
            'brick1': load_image('platformer/brick1.png'),
            'brick2': load_image('platformer/brick2.png'),
            'brick3': load_image('platformer/brick3.png'),
            'brick4': load_image('platformer/brick4.png'),
            'brick5': load_image('platformer/brick5.png'),
            'dogfood': load_image('platformer/dogfood.png'),
            'potion': load_image('platformer/potion.png'),
            'tree': pygame.transform.scale(load_image('platformer/tree.png'), (64, 128)),
            'tree2': pygame.transform.scale(load_image('platformer/tree2.png'), (64, 128))
        }
    
        self.tilemap = Tilemap(self, tile_size=32)
        
        self.scroll = [0,0]

        self.movement = [False, False]

        self.player = Player(self, 'player', (100, 100), (16, 30))

        self.ALL_ITEMS = ['dogfood', 'potion']
        self.rats = [Rat(self, 'rat', (100, 150), (15, 16)), Rat(self, 'rat', (90, 150), (15, 16))]
        self.items = [Item(self, (110, 150), (32,32)), Item(self, (130, 150), (32,32))]

        self.pickup_rat = False
        self.pickup_item = False
        

    def run(self):
        while True:
            self.display.fill((156, 153, 78))
            
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 20
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 20
            camera = (int(self.scroll[0]), int(self.scroll[1]))

            # define map tiles and mobs here
            # tiles: in Tilemap
            # rats, npcs, enemies, items: render and update here 
            self.tilemap.render(self.display, offset=camera)

            for rat in self.rats:
                rat.update()
                rat.render(self.display, offset=camera)
            
            for item in self.items:
                item.update()
                item.render(self.display, offset=camera)


            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=camera)
            
            if self.player.touching_checkpoint():
                # do stuff
                # save coordinates
                # go back to rat breeder game
                print("touch")
                pass

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
