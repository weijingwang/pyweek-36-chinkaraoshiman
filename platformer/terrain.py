import pygame

class Terrain(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * 16
        self.y = y * 16
        self.width = 16
        self.height = 16

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y