import pygame
import random
from platformer.tilemap import Tilemap
from utils import CounterText

class Object:
    def __init__(self, game, etype, pos, size):
        self.game = game
        self.type = etype
        self.pos = list(pos)
        self.size = size
        self.vel = [0,0]
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement=(0,0)):
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}
        movement_tuple = (movement[0] + self.vel[0], movement[1] + self.vel[1])
        
        # check tiles around for collision
        # use current position
        self.pos[0] += movement_tuple[0]
        self_rect = self.rect()
        for rect in tilemap.rects_around(self.pos):
            if self_rect.colliderect(rect):
                if movement_tuple[0] > 0:
                    self_rect.right = rect.left
                    self.collisions['right'] = True
                if movement_tuple[0] < 0:
                    self_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = self_rect.x

        self.pos[1] += movement_tuple[1]
        self_rect = self.rect()
        for rect in tilemap.rects_around(self.pos):
            if self_rect.colliderect(rect):
                if movement_tuple[1] > 0:
                    self_rect.bottom = rect.top
                    self.collisions['down'] = True
                if movement_tuple[1] < 0:
                    self_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = self_rect.y

        self.vel[1] = min(5, self.vel[1] + 0.1)

        if self.collisions['down'] or self.collisions['up']:
            self.vel[1] = 0

    def render(self, surface, offset):
        surface.blit(self.game.assets[self.type], (self.pos[0] - offset[0], self.pos[1] - offset[1]))


class Player(Object):
    def __init__(self, game, etype, pos, size):
        super().__init__(game, etype, pos, size)
    
    def touching_checkpoint(self):
        tilemap = self.game.tilemap
        tile_size = tilemap.tile_size
        
        for tile in tilemap.tiles_around(self.pos):
            if (tile['type'] == 'checkpoint'):
                if self.rect().colliderect(pygame.Rect(tile['pos'][0] * tile_size - 1, tile['pos'][1] * tile_size - 1, tile_size + 2, tile_size + 2)):
                    return True
        return False
        

"""
Spawn items which will drop down to the ground
(kinda hard to fine tune each item rects, so for now they will be same sizes and drop down)
"""
class Item(Object):
    def __init__(self, game, pos, size):
        item_type = random.choice(game.ALL_ITEMS)
        self.on_ground = False
        super().__init__(game, item_type, pos, size)

    def update(self):
        if self.touching_player():
            self.game.items.remove(self)
        
        if not self.on_ground:
            self.ground_collision = False

            gravity = self.vel[1]
            
            tilemap = self.game.tilemap

            self.pos[1] += gravity
            self_rect = self.rect()
            for rect in tilemap.rects_around(self.pos):
                if self_rect.colliderect(rect):
                    self_rect.bottom = rect.top
                    self.ground_collision = True
                    self.pos[1] = self_rect.y

            self.vel[1] = min(5, self.vel[1] + 0.1)

            if self.ground_collision:
                self.vel[1] = 0
                self.on_ground = True

    def touching_player(self):
        return self.rect().colliderect(self.game.player.rect())

    

class Rat(Object):
    def __init__(self, game, etype, pos, size):
        """self.range = range
        self.last_move = 0"""
        super().__init__(game, etype, pos, size)

    def update(self):
        if self.touching_player():
            self.game.rats.remove(self)
        
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}

        # only x movement should be random, y should be 0 as it doesn't jump.
        movement = [0,0]
        movement_tuple = (movement[0] + self.vel[0], movement[1] + self.vel[1])
        
        tilemap = self.game.tilemap

        # y code is still here for gravity.
        self.pos[1] += self.vel[1]
        self_rect = self.rect()
        for rect in tilemap.rects_around(self.pos):
            if self_rect.colliderect(rect):
                if movement_tuple[1] > 0:
                    self_rect.bottom = rect.top
                    self.collisions['down'] = True
                if movement_tuple[1] < 0:
                    self_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = self_rect.y

        self.vel[1] = min(5, self.vel[1] + 0.1)

        if self.collisions['down'] or self.collisions['up']:
            self.vel[1] = 0
    def touching_player(self):
        return self.rect().colliderect(self.game.player.rect())