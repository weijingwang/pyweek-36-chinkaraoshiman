from breeder_game import BreederGame
import pygame
import sys

class Game:
    def __init__(self):
        self.FPS = 60
        self.money = 100
        self.rat_data = [0,0,0,0,0,0,0,0,0,0]

        self.state = 'main'

        pygame.init()
        pygame.mixer.music.load("data/music/breeder.mp3")
        pygame.mixer.music.play(-1)
        self.click = pygame.mixer.Sound("data/sounds/CLICK.ogg")

        pygame.display.set_caption("pyweek36")

        self.screen = pygame.display.set_mode((1280, 720))
        self.done = False
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.one_cycle_counter = 0
        self.mouse_pos = pygame.mouse.get_pos()

        self.state = 'breeder'

        self.breeder = BreederGame()

    def events(self):
        if self.state == 'breeder':
            self.breeder.run_events()

    def run(self):
        while not self.done:
            # #system stuff
            # pygame.display.set_caption("current FPS: "+str(self.clock.get_fps()))
            # self.mouse_pos = pygame.mouse.get_pos()
            # self.timer += 1
            # self.one_cycle_counter += 1
            # if self.one_cycle_counter >= self.FPS:
            #     # print(self.timer)
            #     self.ratGrowth.update()
            #     self.crow.update_states()
            #     self.one_cycle_counter = 0
            # self.crow.update()

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         sys.exit()
            #     self.events()

            # pygame.display.update()
            # self.clock.tick(self.FPS)
            if self.state == 'breeder':
                self.breeder.run()

Game().run()