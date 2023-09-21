import utils
from random import getrandbits, uniform, choice, randrange

class Crow:
    def __init__(self, game):
        self.size = (240, 160)
        self.crow_cage = ((10,770),(400,500))

        self.game = game
        self.pos = [randrange(-200,1280), -200]
        self.destination = [randrange(*self.crow_cage[0]), randrange(*self.crow_cage[1])]
        #sprite img
        self.animation_loop = 0
        self.cursor_crow = utils.load_image("breeder/cursor.png")
        self.cursor_rect = self.cursor_crow.get_rect()
        
        self.sprites = utils.Spritesheet("breeder/crow-fly.png")
        self.sprites_attack = utils.Spritesheet("breeder/crow-attack.png")
        self.taunt_animation = (
            self.sprites.get_sprite(0, 0, 240, 160),
            self.sprites.get_sprite(240, 0, 240, 160),
            self.sprites.get_sprite(480, 0, 240, 160),
            self.sprites.get_sprite(240*3, 0, 240, 160),
            self.sprites.get_sprite(240*4, 0, 240, 160),
            self.sprites.get_sprite(240*5, 0, 240, 160)
        )
        self.attack_animation = (
            self.sprites_attack.get_sprite(0, 0, *self.size),
            self.sprites_attack.get_sprite(240, 0, *self.size),
            self.sprites_attack.get_sprite(480, 0, *self.size),
            self.sprites_attack.get_sprite(720, 0, *self.size),
            self.sprites_attack.get_sprite(0, 0, *self.size),
            self.sprites_attack.get_sprite(240, 0, *self.size)
        )
        self.animation = self.taunt_animation
        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        self.timer = 0
        self.moving = False
        self.SPEED = 6

        self.state = 'wait'
        # wait, taunt, attack

        self.DX_val = 10
        self.DY_val = 5
        self.wait_timer = 0
        self.MAX_WAIT = 5
        self.wait_time = randrange(1, self.MAX_WAIT)
        #set new scalars and directions
        self.dx = uniform(-self.DX_val,self.DX_val) * choice((-1,1))
        self.dy = uniform(-self.DY_val,self.DY_val) * choice((-1,1))
        self.move_time = uniform(1,10) #0.02 is lowest
        self.move = getrandbits(1)

    def animate_update(self):
        if self.animation_loop > len(self.animation):
            self.animation_loop = 0

        if self.state == 'attack':
            self.animation = self.attack_animation
        # if self.state == 'taunt':
        else:
            self.animation = self.taunt_animation

        self.image = self.animation[int(self.animation_loop)]
        self.animation_loop += 0.1


    def mouse_inputs(self, pos):
        if self.rect.collidepoint(pos):
            # print('kill')
            self.state = "wait"
            self.pos = [randrange(-200,1280), -200]
            self.destination = [randrange(*self.crow_cage[0]), randrange(*self.crow_cage[1])]
            self.moving= False

    def update_states(self):
        #update this every so many cylces
        # print(self.state)

        if not self.moving:
            if self.state == 'wait' and self.wait_timer < self.wait_time:
                self.wait_timer += 1
                if self.wait_timer >= self.wait_time:
                    self.state = 'taunt'
                    self.moving = True
                    self.wait_timer = 0
                    self.wait_time = randrange(1,self.MAX_WAIT)
            elif self.state == 'taunt':
                if getrandbits(1): self.state = 'attack'




    def update(self):
        #spawn crow?
        if self.state == 'taunt' and self.moving:
            if self.pos[0] <= self.destination[0]:
                self.pos[0]+=self.SPEED
            if self.pos[0] > self.destination[0]:
                self.pos[0]-=self.SPEED
            if self.pos[1] <= self.destination[1]:
                self.pos[1]+=self.SPEED
            if self.pos[1] >= self.destination[1]:
                self.moving = False
                self.state = 'attack'
            self.rect.x = self.pos[0]
            self.rect.y = self.pos[1]

        elif self.state == 'attack':
            self.eating_update_movement()

    

    def render(self):
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.game.screen.blit(self.image, self.pos)

    def render_cursor(self, pos):
        if self.rect.collidepoint(pos):
            self.cursor_rect.center = pos
            self.game.screen.blit(self.cursor_crow, self.cursor_rect)

    # def eat_rat(self,rat_count):
    #     #do once every rat spawn cylce only
    #     if self.state == 'attack':
    #         if getrandbits(1):
    #             rat_count -= 1

    def eating_update_movement(self):
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

                if self.pos[0] < self.crow_cage[0][0]:
                    #rat cage left
                    self.pos[0] = self.crow_cage[0][0]
                    self.dx *= -1
                if self.pos[0] > self.crow_cage[0][1]:
                    #rat cage right
                    self.pos[0] = self.crow_cage[0][1]
                    self.dx *= -1        
                if self.pos[1] < self.crow_cage[1][0]:
                    #rat cage up
                    self.pos[1] = self.crow_cage[1][0]
                    self.dy *= -1
                if self.pos[1] > self.crow_cage[1][1]:
                    #rat cage down
                    self.pos[1] = self.crow_cage[1][1]
                    self.dy *= -1        
                    

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