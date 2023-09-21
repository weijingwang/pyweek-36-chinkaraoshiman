import utils
# from random import randrange
MAX_VELOCITY = 10
MIN_VELOCITY = 0
ACCELERATION_SCALAR = 0.1
# JERK_SCALAR = 0.1

class Wolf:
    def __init__(self, game, pos=[826, 5]):
        self.game = game
        # self.image = utils.load_image("breeder/player_wolf.png")
        # self.image = utils.load_image("breeder/man.png")

        # self.image_shadow = utils.load_image("breeder/player/wolf_shadow.png")
        # self.image_shadow = utils.load_image("breeder/player/man-s.png")

        self.images = (
            utils.load_image("breeder/player/man.png"),
            utils.load_image("breeder/player/wolf1.png"),
            utils.load_image("breeder/player/wolf2.png"),
            utils.load_image("breeder/player/wolf3.png"),
            utils.load_image("breeder/player/wolf4.png")
        )
        self.image_shadows = (#shadows are 30% transparency
            utils.load_image("breeder/player/man-s.png"),
            utils.load_image("breeder/player/wolf1-s.png"),
            utils.load_image("breeder/player/wolf2-s.png"),
            utils.load_image("breeder/player/wolf3-s.png"),
            utils.load_image("breeder/player/wolf4-s.png")
        )
        self.image_change_counter = 0
        self.image = self.images[0]
        self.image_shadow = self.image_shadows[0]

        self.velocity_scalar = 0
        self.pos = pos
        self.direction = 'up'
        self.bounce_count = 0

    def bouncing(self):
        if self.direction == 'up':
            self.pos[1] -= 0.2
            self.bounce_count += 0.2
            if self.bounce_count >= 20:
                self.direction = 'down'
                self.bounce_count = 0

        elif self.direction == 'down':
            self.pos[1] += 0.2
            self.bounce_count += 0.2
            if self.bounce_count >= 20:
                self.direction = 'up'
                self.bounce_count = 0
        # print(self.bounce_count, self.direction)
        
    
    def update(self, movement):
        self.bouncing()
        #left 0, right 1
        frame_movement = (movement[0]*-1, movement[1])

        self.pos[0] += (frame_movement[0] + frame_movement[1])*self.velocity_scalar

        if self.pos[0] < -100:
            self.pos[0] = -100

        # print(self.velocity_scalar)

        if (frame_movement[0]+frame_movement[1]) == 1:
            #if moving in RIGHT direction
            if self.velocity_scalar<=MAX_VELOCITY*1:
                self.velocity_scalar += ACCELERATION_SCALAR
            else:
                self.velocity_scalar = MAX_VELOCITY

        elif (frame_movement[0]+frame_movement[1]) == -1:
            #if moving in LEF direction
            if self.velocity_scalar<=MAX_VELOCITY*1:
                self.velocity_scalar += ACCELERATION_SCALAR
            else:
                self.velocity_scalar = MAX_VELOCITY
        else:
            self.velocity_scalar = 2
            #would like a slow down
        #     if self.velocity_scalar >= 0:
        #         self.velocity_scalar -= ACCELERATION_SCALAR
        #     frame_movement = (1,0)
        # print(self.velocity_scalar)
    def render(self):
        self.game.screen.blit(self.image, self.pos)
    def shadow(self):
        self.game.screen.blit(self.image_shadow, (self.pos[0],self.pos[1]+300))
    def refresh_image(self):
        # my_choice = randrange(1,4)
        self.image = self.images[self.image_change_counter]
        self.image_shadow = self.image_shadows[self.image_change_counter]
        if self.image_change_counter < (len(self.images)-1): self.image_change_counter += 1
        else: self.image_change_counter = 1
