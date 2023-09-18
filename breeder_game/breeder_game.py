import pygame
import sys
import utils
from wolf import Wolf

from crow import Crow
from rats import Rat
from calculate_rats import BreederCalculations
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
        
        if self.state == 'main':
            self.movement = [False, False]

            self.bg = utils.load_image("02-breeding-room.png")

            self.player = Wolf(self)

            self.crow = Crow(self)
            self.rat = Rat(self)

            self.ratGrowth = BreederCalculations()
            self.rat_text = counterText()

            self.shop_button = Button(70, 200, 80, 80, 'white', 'black', 'SHOP')
            self.options_button = Button(70, 320, 80, 80, 'white', 'black', 'OPTS')
            self.plot_button = Button(70, 440, 80, 80, 'white', 'black', 'PLOT')

            pygame.mouse.set_visible(False)
            self.cursor_img = utils.load_image("cursor.png")
            self.cursor_img_rect = self.cursor_img.get_rect()

    def main_game(self):
        while not self.done:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            pygame.display.set_caption("current FPS: "+str(self.clock.get_fps()))
            if self.player.pos[0] > self.screen.get_width():
                pygame.quit()
                sys.exit()
                self.done = True
                #exit room and go to platformer

            self.timer += 1
            self.ratGrowth.update()
            # print(self.ratGrowth.rat_count)

            self.screen.fill((34, 30, 80))
            self.player.update(self.movement)
            self.player.render()
            self.screen.blit(self.bg, (0, 0))

            self.crow.render()
            self.rat.render()

            self.player.shadow()

            self.rat_text.render(str(self.timer//60)+' '+str(int(self.ratGrowth.rat_count)), self.screen)

            if self.shop_button.update(self.screen,mouse_pos,mouse_pressed):
                self.state = 'shop'
            if self.options_button.update(self.screen,mouse_pos,mouse_pressed):
                self.state = 'options'
            if self.plot_button.update(self.screen,mouse_pos,mouse_pressed):
                self.state = 'plot'


            #custom cursor
            self.cursor_img_rect = pygame.mouse.get_pos()  # update position 
            self.screen.blit(self.cursor_img, self.cursor_img_rect) # draw the cursor


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

    def shop(self):
        pass

    def options(self):
        pass

    def plot(self):
        pass

    def run(self):
        if self.state == 'main':
            self.main_game()
        elif self.state == 'shop':
            self.shop()
        elif self.state == 'options':
            self.options()
        elif self.state == 'plot':
            self.plot()

BreederGame().run()