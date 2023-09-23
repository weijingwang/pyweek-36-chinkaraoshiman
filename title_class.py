import pygame
from button import Button
from utils import load_image
from animation.slideshow import Slideshow
import sys
from displayText import normalText
class Title:
    def __init__(self, game, screen):
        self.images = (
            load_image('intro/1.0.png'),
            load_image('intro/1.1.png'),
            load_image('intro/2.png'),
            load_image('intro/3.png'),
            load_image('intro/4.png'),
            load_image('intro/5.png')
        )
        self.imagesbg = (
            load_image('intro/1.0.png'),
            load_image('intro/1.1.png'),
            load_image('intro/2.png'),
            load_image('intro/3.png'),
            load_image('intro/4.png'),
            load_image('intro/5.png')
        )
        self.texts = (
            'One night the stars fell',
            'The fallen stars brought power',
            'Dark matter was found',
            'Discovered by rats',
            'Darkness filled the little ones'
            ,'New disease is born'
        )
        
        self.image = self.images[0]
        self.screen = screen
        self.game = game

        self.title_text = normalText('Apocalypse of darkness rats',(1280/2,100),True,120)

        self.bg = Slideshow(self.texts, self.images, self.imagesbg, self.screen)

        self.start_button = Button(1280/2, (720/8)*5, 1280/5, 60, 'white', 'black', 'start', 60)
        self.quit_button = Button(1280/2, (720/8)*6, 1280/5, 60, 'white', 'black', 'quit', 60)
    def run(self, mouse_pos):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if self.start_button.rect.collidepoint(mouse_pos):#self.start_button.update(self.screen, mouse_pos):
                    print('start')
                    # pygame.quit()
                    # quit()  
                    self.game.state = 'intro' #CHANGE LATER

                elif self.quit_button.rect.collidepoint(mouse_pos):#(self.screen, mouse_pos):
                    print('quit')
                    pygame.quit()
                    sys.exit()
        self.quit_button.update(self.screen, mouse_pos)



        self.screen.blit(self.images[0], (0,0))
        self.screen.blit(self.image, (0,0))
        self.bg.update()
        self.start_button.render(self.screen)
        self.quit_button.render(self.screen)
        self.title_text.render(self.screen)
            
class clickCutscene:
    def __init__(self, game, image ,screen):

        self.image = image
        self.screen = screen
        self.game = game

        self.start_button = Button(1280/2, (720/8)*6, 1280/5, 60, 'white', 'black', 'ok', 60)
    
    def run(self, mouse_pos):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if self.start_button.rect.collidepoint(mouse_pos):#self.start_button.update(self.screen, mouse_pos):
                    print('start')
                    # pygame.quit()
                    # quit()  
                    self.game.state = 'breeder' #CHANGE LATER
        self.screen.blit(self.image, (0,0))
        self.start_button.update(self.screen, mouse_pos)