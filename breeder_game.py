import pygame
import sys
import utils
from breeder.wolf import Wolf

from breeder.crow import Crow
from breeder.rats import Rat
from breeder.calculate_rats import BreederCalculations
from displayText import counterText
from button import Button, itemButton, textInput

class BreederGame:
    def __init__(self):
        self.rat_data = [0,0,0,0,0,0,0,0,0,0]

        self.state = 'main'

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
        self.shop_img = utils.load_image("breeder/07-shop.png")
        self.shop_img_rect = self.shop_img.get_rect(center = self.screen.get_rect().center)
        self.input_buy_rats = textInput(200, 200, "buy")
        self.input_sell_rats = textInput(900, 200, "sell")
        self.storage_button = itemButton(1280/2,200,"buy storage",260,100)

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


        self.screen.fill((34, 30, 80))
        pygame.draw.circle(self.screen, (255,255,0), (1150,80), 50)
        self.screen.blit(self.wall, (0, 0))

        self.player.update(self.movement)
        self.player.render()
        self.screen.blit(self.bg, (0, 0))

        for rat in range(len(self.rats)):
            self.rats[rat].update()
            self.rats[rat].render()

        self.crow.update()
        self.crow.render()



        self.player.shadow()
        
        # self.screen.blit(pygame.transform.scale(self.screen, self.screen.get_size()), (0, 0))
    def main_game_events(self):
        self.crow.mouse_inputs(self.mouse_pos)
    def shop(self):            
        self.screen.blit(self.shop_img, self.shop_img_rect)
    def shop_events(self):
        if self.close_button.update(self.screen,self.mouse_pos):
            self.state = 'main'

        self.input_buy_rats.update(self.mouse_pos)
        self.input_sell_rats.update(self.mouse_pos)
        self.storage_button.update(self.mouse_pos)
        for i in range(len(self.button_grid)): 
            self.button_grid[i].update(self.mouse_pos)#, self.items[i]["owned"]
                
            if self.button_grid[i].activated:
                self.items[i]["owned"] = True
            print(self.items[i]["name"],self.items[i]["owned"])


    def options(self):
        self.screen.blit(self.opts_img, self.opts_img_rect)
    def options_events(self):
        if self.close_button.update(self.screen,self.mouse_pos):
            self.state = 'main'

    def plot(self):
        self.screen.blit(self.plot_img, self.plot_img_rect)
    def plot_events(self):
        if self.close_button.update(self.screen,self.mouse_pos):
            self.state = 'main'

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
            self.ratGrowth.update()
            #rat math
            if int(self.ratGrowth.rat_count) > len(self.rats):
                for x in range(int(self.ratGrowth.rat_count)-len(self.rats)):
                    self.rats.append(Rat(self))
            elif int(self.ratGrowth.rat_count) < len(self.rats):
                for x in range(len(self.rats)-int(self.ratGrowth.rat_count)):
                    self.rats.pop()

            #draw static background if not main
            if self.state != "main":
                self.screen.fill((34, 30, 80))
                self.screen.blit(self.wall, (0, 0))
                pygame.draw.circle(self.screen, (255,255,0), (1150,80), 50)
                self.screen.blit(self.bg,(0,0))
                self.movement = [0,0]     

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #33:50
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.ratGrowth.rat_count -=1
                        self.rats.pop()
                if event.type == pygame.MOUSEBUTTONDOWN:     
                    if self.state == 'main':
                        self.main_game_events()
                    elif self.state == 'shop':
                        self.shop_events()
                    elif self.state == 'options':
                        self.options_events()
                    elif self.state == 'plot':
                        self.plot_events()
                    self.run_events()
                    
                if self.state == 'shop':
                    self.input_buy_rats.input_control(event)
                    self.input_sell_rats.input_control(event)

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


            if self.state == 'main':
                self.main_game()
            elif self.state == 'shop':
                self.shop()
            elif self.state == 'options':
                self.options()
            elif self.state == 'plot':
                self.plot()

            if self.state == "shop":
                for i in range(len(self.button_grid)): 
                    self.button_grid[i].render(self.screen)
            if self.state == "shop":
                self.input_buy_rats.render(self.screen)
                self.input_sell_rats.render(self.screen)
                self.storage_button.render(self.screen)

            self.shop_button.render(self.screen)
            self.options_button.render(self.screen)
            self.plot_button.render(self.screen)


            if self.state != "main":
                self.close_button.render(self.screen)
            #custom cursor
            self.cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
            self.screen.blit(self.cursor_img, self.cursor_img_rect) # draw the cursor



            self.rat_text.render(str(self.timer//60)+' '+str(int(self.ratGrowth.rat_count))+' '+str(int(len(self.rats))), self.screen)
            
            pygame.display.update()
            self.clock.tick(60)

BreederGame().run()