import pygame

# things that can block the player
ENV_BLOCKS = ['stone', 'grass', 'checkpoint', 'brick1', 'brick2', 'brick3', 'brick4', 'brick5']

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}

        # define level here
        # decrease first number to move tiles left
        # decrease second number to move tiles up

        
        """self.tilemap['8,2'] = {'type': 'tree2', 'pos': (8,2)}
        self.tilemap['10,2'] = {'type': 'tree2', 'pos': (10,2)}
        self.tilemap['12,2'] = {'type': 'tree2', 'pos': (12,2)}
        self.tilemap['14,2'] = {'type': 'tree2', 'pos': (14,2)}"""


        for i in range(-30,30):
            # the index should be a string, and the info stored should be a dictionary
            self.tilemap[str(1+i) + ',10'] = {'type': 'brick5', 'pos': (1+i, 10)}
            self.tilemap[str(1+i) + ',11'] = {'type': 'brick5', 'pos': (1+i, 11)}
            self.tilemap[str(1+i) + ',12'] = {'type': 'brick5', 'pos': (1+i, 12)}
            #self.tilemap['6,' + str(4+i)] = {'type': 'brick2', 'pos': (6, 4+i)}
        for i in range(30):
            self.tilemap[str(4+i) + ',9'] = {'type': 'brick5', 'pos': (4+i, 9)}
            self.tilemap[str(5+i) + ',8'] = {'type': 'brick5', 'pos': (5+i, 8)}
            self.tilemap[str(6+i) + ',7'] = {'type': 'brick5', 'pos': (6+i, 7)}
            self.tilemap[str(7+i) + ',6'] = {'type': 'brick4', 'pos': (7+i, 6)}
        self.tilemap['0,10'] = {'type': 'checkpoint', 'pos': (0,10)} 

        self.tilemap['10,4'] = {'type': 'house', 'pos': (10,4)}
        self.tilemap['12,5'] = {'type': 'fence', 'pos': (12,5)} 
        self.tilemap['13,5'] = {'type': 'fence', 'pos': (13,5)} 

        for i in range(-30, 5):
            self.tilemap[str(i) + ',6'] = {'type': 'brick4', 'pos': (i, 6)}

    def tiles_around(self, pos):
        """
        Return all tiles around a given position.

        Helper function for rects_around()
        """
        tiles = []
        # floor divisions to go from pixels to grid location
        grid_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        around_list = [(-1,0), (-1,-1), (-1,1), (0,-1), (0,0), (0,1), (1,1), (1,0), (1,-1)]
        for off in around_list:
            around = str(grid_loc[0] + off[0]) + "," + str(grid_loc[1] + off[1])
            if around in self.tilemap:
                tiles.append(self.tilemap[around])
        return tiles

    def rects_around(self, pos):
        """
        Return all rects of tiles around a position.

        Used mostly for collision checking.
        """
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in ENV_BLOCKS: 
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects

    def render(self, surface, offset):
        """
        Render tiles that are in the camera's view.
        """ 
        for x in range(offset[0] // self.tile_size, (offset[0] + surface.get_width()) // self.tile_size + 1):
            for y in range(offset[1] // self.tile_size, (offset[1] + surface.get_height()) // self.tile_size + 1):
                str_index = str(x) + ',' + str(y)
                if str_index in self.tilemap:
                    tile = self.tilemap[str_index]
                    surface.blit(self.game.assets[tile['type']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))