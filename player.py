from entities import Mob
import pygame

#player can jump and is affected by gravity
#player shoots bullets which kills enemies
#should we include wall jumping?

class Player(Mob):
    def __init__(self, x, y, scale):
        # image var is initialized in super init
        img = pygame.image.load('assets/car.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        
        super().__init__(x,y,scale)
        self.speed = 50



    def movement(self):
        change_x = 0
        #change_y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            change_x = -self.speed
        if keys[pygame.K_RIGHT]:
            change_x = self.speed
        
        self.rect.x += change_x