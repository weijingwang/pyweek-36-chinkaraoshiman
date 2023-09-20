class Tilemap:
    def __init__(self, game, tile_size=32):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        # define level here
        for i in range(50):
            self.tilemap[str(i) + ';15'] = {'type': 'stone', 'pos': (i, 15)}

    def render(self, surface):
        for t in self.tilemap:
            tile = self.tilemap[t]
            surface.blit(self.game.assets[tile['type']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))