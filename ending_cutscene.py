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
        self.first_iteration = True
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    def end_anime(self):
        if self.first_iteration:
            pygame.mixer.stop()
            pygame.mixer.music.load("data/music/world-end.ogg")
            pygame.mixer.music.play(-1)
            self.first_iteration = False
        self.events()
        self.cutscene.update()
        if self.cutscene.stop: 
            # print('stop')
            return True
        else:
            # print('')
            return False
class stillImage:
    def __init__(self, screen, image):
        self.image = image
        self.screen = screen
    
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.screen.blit(self.image,(0,0))



class Animation():
    """docstring for Animation"""
    def __init__(self,images, loop_on):
        self.images=images
        self.loop_on = loop_on
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.speed = 0.05
        self.finished= False
    def update(self):
        print(self.index)
        if self.loop_on==True:
            if self.index>=len(self.images)-1:
                self.index=0
            else:
                self.index+=self.speed
        elif self.loop_on==False:
            if self.index>=len(self.images)-1:
                self.index=0
                self.speed = 0
                self.finished= True
                self.isFinished()
                # self.kill()
            else:
                self.index+=self.speed
        self.image = self.images[int(self.index)]
    def render(self,screen):
        screen.blit(self.image,(0,0))
    def isFinished(self):
        return self.finished
      
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()