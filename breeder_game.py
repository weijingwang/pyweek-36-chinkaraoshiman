import pygame
import sys
import utils
from breeder.wolf import Wolf

from breeder.crow import Crow
from breeder.rats import Rat
from breeder.calculate_rats import BreederCalculations
from displayText import counterText
from button import Button

class BreederGame:
    def __init__(self):

        self.state = 'main'

        pygame.init()

        pygame.display.set_caption('pyweek36')

        self.screen = pygame.display.set_mode((1280, 720))
        self.done = False
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.close_button = utils.load_image("breeder/close_button.png")

        #MAIN-----------------------------
        self.movement = [False, False]

        self.bg = utils.load_image("breeder/02-breeding-room.png")

        self.player = Wolf(self)

        self.crow = Crow(self)
        self.rat = Rat(self)

        self.ratGrowth = BreederCalculations()
        self.rat_text = counterText()

        self.shop_button = Button(70, 200, 80, 80, 'white', 'black', 'SHOP')
        self.options_button = Button(70, 320, 80, 80, 'white', 'black', 'OPTS')
        self.plot_button = Button(70, 440, 80, 80, 'white', 'black', 'PLOT')
        self.close_button = Button(1000, 200, 80, 80, 'white', 'red', 'X')


        pygame.mouse.set_visible(False)
        self.cursor_img = utils.load_image("breeder/cursor.png")
        self.cursor_img_rect = self.cursor_img.get_rect()

        #PLOT--------------------------------------
        self.plot_img = utils.load_image("breeder/plot.png")
        self.plot_img_rect = self.plot_img.get_rect(center = self.screen.get_rect().center)

        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pressed = pygame.mouse.get_pressed()

        #SHOP--------------------------------------
        self.shop_img = utils.load_image("breeder/shop.png")
        self.shop_img_rect = self.shop_img.get_rect(center = self.screen.get_rect().center)

        #OPTS--------------------------------------
        self.opts_img = utils.load_image("breeder/opts.png")
        self.opts_img_rect = self.opts_img.get_rect(center = self.screen.get_rect().center)


    def main_game(self):

        pygame.display.set_caption("current FPS: "+str(self.clock.get_fps()))
        if self.player.pos[0] > self.screen.get_width():
            pygame.quit()
            sys.exit()
            self.done = True
            #exit room and go to platformer


        # print(self.ratGrowth.rat_count)

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

    def shop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.screen.blit(self.shop_img, self.shop_img_rect)
        if self.close_button.update(self.screen,self.mouse_pos,self.mouse_pressed):
            self.state = 'main'

    def options(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.screen.blit(self.opts_img, self.opts_img_rect)
        if self.close_button.update(self.screen,self.mouse_pos,self.mouse_pressed):
            self.state = 'main'

    def plot(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.screen.blit(self.plot_img, self.plot_img_rect)
        if self.close_button.update(self.screen,self.mouse_pos,self.mouse_pressed):
            self.state = 'main'

    def run(self):
        while not self.done:
            self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_pressed = pygame.mouse.get_pressed()

            self.timer += 1
            self.ratGrowth.update()

            if self.state == 'main':
                self.main_game()
            elif self.state == 'shop':
                self.shop()
            elif self.state == 'options':
                self.options()
            elif self.state == 'plot':
                self.plot()

            if self.shop_button.update(self.screen,self.mouse_pos,self.mouse_pressed):
                self.state = 'shop'
            if self.options_button.update(self.screen,self.mouse_pos,self.mouse_pressed):
                self.state = 'options'
            if self.plot_button.update(self.screen,self.mouse_pos,self.mouse_pressed):
                self.state = 'plot'
            #custom cursor
            self.cursor_img_rect = pygame.mouse.get_pos()  # update position 
            self.screen.blit(self.cursor_img, self.cursor_img_rect) # draw the cursor



            self.rat_text.render(str(self.timer//60)+' '+str(int(self.ratGrowth.rat_count)), self.screen)
            pygame.display.update()
            self.clock.tick(60)

BreederGame().run()