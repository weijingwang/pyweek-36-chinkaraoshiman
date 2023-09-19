import utils
from random import uniform, getrandbits, choice, randrange

class Rat:
    def __init__(self, game, pos=[randrange(100,700),randrange(300,700)]):
        self.DX_val = 5
        self.DY_val = 5
        self.game = game
        self.pos = pos
        self.pos=[randrange(100,700),randrange(300,700)]
        self.image = utils.load_image("breeder/mouse.png")
        self.timer = 0
        # print(self.pos)

        #set new scalars and directions
        self.dx = uniform(-self.DX_val,self.DX_val) * choice((-1,1))
        self.dy = uniform(-self.DY_val,self.DY_val) * choice((-1,1))

        self.move_time = uniform(1,10) #0.02 is lowest
        self.move = getrandbits(1)

        if self.move == 0:
            self.moving = False
        else:
            self.moving = True

        # print(self.dx, self.dy, self.move_time, self.move)
    


    def update(self):
        # print(self.move_time)
        if self.move and not self.moving:
            self.moving = True
        elif not self.move:
            #set new scalars and directions
            self.dx = uniform(-self.DX_val,self.DX_val) * choice((-1,1))
            self.dy = uniform(-self.DY_val,self.DY_val) * choice((-1,1))
            #set new duration of move
            self.move_time = uniform(1,10)
            #will it move?
            self.move = getrandbits(1)
        if self.moving:
            if self.timer < self.move_time:
                self.pos[0] += self.dx
                self.pos[1] += self.dy
                self.timer += 1
            else:
                self.moving = False
                self.timer = 0

                #set new scalars and directions
                self.dx = uniform(-self.DX_val,self.DX_val) * choice((-1,1))
                self.dy = uniform(-self.DY_val,self.DY_val) * choice((-1,1))
                #set new duration of move
                self.move_time = uniform(1,10)
                #will it move?
                self.move = getrandbits(1)

    def render(self):
        self.game.screen.blit(self.image, self.pos)
