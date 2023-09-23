import os
import pygame

BASE_PATH = "data/images/"

def load_image(path, colorkey = (0,0,0)):
    img = pygame.image.load(BASE_PATH + path).convert()
    if "brick" in path:
        img.set_colorkey((0,0,1))
    else:
        img.set_colorkey(colorkey)
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images
    
class CounterText:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 80)
    def render(self,text,surface, x, y):
        image = self.font.render(str(text), True, (255, 0, 0)).convert_alpha()
        image_rect = image.get_rect(bottomright = (x,y))#center = surface.get_rect().center)
        surface.blit(image, image_rect)