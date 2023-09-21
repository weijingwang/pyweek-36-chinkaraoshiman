import pygame

# things that can block the player
ENV_BLOCKS = ['stone', 'grass']

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        # define level here
        for i in range(50):
            #decrease first number to move tiles left
            #decrease second number to move tiles up
            self.tilemap[str(0+i) + ',6'] = {'type': 'stone', 'pos': (0+ i, 6)}
            self.tilemap['6,' + str(3+i)] = {'type': 'stone', 'pos': (6, 3+i)}

    def tiles_around(self, pos):
        tiles = []
        # floor divisions to go from tiles to grid location
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
            if tile['type'] in ENV_BLOCKS: 
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects

    def render(self, surface, offset):
        for tile in self.offgrid_tiles:
            surface.blit(self.game.assets[tile['type']], (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))
            
        for x in range(offset[0] // self.tile_size, (offset[0] + surface.get_width()) // self.tile_size + 1):
            for y in range(offset[1] // self.tile_size, (offset[1] + surface.get_height()) // self.tile_size + 1):
                loc = str(x) + ',' + str(y)
                if loc in self.tilemap:
                    tile = self.tilemap[loc]
                    surface.blit(self.game.assets[tile['type']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))