from breeder_game import BreederGame
import platformer_game
from displayText import counterText
from title_class import Title
import pygame
import sys
import utils

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load("data/music/wolfBGM.ogg")
        pygame.mixer.music.play(-1)
        pygame.display.set_caption("pyweek36")
        self.screen = pygame.display.set_mode((1280, 720))
        self.done = False
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.mouse_pos = pygame.mouse.get_pos()

        self.state = 'title'

        self.my_title = Title(self, self.screen)
        self.breeder = BreederGame(self.screen)
        self.platformer = platformer_game.Game(self.screen)

        self.rat_text = counterText(50)

    # def events(self):
    #     if self.state == 'breeder':
    #         self.breeder.run_events()

    def update_cursor(self):
        #cursor
        self.mouse_pos = pygame.mouse.get_pos()
        if self.state == 'breeder' or self.state == 'platformer':
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)


    def run(self):
        while not self.done:
            self.update_cursor()
            pygame.display.set_caption("current FPS: "+str(self.clock.get_fps()))

            if self.state == 'title':
                self.my_title.run(self.mouse_pos)
            elif self.state == 'breeder':
                self.breeder.run()
                if self.breeder.exit():
                    self.state = 'platformer'
            elif self.state == 'platformer':
                self.platformer.run()
            
            if self.state == 'breeder' or self.state == 'platformer':
                #rats and crows update
                self.breeder.update()

                #currents stats
                # self.rat_text.render("timeNow: "+str(self.breeder.timer//self.FPS), self.screen, 1240, 580)
                self.rat_text.render("my_rats: "+str(int(self.breeder.ratGrowth.rat_count)), self.screen, 1240, 630)
                self.rat_text.render("myMoney: "+str(int(self.breeder.money)), self.screen, 1240, 680)


            pygame.display.update()
            self.clock.tick(self.FPS)

Game().run()