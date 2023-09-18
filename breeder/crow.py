import utils
from random import getrandbits

class Crow:
    def __init__(self, game, pos=[100, 5]):
        self.game = game
        self.pos = pos
        self.image = utils.load_image("breeder/crow.png")

    def update(self):
       pass
    def render(self):
        self.game.screen.blit(self.image, self.pos)
    def eat_rat(self,rat_count):
        #do once every rat spawn cylce only
        if getrandbits:
            rat_count -= 1

