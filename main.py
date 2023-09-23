from breeder_game import BreederGame
import platformer_game
from displayText import counterText
from title_class import Title, clickCutscene
import pygame
import sys
import utils
from ending_cutscene import endAnime, Animation, stillImage

class Game:
    def __init__(self):
        self.rat_count_to_win = 500
        pygame.init()
        self.state = 'ending2'
        pygame.mixer.stop()
        pygame.mixer.music.load("data/music/wolfBGM.ogg")
        pygame.mixer.music.play(-1)
        pygame.display.set_caption("pyweek36")
        self.screen = pygame.display.set_mode((1280, 720))
        self.done = False
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.mouse_pos = pygame.mouse.get_pos()



        self.my_title = Title(self, self.screen)
        self.breeder = BreederGame(self.screen)
        self.platformer = platformer_game.Game(self,self.screen)
# (self, pos, align='right',size=50):
        self.rat_text = counterText((1240, 630),'right',50)
        self.money_text = counterText((1240, 680),'right',50)
        
        self.intro_img = utils.load_image("intro_img.png")
        self.intro = clickCutscene(self, self.intro_img, self.screen)


        self.ending_text = ('','','','')
        self.ending_imgs = (
            utils.load_image("ending/DarkMatter1.jpg"),
            utils.load_image("ending/DarkMatter2.jpg"),
            utils.load_image("ending/DarkMatter3.jpg"),
            utils.load_image("ending/DarkMatter4.jpg")
        )
        self.ending_imgs2 = (
            utils.load_image("ending/DarkMatter1.jpg"),
            utils.load_image("ending/DarkMatter2.jpg"),
            utils.load_image("ending/DarkMatter3.jpg"),
            utils.load_image("ending/DarkMatter4.jpg")
        )

        self.earth_end_imgs = (
            utils.load_image("ending/DarkMatter5.1.jpg"),
            utils.load_image("ending/DarkMatter5.2.jpg"),
            utils.load_image("ending/DarkMatter5.3.jpg"),
            utils.load_image("ending/DarkMatter5.4.jpg"),
            utils.load_image("ending/DarkMatter5.5.jpg"),
            utils.load_image("ending/DarkMatter5.6.jpg"),
            utils.load_image("ending/DarkMatter5.7.jpg"),
            utils.load_image("ending/DarkMatter5.8.jpg"),
            utils.load_image("ending/DarkMatter5.9.jpg")
        )

        self.ending = endAnime(self.ending_text, self.ending_imgs, self.ending_imgs2, self.screen)
        self.endingAnimation = Animation(self.earth_end_imgs, False)
        self.endingAnimation_group = pygame.sprite.Group()
        self.endingAnimation_group.add(self.endingAnimation)
        self.ending_card = stillImage(self.screen, self.earth_end_imgs[8])
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

            if self.breeder.ratGrowth.rat_count >= self.rat_count_to_win:
                self.state = 'ending'


            if self.state == 'title':
                self.my_title.run(self.mouse_pos)
            elif self.state =='intro':
                self.intro.run(self.mouse_pos)
            elif self.state == 'breeder':
                self.breeder.run()
                if self.breeder.exit():
                    self.platformer.can_play_music = True
                    self.state = 'platformer'
            elif self.state == 'platformer':
                self.platformer.run()
            elif self.state == 'ending':
                # pygame.mixer.music.load("data/music/world-end.ogg")
                if self.ending.end_anime():
                    self.state = 'ending2'
            elif self.state == 'ending2':
                self.endingAnimation.events()
                self.endingAnimation_group.update()
                self.endingAnimation_group.draw(self.screen)
                if self.endingAnimation.isFinished():
                    pygame.mixer.music.fadeout(5000)
                    self.state = 'ending3'
            elif self.state == 'ending3':
                
                self.ending_card.run()

            
            if self.state == 'breeder' or self.state == 'platformer':
                #rats and crows update
                self.breeder.update()

                #currents stats
                # self.rat_text.render("timeNow: "+str(self.breeder.timer//self.FPS), self.screen, 1240, 580)
                self.rat_text.render("rats: "+str(int(self.breeder.ratGrowth.rat_count))+"/"+str(self.breeder.ratGrowth.upper_cap), self.screen)
                self.money_text.render("$"+str(int(self.breeder.money)), self.screen)


            pygame.display.update()
            self.clock.tick(self.FPS)
            print(self.state)

Game().run()