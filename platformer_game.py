import sys

from platformer.entities import Player, Rat, Item
from platformer.tilemap import Tilemap
from utils import load_image_platformer
from utils import load_image_platformer
from utils import CounterText

import pygame

class Game:
    def __init__(self, game, screen):
        self.game = game
        self.can_play_music = False

        self.screen = screen
        #i think this is a good resolution 3:1 ratio
        self.display = pygame.Surface((1280/3, 720/3))
        
        self.clock = pygame.time.Clock()
        
        self.assets = {
            'player': pygame.transform.scale(load_image_platformer('platformer/player.png'), (16,30)),
            'checkpoint': pygame.transform.scale(load_image_platformer('platformer/checkpoint.png', (0,0,1)), (32,32)),
            'rat': load_image_platformer('platformer/rat.png'),
            'brick1': load_image_platformer('platformer/brick1.png'),
            'brick2': load_image_platformer('platformer/brick2.png'),
            'brick3': load_image_platformer('platformer/brick3.png'),
            'brick4': load_image_platformer('platformer/brick4.png'),
            'brick5': load_image_platformer('platformer/brick5.png'),
            'dogfood': load_image_platformer('platformer/dogfood.png'),
            'potion': load_image_platformer('platformer/potion.png'),
            'tree': pygame.transform.scale(load_image_platformer('platformer/tree.png'), (64, 128)),
            'tree2': pygame.transform.scale(load_image_platformer('platformer/tree2.png'), (64, 128)),
            'house': load_image_platformer('platformer/house.png', (0,0,0)),
            'fence': load_image_platformer('platformer/fence.png'),
            'dirt': pygame.transform.scale(load_image_platformer('platformer/dirt.png'), (32, 32)),
            'grass': load_image_platformer('platformer/grass.png')
        }

        self.black_filter = load_image_platformer('black_filter.png')
    
        self.tilemap = Tilemap(self, tile_size=32)
        
        self.scroll = [0,0]

        self.movement = [False, False]

        self.player = Player(self, 'player', (100, 300), (16, 30))

        self.ALL_ITEMS = ['dogfood', 'potion']
        
        self.rats = [] #[Rat(self, 'rat', (100, 150), (15, 16)), Rat(self, 'rat', (90, 150), (15, 16))]
        self.items = [] #[Item(self, (110, 150), (32,32)), Item(self, (130, 150), (32,32)), Item(self, (250, 150), (32,32))]

        self.pickup_rat = False
        self.pickup_item = False

        self.bg = pygame.transform.scale(load_image_platformer("bg.png"), (1280/3, 720/3))
        self.bg = pygame.transform.scale(load_image_platformer("bg.png"), (1280/3, 720/3))

        

    def run(self):
        if self.can_play_music:
            pygame.mixer.stop()
            pygame.mixer.music.load("data/music/walking.ogg")
            pygame.mixer.music.play(-1)
            self.can_play_music = False
        pickup_rat_text1 = pygame.font.SysFont('Consolas', 32).render('You picked up a rat!', True, pygame.color.Color('White'))
        continue_text = pygame.font.SysFont('Consolas', 32).render('Press F to continue.', True, pygame.color.Color('White'))
        pickup_item_text1 = pygame.font.SysFont('Consolas', 32).render('You picked up an item!', True, pygame.color.Color('White'))

        while not (self.pickup_rat ^ self.pickup_item):
            self.display.blit(self.bg, (0, 0))
            self.display.blit(self.black_filter, (0,0))
            
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 20
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 20
            camera = (int(self.scroll[0]), int(self.scroll[1]))

            # define map tiles and mobs here
            # tiles: in Tilemap
            # rats, npcs, enemies, items: render and update here 
            self.tilemap.render(self.display, offset=camera)
            # define map tiles and mobs here
            # tiles: in Tilemap
            # rats, npcs, enemies, items: render and update here 
            self.tilemap.render(self.display, offset=camera)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=camera)
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=camera)

            for rat in self.rats:
                if rat.touching_player():
                    rat.update()
                    self.pickup_rat = True
                else:
                    rat.update()
                    rat.render(self.display, offset=camera)
        
            
            for item in self.items:
                if item.touching_player():
                    item.update()
                    self.pickup_item = True
                else:
                    item.update()
                    item.render(self.display, offset=camera)
            
            if self.player.touching_checkpoint():
                # do stuff
                # save coordinates
                # go back to rat breeder game
                print("touch")

                self.game.breeder.player.pos[0] = 826 #set it so that u dont constantly teleport back between breeder and platformer
                self.game.breeder.movement = [False, False]
                pygame.mixer.stop()
                pygame.mixer.music.load("data/music/breeder.mp3")
                pygame.mixer.music.play(-1)
                self.player.pos[0]+=100
                self.movement = [0,0]
                self.game.state = 'breeder'
                break
            for rat in self.rats:
                if rat.touching_player():
                    rat.update()
                    self.pickup_rat = True
                else:
                    rat.update()
                    rat.render(self.display, offset=camera)
        
            
            for item in self.items:
                if item.touching_player():
                    item.update()
                    self.pickup_item = True
                else:
                    item.update()
                    item.render(self.display, offset=camera)
            
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
    
        while self.pickup_rat:
            self.screen.blit(pickup_rat_text1, (100, 100))
            self.screen.blit(continue_text, (100, 140))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.pickup_rat = False
            pygame.display.update()
            self.clock.tick(60)
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
    
        while self.pickup_rat:
            self.screen.blit(pickup_rat_text1, (100, 100))
            self.screen.blit(continue_text, (100, 140))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.pickup_rat = False
            pygame.display.update()
            self.clock.tick(60)

        while self.pickup_item:
            self.screen.blit(pickup_item_text1, (100, 100))
            self.screen.blit(continue_text, (100, 140))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.pickup_item = False
        while self.pickup_item:
            self.screen.blit(pickup_item_text1, (100, 100))
            self.screen.blit(continue_text, (100, 140))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.pickup_item = False


