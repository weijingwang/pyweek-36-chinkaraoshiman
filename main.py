from breeder_game import BreederGame
import platformer_game
from displayText import counterText
import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load("data/music/breeder.mp3")
        pygame.mixer.music.play(-1)
        pygame.display.set_caption("pyweek36")
        self.screen = pygame.display.set_mode((1280, 720))
        self.done = False
        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.state = 'breeder'

        self.breeder = BreederGame(self.screen)
        self.platformer = platformer_game.Game(self.screen)

        self.rat_text = counterText()

    # def events(self):
    #     if self.state == 'breeder':
    #         self.breeder.run_events()

    def run(self):
        while not self.done:
            pygame.display.set_caption("current FPS: "+str(self.clock.get_fps()))

            if self.state == 'breeder':
                self.breeder.run()
                if self.breeder.exit():
                    self.state = 'platformer'
            elif self.state == 'platformer':
                self.platformer.run()
            
            if self.state == 'breeder' or self.state == 'platformer':
                #rats and crows update
                self.breeder.update()

            #currents stats
            self.rat_text.render("time_now: "+str(self.breeder.timer//self.FPS), self.screen, 1240, 630)
            self.rat_text.render("my_rats: "+str(int(self.breeder.ratGrowth.rat_count)), self.screen, 1240, 700)

            pygame.display.update()
            self.clock.tick(self.FPS)

Game().run()