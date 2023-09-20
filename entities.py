import pygame
from tilemap import Tilemap

class Mob:
    def __init__(self, game, etype, pos, size):
        self.game = game
        self.type = etype
        self.pos = list(pos)
        self.size = size
        self.vel = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        
    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        movement_tuple = (movement[0] + self.vel[0], movement[1] + self.vel[1])
        
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
        
    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)
        