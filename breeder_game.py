import pygame
import sys
import utils
from breeder.wolf import Wolf

from breeder.crow import Crow
from breeder.rats import Rat
from breeder.calculate_rats import BreederCalculations
from displayText import normalText, counterText
from button import Button, itemButton, textInput
from breeder.shop_class import Shop


class BreederGame:
    def __init__(self, screen):

        self.money = 500#ftyugweirtiyfjopkghcf9x0ud8eoihwujknl3terydjhgusfe8aowiuh3jk4tQ!!!!!!

        self.state = "main"
        self.food_text = counterText((40,630),'right, 50')
        self.medicine_text = counterText((40,680),'right, 50')


        self.rat_cage_rect = pygame.Rect(10, 550, 760, 100)

        self.FPS = 60
        self.food = 0
        self.medicine = 0
        self.rat_data = [0,0,0,0,0,0,0,0,0,0]

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
        self.autofeeder_img = utils.load_image("breeder/items/Autofeeder.png")
        self.autofeeder_img = pygame.transform.scale(self.autofeeder_img, (500,500))

        self.crow_destroyer_img = utils.load_image("breeder/crow_destroyer.png")
        self.doctor_img = utils.load_image("breeder/items/Doctor_copy.png")
        self.doctor_img = pygame.transform.scale(self.doctor_img, (300,720))
        self.seller_img = utils.load_image("breeder/seller.png")
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
        if len(self.rats)<=self.rat_render_limit:
            if len(self.rats)+self.ratGrowth.next_increase <=self.rat_render_limit:

                for x in range(self.ratGrowth.rat_count):
                    self.rats.append(Rat(self))

        self.shop_button = Button(50, 200, 80, 80, 'white', 'black', 'SHOP')
        self.room_button = Button(50, 320, 80, 80, 'white', 'black', 'ROOM')
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
        self.opts_img = utils.load_image("breeder/room.png")
        # self.opts_img_rect = self.opts_img.get_rect(center = self.screen.get_rect().center)

        #SHOP--------------------------------------
        self.breeder_shop = Shop(self, self.screen)


        #STATUS EFFECT
        self.hungry_text = normalText("xxHUNGRYxx", (1280/2,50))
        self.OVERLOADED_text = normalText("OVERLOADED", (1280/2,0))


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




        if self.breeder_shop.items[6]["owned"]:#scarecrow
            self.screen.blit(self.tiger, (0,0))

        if self.breeder_shop.items[1]["owned"]:#autofeeder
            self.screen.blit(self.autofeeder_img, (250,0))
            
        self.screen.blit(self.cage1, (-50,350))
        self.screen.blit(self.cage3, (-50,350))

        for rat in range(len(self.rats)):
            self.rats[rat].update()
            self.rats[rat].render()

        self.crow.render()
        self.screen.blit(self.cage2, (-50,350))
        self.screen.blit(self.cage4, (-50,350))

        # self.screen.blit(self.seller_img, (0,0))

        self.player.shadow()
        
        # self.screen.blit(pygame.transform.scale(self.screen, self.screen.get_size()), (0, 0))
    def main_game_events(self):
        self.crow.mouse_inputs(self.mouse_pos)
        if self.breeder_shop.items[4]["owned"]:
            if self.rat_cage_rect.collidepoint(self.mouse_pos) and self.ratGrowth.rat_count>1:
                self.ratGrowth.rat_count += 1
                self.money += 1
                self.click.play()
                print("rat +1")

    def room(self):
        self.screen.fill((34, 30, 80))
        pygame.draw.circle(self.screen, (255,255,0), (1150,80), 50)
        self.screen.blit(self.wall, (0, 0))

        self.player.update(self.movement)
        self.player.render()
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.opts_img, (0,0))

        if self.breeder_shop.items[7]["owned"]:#crow destroyer
            self.screen.blit(self.crow_destroyer_img, (600,0))
        if self.breeder_shop.items[5]["owned"]:#seller
            self.screen.blit(self.seller_img, (0,0))
        if self.breeder_shop.items[3]["owned"]:#doctor
            self.screen.blit(self.doctor_img, (400,50))
        self.player.shadow()
        
        # self.screen.blit(pygame.transform.scale(self.screen, self.screen.get_size()), (0, 0))




    # def options(self):
    #     self.screen.blit(self.opts_img, self.opts_img_rect)

    def plot(self):
        self.screen.blit(self.plot_img, self.plot_img_rect)

    def run_events(self):
        #would like toggle button
        if self.shop_button.update(self.screen,self.mouse_pos):
            self.state = 'shop'
            self.click.play()
        if self.room_button.update(self.screen,self.mouse_pos):
            self.state = 'room'
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


        #rat math RENDERING!!!!!

        # if too many rats
            #dont add
        # if can add rats
            #only append up to limit
        #decrease anyways unless its less than zero


        #increase part
        # print(str(len(self.rats))+"before")

        if int(self.ratGrowth.rat_count) > len(self.rats):
            #if rat count is greater than rendered rats you wanna increase the rendered rats
            if len(self.rats) >= self.rat_render_limit: #if reach render limit
                pass
                #count is greater than render limit so rats are just render limit
            if len(self.rats) < self.rat_render_limit:
                #if can increase
                for x in range(self.rat_render_limit-len(self.rats)):
                    self.rats.append(Rat(self)) 
            # elif self.ratGrowth.rat_count < self.rat_render_limit:
            #     #count is always less than render limit
            #     for x in range(self.rat_render_limit-int(self.ratGrowth.rat_count)):
            #         self.rats.append(Rat(self)) 
        #decrease part
        elif int(self.ratGrowth.rat_count) < len(self.rats):
            #here rat count is less than rat list so you want to remove list items
            # print(str(len(self.rats))+"after")
            if len(self.rats) > 0:
                for x in range(len(self.rats)-int(self.ratGrowth.rat_count)):
                    self.rats.pop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #33:50
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_BACKSPACE:
            #         s
            # elf.ratGrowth.rat_count -=1
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
                self.breeder_shop.hover_events(self.mouse_pos)
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
        elif self.state == 'room':
            self.room()

        elif self.state == 'shop':
            # self.breeder_shop.transactions()
            self.breeder_shop.render()
        elif self.state == 'room':
            self.room()
        elif self.state == 'plot':
            self.plot()

        #draw menu buttons (always visible)
        self.shop_button.render(self.screen)
        self.room_button.render(self.screen)
        self.plot_button.render(self.screen)

        #draw exit button (needs to be drawn on top of everything else)
        if self.state != "main":
            self.close_button.render(self.screen)

        self.screen.blit(self.overlay, (0,0))
        #custom cursor
        if self.state == 'main': self.crow.render_cursor(self.mouse_pos)
        self.cursor_img_rect.center = pygame.mouse.get_pos()  # update position 
        self.screen.blit(self.cursor_img, self.cursor_img_rect) # draw the cursor
        
        if self.ratGrowth.hungry and self.food <= 0:
            self.hungry_text.render(self.screen)
        if self.ratGrowth.sick and self.medicine <=0:
            self.OVERLOADED_text.render(self.screen)

        self.food_text.render("food: "+str(self.food), self.screen)
        self.medicine_text.render("medicine: "+str(self.medicine), self.screen)
        # print(self.ratGrowth.hungry)
        # print(self.ratGrowth.rat_count, len(self.rats))