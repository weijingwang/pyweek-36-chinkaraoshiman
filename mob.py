import pygame
from abc import ABC, abstractmethod

# superclass for mobs (player, enemy, etc)
# all mobs should have:
# image
# x, y
# etc etc

class Mob(pygame.sprite.Sprite, ABC):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = 1
        self.speed = 0

    @abstractmethod
    def movement():
        pass