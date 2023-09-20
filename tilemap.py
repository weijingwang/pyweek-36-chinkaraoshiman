import pygame

class Tilemap:
    def __init__(self, game, tile_size=32):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        # define level here
        for i in range(50):
            self.tilemap[str(i) + ',15'] = {'type': 'stone', 'pos': (i, 15)}
    
    def tiles_acround(self, pos):
        tiles = []
        grid_loc = (pos[0] // self.tile_size, pos[1] // self.tile_size)
        around_list = [(-1,0), (-1,-1), (-1,1), (0,-1), (0,0), (0,1), (1,1), (1,0), (1,-1)]
        for pos in around_list:
            around = str(grid_loc[0] + pos[0]) + "," + str(grid_loc[1] + pos[1])
            if around in self.tilemap:
                tiles.append(around)
        return tiles



    def render(self, surface):
        for t in self.tilemap:
            tile = self.tilemap[t]
            surface.blit(self.game.assets[tile['type']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))