import utils
from random import getrandbits

class Crow:
    def __init__(self, game, pos=[0, 0]):
        self.game = game
        self.pos = pos
        self.image = utils.load_image("breeder/crow.png")
        self.rect = self.image.get_rect()

        self.come = False
        self.moving = False
        self.SPEED = 6

        self.state = 'wait'
        # wait, hover, attack

    def mouse_inputs(self, pos):
        if self.rect.collidepoint(pos):

            self.pos = [0,0]
            self.come = False

    def update(self):
        #spawn crow?
        if not self.come:
            if getrandbits:
                self.come = True
        if self.come == True:
            
            if self.pos[0] <= 300:
                self.pos[0]+=self.SPEED
            if self.pos[1] <= 450:
                self.pos[1]+=self.SPEED
            if self.pos[0] >= 300 and self.pos[1] >= 450:
                self.come = False
            
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]

    

    def render(self):


        self.game.screen.blit(self.image, self.pos)
    def eat_rat(self,rat_count):
        #do once every rat spawn cylce only
        if getrandbits:
            rat_count -= 1

