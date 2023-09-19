import pygame
import sys
import utils
from breeder.wolf import Wolf

from breeder.crow import Crow
from breeder.rats import Rat
from breeder.calculate_rats import BreederCalculations
from displayText import counterText
from button import Button, itemButton

class BreederGame:
    def __init__(self):

        self.state = 'shop'

        pygame.init()

        pygame.display.set_caption("pyweek36")

        self.screen = pygame.display.set_mode((1280, 720))
        self.done = False
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.close_button = utils.load_image("breeder/close_button.png")

        #MAIN-----------------------------
        self.movement = [False, False]
        self.wall = utils.load_image("breeder/wall.png")

        self.bg = utils.load_image("breeder/02-breeding-room.png")

        self.player = Wolf(self)

        self.crow = Crow(self)
        self.rat = Rat(self)

        self.ratGrowth = BreederCalculations()
        self.rat_text = counterText()

        self.shop_button = Button(50, 200, 80, 80, 'white', 'black', 'SHOP')
        self.options_button = Button(50, 320, 80, 80, 'white', 'black', 'OPTS')
        self.plot_button = Button(50, 440, 80, 80, 'white', 'black', 'PLOT')
        self.close_button = Button(1130, 90, 80, 50, 'white', 'red', 'X')

        pygame.mouse.set_visible(False)
        self.cursor_img = utils.load_image("breeder/cursor.png")
        self.cursor_img_rect = self.cursor_img.get_rect()

        #PLOT--------------------------------------
        self.plot_img = utils.load_image("breeder/plot.png")
        self.plot_img_rect = self.plot_img.get_rect(center = self.screen.get_rect().center)

        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pressed = False
        self.mouse_clicking = False

        #SHOP--------------------------------------
        self.shop_img = utils.load_image("breeder/07-shop.png")
        self.shop_img_rect = self.shop_img.get_rect(center = self.screen.get_rect().center)

        #OPTS--------------------------------------
        self.opts_img = utils.load_image("breeder/opts.png")
        self.opts_img_rect = self.opts_img.get_rect(center = self.screen.get_rect().center)

        self.items = [
            {"name": "Food", "price": 5, "pos": (320,330), "owned": False, "description": "temporarily satiate rat hunger"},
            {"name": "Auto-feeder", "price": 5, "pos": (320,400), "owned": False, "description": "rats never go hungry"},
            {"name": "Medicine", "price": 5, "pos": (320,470), "owned": False, "description": "cure rats"},
            {"name": "Doctor", "price": 5, "pos": (320,540), "owned": False, "description": "rats never sick"},
            {"name": "Tempting hand", "price": 5, "pos": (620,330), "owned": False, "description": "slightly increase rat breeding chance when clicking on them"},
            {"name": "Skillful hand", "price": 5, "pos": (620,400), "owned": False, "description": "greatly increase rat breeding chance when clicking on them"},
            {"name": "Scarecrow", "price": 5, "pos": (620,470), "owned": False, "description": "decrease crow attack rate"},
            {"name": "Crow destroyer", "price": 5, "pos": (620,540), "owned": False, "description": "crows do not kill rats"}
        ]
        self.button_grid = []
        for x in self.items:
            self.button_grid.append(itemButton(x["pos"][0], x["pos"][1], x["name"]))

    def main_game(self):
        if self.player.pos[0] > self.screen.get_width():
            pygame.quit()
            sys.exit()
            self.done = True
            #exit room and go to platformer

        # print(self.ratGrowth.rat_count)

        self.screen.fill((34, 30, 80))
        pygame.draw.circle(self.screen, (255,255,0), (1150,80), 50)
        self.screen.blit(self.wall, (0, 0))

        self.player.update(self.movement)
        self.player.render()
        self.screen.blit(self.bg, (0, 0))

        self.crow.render()
        self.rat.render()

        self.player.shadow()
        
        # self.screen.blit(pygame.transform.scale(self.screen, self.screen.get_size()), (0, 0))

    def shop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.screen.blit(self.shop_img, self.shop_img_rect)
        if self.close_button.update(self.screen,self.mouse_pos,self.mouse_pressed):
            self.state = 'main'

        for i in range(len(self.button_grid)): 
            if self.button_grid[i].update(self.screen,self.mouse_pos,self.mouse_pressed, self.items[i]["owned"]):
                self.items[i]["owned"] = True
                # print(str(i)+" is owned "+str(self.items[i]["owned"])+" ")
        # print(self.items)
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
            pygame.display.set_caption("current FPS: "+str(self.clock.get_fps()))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # self.mouse_pressed = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_clicking = True
                if event.type == pygame.MOUSEBUTTONUP and self.mouse_clicking:
                    self.mouse_pressed = True
                    self.mouse_clicking = False
                    # print('yes')
                else:
                    self.mouse_pressed = False

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
                else:
                    self.screen.fill((34, 30, 80))
                    self.screen.blit(self.wall, (0, 0))

                    pygame.draw.circle(self.screen, (255,255,0), (1150,80), 50)
                    self.screen.blit(self.bg,(0,0))
                    self.movement = [0,0]

            # print(' ')
            self.mouse_pos = pygame.mouse.get_pos()
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

            #would like toggle button
            if self.shop_button.update(self.screen,self.mouse_pos,self.mouse_pressed):
                self.state = 'shop'
            if self.options_button.update(self.screen,self.mouse_pos,self.mouse_pressed):
                self.state = 'options'
            if self.plot_button.update(self.screen,self.mouse_pos,self.mouse_pressed):
                self.state = 'plot'
            

            #custom cursor
            self.cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
            self.screen.blit(self.cursor_img, self.cursor_img_rect) # draw the cursor



            self.rat_text.render(str(self.timer//60)+' '+str(int(self.ratGrowth.rat_count)), self.screen)
            pygame.display.update()
            self.clock.tick(60)

BreederGame().run()