import os
import pygame

BASE_PATH = "data/images/"

def load_img(path):
    img = pygame.image.load(BASE_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img

def load_imgs(path):
    images = []
    for img_name in sorted(os.listdir(BASE_PATH + path)):
        images.append(load_img(path + '/' + img_name))
    return images
    