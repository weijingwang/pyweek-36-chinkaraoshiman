import pygame
import sys
import utils
from wolf import Wolf

from crow import Crow
from rats import Rat

class BreederGame:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('pyweek36')
        self.screen = pygame.display.set_mode((1280, 720))

        self.clock = pygame.time.Clock()
        
        self.movement = [False, False]

        self.bg = utils.load_image("02-breeding-room.png")

        self.player = Wolf(self)

        self.done = False

        self.crow = Crow(self)
        self.rat = Rat(self)


    def run(self):
        while not self.done:
            self.screen.fill((34, 30, 80))
            self.player.update(self.movement)
            self.player.render()
            self.screen.blit(self.bg, (0, 0))

            self.crow.render()
            self.rat.render()

            self.player.shadow()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            # self.screen.blit(pygame.transform.scale(self.screen, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

BreederGame().run()