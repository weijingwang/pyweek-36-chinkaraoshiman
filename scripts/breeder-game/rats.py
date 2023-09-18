import utils

class Rat:
    def __init__(self, game, pos=[30, 300]):
        self.game = game
        self.pos = pos
        self.image = utils.load_image("mouse.png")

    def update():
       pass
    def render(self):
        self.game.screen.blit(self.image, self.pos)
