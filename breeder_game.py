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
    def __init__(self, screen):
        self.FPS = 60
        self.money = 100
        self.rat_data = [0,0,0,0,0,0,0,0,0,0]

        self.state = 'shop'

        # pygame.mixer.music.load("data/music/breeder.mp3")
        # pygame.mixer.music.play(-1)
        self.click = pygame.mixer.Sound("data/sounds/click.ogg")
        self.click.set_volume(0.8)

        self.screen = screen
        self.done = False
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.one_cycle_counter = 0
        self.close_button = utils.load_image("breeder/close_button.png")
        self.overlay = utils.load_image("breeder/overlay.png")
        self.tiger = utils.load_image("breeder/tiger.png")
        # self.tiger = pygame.transform.scale(self.tiger, (1000,400))

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

        self.rats = []
        self.rat_render_limit = 150

        for x in range(self.ratGrowth.rat_count):
            if len(self.rats)<=self.rat_render_limit:
                self.rats.append(Rat(self))

        self.shop_button = Button(50, 200, 80, 80, 'white', 'black', 'SHOP')
        self.options_button = Button(50, 320, 80, 80, 'white', 'black', 'OPTS')
        self.plot_button = Button(50, 440, 80, 80, 'white', 'black', 'PLOT')
        self.close_button = Button(1130, 90, 80, 50, 'white', 'red', 'X')

        #CURSOR
        self.cursor_sprites = utils.Spritesheet("breeder/cursor-sprite.png")
        cursor_size = 50
        self.cursor_imgs = (
            self.cursor_sprites.get_sprite(0,0,cursor_size,cursor_size),
            self.cursor_sprites.get_sprite(cursor_size,0,cursor_size,cursor_size)
        )
        self.cursor_img = self.cursor_imgs[0]
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

    def exit(self):
        if self.player.pos[0] > self.screen.get_width():
            return True
            self.done = True
            #exit room and go to platformer

    def main_game(self):

        self.screen.fill((34, 30, 80))
        pygame.draw.circle(self.screen, (255,255,0), (1150,80), 50)
        self.screen.blit(self.wall, (0, 0))

        self.player.update(self.movement)
        self.player.render()
        self.screen.blit(self.bg, (0, 0))


        if self.breeder_shop.items[6]["owned"]:
            self.screen.blit(self.tiger, (0,0))

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
            self.click.play()
        if self.options_button.update(self.screen,self.mouse_pos):
            self.state = 'options'
            self.click.play()
        if self.plot_button.update(self.screen,self.mouse_pos):
            self.plot_update = True
            if self.plot_update:
                self.ratGrowth.plotter()
                self.plot_img = utils.load_image("breeder/rat_data.png")
                self.plot_update = False
            self.state = 'plot'
            self.click.play()

    def update(self):
        #TIMER CYCLE TICKS WHATEVER YOU CALL IT
        self.timer += 1
        self.one_cycle_counter += 1
        if self.one_cycle_counter >= self.FPS:
            # print(self.timer)
            self.ratGrowth.update()
            self.crow.update_states()
            self.one_cycle_counter = 0
        self.crow.update()

    def run(self):
        # print('breeder main')
    # while not self.done:
        #system stuff
        self.mouse_pos = pygame.mouse.get_pos()



        # #hover over crow change cursor
        # self.crow.mouse_input_hover(self.mouse_pos)

        #ANIMATION
        # if self.one_cycle_counter >= self.FPS:
        self.crow.animate_update()


        #rat math
        if int(self.ratGrowth.rat_count) > len(self.rats) and len(self.rats)<=self.rat_render_limit:
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
                self.cursor_img = self.cursor_imgs[1]    
                if self.state == 'main':
                    self.main_game_events()
                elif self.state == 'shop':
                    self.breeder_shop.mouse_down_events(self.mouse_pos)
                if self.state != 'main':
                    if self.close_button.update(self.screen,self.mouse_pos):
                        self.player.refresh_image()
                        self.click.play()
                        self.state = 'main'
                self.run_events()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.cursor_img = self.cursor_imgs[0]    

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

        self.screen.blit(self.overlay, (0,0))
        #custom cursor
        if self.state == 'main': self.crow.render_cursor(self.mouse_pos)
        self.cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
        self.screen.blit(self.cursor_img, self.cursor_img_rect) # draw the cursor


