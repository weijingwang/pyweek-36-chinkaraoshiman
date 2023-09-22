import pygame
from button import Button
from utils import load_image
from animation.slideshow import Slideshow

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

        self.bg = Slideshow(self.texts, self.images, self.images, self.screen)

        self.start_button = Button(1280/2, (720/4)*2, 1280/6, 720/6, 'white', 'black', 'start', int(720/6))
        self.quit_button = Button(1280/2, (720/4)*3, 1280/6, 720/6, 'white', 'black', 'quit', int(720/6))
    def run(self, mouse_pos):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                # print('s')
                if not self.start_button.update(self.screen, mouse_pos):
                    self.game.state = 'breeder' #CHANGE LATER

                elif not self.quit_button.update(self.screen, mouse_pos):
                    pygame.quit()
                    quit()  
        self.screen.blit(self.images[0], (0,0))
        self.screen.blit(self.image, (0,0))
        self.bg.update()
        self.start_button.render(self.screen)
        self.quit_button.render(self.screen)
            
