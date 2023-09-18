import pygame

# superclass for mobs (player, enemy, etc)
# all mobs should have:
# image
# x, y
# etc etc

class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
