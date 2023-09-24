import pygame
import random

# things that can block the player
ENV_BLOCKS = ['checkpoint', 'brick1', 'brick2', 'brick3', 'brick4', 'brick5', 'dirt', 'grass']

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}

        # define level here
        # decrease first number to move tiles left
        # decrease second number to move tiles up
        # the index should be a string, and the info stored should be a dictionary

        # starting checkpoint
        self.tilemap['0,10'] = {'type': 'checkpoint', 'pos': (0,10)} 

        self.left_side()
        self.right_side()

    def left_side(self):
        # LEFT SIDE terrains
        self.make_row(-10, 6, 15, 'brick3')
        self.make_row(-10, 7, 12, 'brick5')
        self.make_row(-10, 8, 10, 'brick5')
        self.make_row(-10, 9, 10, 'brick5')
        self.make_row(-10, 10, 40, 'brick5')
        self.make_row(-10, 11, 40, 'brick5')
        self.make_row(-10, 12, 40, 'brick5')

        # make bridge
        self.make_col(-11, 6, 8, 'brick2')
        self.make_col(-12, 5, 3, 'brick2')
        self.make_col(-13, 4, 3, 'brick2')
        self.make_row(-25, 4, 12, 'brick2')
        self.make_row(-25, 5, 12, 'brick2')
        self.make_row(-25, 3, 12, 'fence')
        self.make_col(-26, 4, 3, 'brick2')
        self.make_col(-27, 5, 3, 'brick2')
        self.make_col(-28, 6, 8, 'brick2')

        # make forest ground terrain
        """self.make_row(-40, 6, 8, 'dirt')
        self.make_row(-40, 7, 8, 'dirt')
        self.make_row(-40, 8, 8, 'dirt')"""
        self.make_row(-32, 6, 4, 'brick3')
        self.make_row(-32, 7, 4, 'brick4')
        self.make_row(-32, 8, 4, 'brick4')
        self.make_row(-32, 9, 4, 'brick4')

        self.make_row(-60, 6, 28, 'grass')
        self.make_row(-75, 6, 9, 'grass')
        self.make_row(-75, 7, 43, 'dirt')
        self.make_row(-75, 8, 43, 'dirt')
        self.make_row(-75, 9, 43, 'dirt')

        # forest trees
        self.trees(-60, 6, 26)

        # forest house
        self.house_unit1(-68, 4)
        self.tilemap['-66,6'] = {'type': 'checkpoint', 'pos': (-66,6)}

        # castle wall
        self.make_col(-78, -4, 11, 'brick1')
        self.make_col(-77, -4, 11, 'brick1')
        self.make_col(-76, -4, 11, 'brick1')
        self.make_col(-78, 7, 4, 'dirt')
        self.make_col(-77, 7, 4, 'dirt')
        self.make_col(-76, 7, 4, 'dirt')
        
        self.make_row(-82, 6, 4, 'brick3')
        self.make_row(-82, 7, 4, 'brick4')
        self.make_row(-82, 8, 4, 'brick4')
        self.make_row(-82, 9, 4, 'brick4')

    def right_side(self):
        # RIGHT SIDE OF THE BEGINNING CHECKPOINT
        # this is the ground terrain
        self.make_row(4, 9, 100, 'brick5')
        self.make_row(5, 8, 101, 'brick5')
        self.make_row(6, 7, 102, 'brick5')
        self.make_row(7, 6, 103, 'brick3')
        self.make_row(104, 9, 8, 'dirt')
        self.make_row(104, 8, 8, 'dirt')
        self.make_row(104, 7, 8, 'dirt')
        self.make_row(104, 6, 8, 'dirt')

        # this is the houses
        self.house_unit1(15, 4)
        self.house_unit2(25, 4)
        self.house_unit1(35, 4)
        self.house_unit2(45, 4)
        self.house_unit1(55, 4)
        self.house_unit2(65, 4)
        self.house_unit1(75, 4)
        self.house_unit2(85, 4)

        # this is the castle wall
        self.make_col(101, -4, 10, 'brick1')
        self.make_col(102, -4, 10, 'brick1')
        self.make_col(103, -4, 10, 'brick1')

        # this is the checkpoint at the house
        self.tilemap['57,6'] = {'type': 'checkpoint', 'pos': (57,6)} 

    """
    start adding random trees from given position.
    """
    def trees(self, x, y, amount):
        for i in range(amount):
            if i % 2 == 0:
                tree_type = random.choice(['tree', 'tree2'])
                self.tilemap[str(x+i) + "," + str(y-4)] = {'type': tree_type, 'pos': (x+i,y-4)}

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