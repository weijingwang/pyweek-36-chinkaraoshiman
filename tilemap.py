import pygame

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        # define level here
        for i in range(50):
            self.tilemap[str(3+i) + ',10'] = {'type': 'stone', 'pos': (3+ i, 10)}

    def tiles_around(self, pos):
        tiles = []
        grid_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        around_list = [(-1,0), (-1,-1), (-1,1), (0,-1), (0,0), (0,1), (1,1), (1,0), (1,-1)]
        for off in around_list:
            around = str(grid_loc[0] + off[0]) + "," + str(grid_loc[1] + off[1])
            if around in self.tilemap:
                tiles.append(self.tilemap[around])
        return tiles

    def rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects

    def render(self, surface):
        for t in self.tilemap:
            tile = self.tilemap[t]
            surface.blit(self.game.assets[tile['type']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))