import pygame
from button import Button
class Title:
    def __init__(self, game, screen):
        self.screen = screen
        self.game = game
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

        self.start_button.render(self.screen)
        self.quit_button.render(self.screen)
            
