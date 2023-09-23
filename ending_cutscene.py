from animation.slideshow import Slideshow
import pygame
import sys
class endAnime:
    def __init__(self, texts, imgs, imgs_copy, screen):
        self.texts = texts
        self.imgs = imgs
        self.imgs_copy = imgs_copy
        self.screen = screen
        self.cutscene = Slideshow(self.texts, self.imgs, self.imgs_copy, self.screen)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


    def end_anime(self):
        self.events()
        self.cutscene.update()
        if self.cutscene.stop: return True
        else: return False
