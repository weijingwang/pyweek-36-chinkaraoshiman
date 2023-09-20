import pygame
import sys
import utils
from breeder.wolf import Wolf

from breeder.crow import Crow
from breeder.rats import Rat
from breeder.calculate_rats import BreederCalculations
from displayText import counterText
from button import Button, itemButton, textInput
from breeder.shop_class import Shop


class BreederGame:
    def __init__(self):
        self.FPS = 60
        self.money = 100
        self.rat_data = [0,0,0,0,0,0,0,0,0,0]

        self.state = 'main'

        pygame.init()

        pygame.display.set_caption("pyweek36")

        self.screen = pygame.display.set_mode((1280, 720))
        self.done = False
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.one_cycle_counter = 0
        self.close_button = utils.load_image("breeder/close_button.png")

        #MAIN-----------------------------
        self.movement = [False, False]
        self.wall = utils.load_image("breeder/wall.png")
# (0,782),(330,600)
        self.cage1 = utils.load_image("breeder/cage-1.png")
        self.cage2 = utils.load_image("breeder/cage-2.png")
        self.cage3 = utils.load_image("breeder/cage-3.png")
        self.cage4 = utils.load_image("breeder/cage-4.png")
        self.cage1 = pygame.transform.scale(self.cage1, (1000,400))
        self.cage2 = pygame.transform.scale(self.cage2, (1000,400))
        self.cage3 = pygame.transform.scale(self.cage3, (1000,400))
        self.cage4 = pygame.transform.scale(self.cage4, (1000,400))
        self.bg = utils.load_image("breeder/02-breeding-room.png")

        self.player = Wolf(self)

        self.crow = Crow(self)

        self.ratGrowth = BreederCalculations(self)
        self.rat_text = counterText()

        self.rats = []
        for x in range(self.ratGrowth.rat_count):
            self.rats.append(Rat(self))

        self.shop_button = Button(50, 200, 80, 80, 'white', 'black', 'SHOP')
        self.options_button = Button(50, 320, 80, 80, 'white', 'black', 'OPTS')
        self.plot_button = Button(50, 440, 80, 80, 'white', 'black', 'PLOT')
        self.close_button = Button(1130, 90, 80, 50, 'white', 'red', 'X')

        pygame.mouse.set_visible(False)
        self.cursor_img = utils.load_image("breeder/cursor.png")
        self.cursor_img_rect = self.cursor_img.get_rect()

        #PLOT--------------------------------------
        self.plot_img = utils.load_image("breeder/rat_data.png")
        self.plot_img_rect = self.plot_img.get_rect(center = self.screen.get_rect().center)

        self.mouse_pos = pygame.mouse.get_pos()
        self.plot_update = True

        #OPTS--------------------------------------
        self.opts_img = utils.load_image("breeder/opts.png")
        self.opts_img_rect = self.opts_img.get_rect(center = self.screen.get_rect().center)

        #SHOP--------------------------------------
        self.breeder_shop = Shop(self, self.screen)

    def main_game(self):
        if self.player.pos[0] > self.screen.get_width():
            pygame.quit()
            sys.exit()
            self.done = True
            #exit room and go to platformer


        self.screen.fill((34, 30, 80))
        pygame.draw.circle(self.screen, (255,255,0), (1150,80), 50)
        self.screen.blit(self.wall, (0, 0))

        self.player.update(self.movement)
        self.player.render()
        self.screen.blit(self.bg, (0, 0))

        self.screen.blit(self.cage1, (-50,350))
        self.screen.blit(self.cage3, (-50,350))

        for rat in range(len(self.rats)):
            self.rats[rat].update()
            self.rats[rat].render()

        self.crow.render()
        self.screen.blit(self.cage2, (-50,350))
        self.screen.blit(self.cage4, (-50,350))
        self.player.shadow()
        
        # self.screen.blit(pygame.transform.scale(self.screen, self.screen.get_size()), (0, 0))
    def main_game_events(self):
        self.crow.mouse_inputs(self.mouse_pos)


    def options(self):
        self.screen.blit(self.opts_img, self.opts_img_rect)

    def plot(self):
        self.screen.blit(self.plot_img, self.plot_img_rect)

    def run_events(self):
        #would like toggle button
        if self.shop_button.update(self.screen,self.mouse_pos):
            self.state = 'shop'
        if self.options_button.update(self.screen,self.mouse_pos):
            self.state = 'options'
        if self.plot_button.update(self.screen,self.mouse_pos):
            self.plot_update = True
            if self.plot_update:
                self.ratGrowth.plotter()
                self.plot_img = utils.load_image("breeder/rat_data.png")
                self.plot_update = False
            self.state = 'plot'


    def run(self):
        while not self.done:
            #system stuff
            pygame.display.set_caption("current FPS: "+str(self.clock.get_fps()))
            self.mouse_pos = pygame.mouse.get_pos()
            self.timer += 1
            self.one_cycle_counter += 1
            if self.one_cycle_counter >= self.FPS:
                # print(self.timer)
                self.ratGrowth.update()
                self.crow.update_states()
                self.one_cycle_counter = 0
            self.crow.update()

            #rat math
            if int(self.ratGrowth.rat_count) > len(self.rats):
                for x in range(int(self.ratGrowth.rat_count)-len(self.rats)):
                    self.rats.append(Rat(self))
            elif int(self.ratGrowth.rat_count) < len(self.rats):
                for x in range(len(self.rats)-int(self.ratGrowth.rat_count)):
                    self.rats.pop()   

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #33:50
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_BACKSPACE:
                #         self.ratGrowth.rat_count -=1
                #         self.rats.pop()
                if event.type == pygame.MOUSEBUTTONDOWN:     
                    if self.state == 'main':
                        self.main_game_events()
                    elif self.state == 'shop':
                        self.breeder_shop.mouse_down_events(self.mouse_pos)
                    if self.state != 'main':
                        if self.close_button.update(self.screen,self.mouse_pos):
                            self.state = 'main'
                    self.run_events()
                elif event.type == pygame.MOUSEBUTTONUP:
                    # if self.state == 'shop':
                    self.breeder_shop.mouse_up_events()
                #other events like typing
                if self.state == 'main':
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
                if self.state == 'shop':
                    self.breeder_shop.state_events(event)


            #draw static background if not main
            if self.state != "main":
                self.screen.fill((34, 30, 80))
                self.screen.blit(self.wall, (0, 0))
                pygame.draw.circle(self.screen, (255,255,0), (1150,80), 50)
                self.screen.blit(self.bg,(0,0))
                self.movement = [0,0]  

            if self.state == 'main':
                self.main_game()
            elif self.state == 'shop':
                # self.breeder_shop.transactions()
                self.breeder_shop.render()
            elif self.state == 'options':
                self.options()
            elif self.state == 'plot':
                self.plot()

            #draw menu buttons (always visible)
            self.shop_button.render(self.screen)
            self.options_button.render(self.screen)
            self.plot_button.render(self.screen)

            #draw exit button (needs to be drawn on top of everything else)
            if self.state != "main":
                self.close_button.render(self.screen)

            #custom cursor
            self.cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
            self.screen.blit(self.cursor_img, self.cursor_img_rect) # draw the cursor

            #currents stats
            self.rat_text.render(str(self.timer//self.FPS)+' '+str(int(self.ratGrowth.rat_count))+' '+str(int(len(self.rats))), self.screen)
            
            pygame.display.update()
            self.clock.tick(self.FPS)

BreederGame().run()