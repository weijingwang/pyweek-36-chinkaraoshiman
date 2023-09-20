import pygame

class Object:
    def __init__(self, game, etype, pos, size):
        self.game = game
        self.type = etype
        self.pos = list(pos)
        self.size = size
        self.vel = [0,7] # 7 is gravity, goes down the screen


    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement=(0,0)):
        movement_tuple = (movement[0] + self.vel[0], movement[1] + self.vel[1])
        
        self.pos[0] += movement_tuple[0]
        
        # check tiles around for collision
        # use current position
        # 
        self_rect = self.rect()
        around = tilemap.tiles_around()
        self.pos[1] += movement_tuple[1]

    def render(self, surface):
        surface.blit(self.game.assets['player'], self.pos)