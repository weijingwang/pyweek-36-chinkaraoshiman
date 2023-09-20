import utils
from random import getrandbits

class Crow:
    def __init__(self, game, pos=[0, 0]):
        self.game = game
        self.pos = pos
        self.image = utils.load_image("breeder/crow.png")
        self.rect = self.image.get_rect()

        self.moving = False
        self.SPEED = 6

        self.state = 'wait'
        # wait, taunt, attack

    def mouse_inputs(self, pos):
        if self.rect.collidepoint(pos):
            print('kill')
            self.state = "wait"
            self.pos = [0,0]
            self.moving= False

    def update_states(self):
        #update this every so many cylces
        print(self.state)

        if not self.moving:
            if self.state == 'wait':
                if getrandbits(1):
                    self.state = 'taunt'
                    self.moving = True
            elif self.state == 'taunt':
                if getrandbits(1): self.state = 'attack'


    def update(self):
        #spawn crow?
        if self.state == 'taunt' and self.moving:
            if self.pos[0] <= 300:
                self.pos[0]+=self.SPEED
            if self.pos[1] <= 450:
                self.pos[1]+=self.SPEED
            if self.pos[0] >= 300 and self.pos[1] >= 450:
                self.moving = False
            
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]

    

    def render(self):

        self.game.screen.blit(self.image, self.pos)

    def eat_rat(self,rat_count):
        #do once every rat spawn cylce only
        if self.state == 'attack':
            if getrandbits(1):
                rat_count -= 1

