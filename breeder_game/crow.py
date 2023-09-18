import utils

class Crow:
    def __init__(self, game, pos=[100, 5]):
        self.game = game
        self.pos = pos
        self.image = utils.load_image("crow.png")

    def update(self):
       pass
    def render(self):
        self.game.screen.blit(self.image, self.pos)
