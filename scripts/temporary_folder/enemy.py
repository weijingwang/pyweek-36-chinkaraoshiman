import pygame
from mob import Mob

#enemy walks around
#when in range of player, begins offensive mode by shooting
#shoots slower than player
#moves slower than player
#maybe different kinds of attacks as well
#if different types of enemy, better to create new file

class Enemy(Mob):
    def __init__():
        super().__init__(6,9,4)
        # image var is initialized in super init
        #image = #pygame.image.load(PATH TO IMG)