import pygame
from config import *

class Button:
    def __init__(self, x, y, width, height, fg, bg, content):
        """self, x, y, width, height, fg, bg, content)"""
        self.font = pygame.font.SysFont(None, 100)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg =fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height)) 
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.center = (self.x, self.y)

        self.text = self.font.render(self.content, False, self.fg) #false antialiasing
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def update(self, surface, pos, pressed):
        surface.blit(self.image, self.rect)
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
        return False
        #     return False
        # return False