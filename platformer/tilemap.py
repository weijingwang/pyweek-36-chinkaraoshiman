import pygame
import random

# things that can block the player
ENV_BLOCKS = ['checkpoint', 'brick1', 'brick2', 'brick3', 'brick4', 'brick5', 'dirt']

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}

        # define level here
        # decrease first number to move tiles left
        # decrease second number to move tiles up
        # the index should be a string, and the info stored should be a dictionary

        for i in range(-30,30):
            self.tilemap[str(1+i) + ',10'] = {'type': 'brick5', 'pos': (1+i, 10)}
            self.tilemap[str(1+i) + ',11'] = {'type': 'brick5', 'pos': (1+i, 11)}
            self.tilemap[str(1+i) + ',12'] = {'type': 'brick5', 'pos': (1+i, 12)}
            #self.tilemap['6,' + str(4+i)] = {'type': 'brick2', 'pos': (6, 4+i)}
        
        for i in range(-30, 5):
            self.tilemap[str(i) + ',6'] = {'type': 'brick4', 'pos': (i, 6)}

        # RIGHT SIDE OF THE BEGINNING CHECKPOINT
        self.make_row(4, 9, 100, 'brick5')
        self.make_row(5, 8, 101, 'brick5')
        self.make_row(6, 7, 102, 'brick5')
        self.make_row(7, 6, 103, 'brick3')
        self.make_row(104, 9, 8, 'dirt')
        self.make_row(104, 8, 8, 'dirt')
        self.make_row(104, 7, 8, 'dirt')
        self.make_row(104, 6, 8, 'dirt')

        self.tilemap['0,10'] = {'type': 'checkpoint', 'pos': (0,10)} 

        self.house_unit1(15, 4)
        self.house_unit2(25, 4)
        self.house_unit1(35, 4)
        self.house_unit2(45, 4)
        self.house_unit1(55, 4)
        self.house_unit2(65, 4)
        self.house_unit1(75, 4)
        self.house_unit2(85, 4)

        self.make_col(101, -4, 10, 'brick1')
        self.make_col(102, -4, 10, 'brick1')
        self.make_col(103, -4, 10, 'brick1')

        self.tilemap['37,6'] = {'type': 'checkpoint', 'pos': (37,6)} 


    """
    make a house unit starting at the given position
    each house unit is *8* tiles! useful to know
    """
    def house_unit1(self, x, y):
        self.make_row(x, y+2, 8, 'dirt')
        tree_type = random.choice(['tree', 'tree2'])
        self.tilemap[str(x) + "," + str(y-2)] = {'type': tree_type, 'pos': (x,y-2)}
        self.tilemap[str(x+2) + "," + str(y)] = {'type': 'house', 'pos': (x+2,y)}
        self.make_row(x+4, y+1, 4, 'fence')

    def house_unit2(self, x, y):
        self.make_row(x, y+2, 8, 'dirt')
        self.make_row(x, y+1, 4, 'fence')
        self.tilemap[str(x+4) + "," + str(y)] = {'type': 'house', 'pos': (x+4,y)}
        tree_type = random.choice(['tree', 'tree2'])
        self.tilemap[str(x+6) + "," + str(y-2)] = {'type': tree_type, 'pos': (x+6,y-2)}
        pass

    """
    make a row of given type starting from given x and y
    """
    def make_row(self, x, y, amount, type):
        for i in range(amount):
            self.tilemap[str(x+i) + "," + str(y)] = {'type': type, 'pos': (x+i,y)}


    """
    make a column of given type tile starting at given x and y and *goes down*.
    """
    def make_col(self, x, y, amount, type):
        for i in range(amount):
            self.tilemap[str(x) + "," + str(y+i)] = {'type': type, 'pos': (x,y+i)}




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