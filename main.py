#main game is platformer
#player jumps and stands on walls
#player can shoot gun really fast
#enemies will attack player when in range, otherwise, walk around
#bullets
#player can talk to npcs
#player moves to room/change level by going though a door

import sys

import pygame

class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption('pyweek 36')
        self.screen = pygame.display.set_mode((1280, 720))

        self.clock = pygame.time.Clock()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()