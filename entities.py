import pygame

class Object:
    def __init__(self, game, etype, pos, size):
        self.game = game
        self.type = etype
        self.pos = list(pos)
        self.size = size
        self.vel = [0,0]

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, movement=(0,0)):
        movement_tuple = (movement[0] + self.vel[0], movement[1] + self.vel[1])
        
        self.pos[0] += movement_tuple[0]
        self_rect = self.rect()

        # check tiles around for collision

        self.pos[1] += movement_tuple[1]

    def render(self, surface):
        surface.blit(self.game.assets['player'], self.pos)