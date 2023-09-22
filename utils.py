import os

import pygame

BASE_IMG_PATH = './data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    # img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        if img_name != '.DS_Store':
            images.append(load_image(path + '/' + img_name))
    return images
    
class CounterText:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 80)
    def render(self,text,surface, x, y):
        image = self.font.render(str(text), True, (255, 0, 0)).convert_alpha()
        image_rect = image.get_rect(bottomright = (x,y))#center = surface.get_rect().center)
        surface.blit(image, image_rect)