## make an iterating slideshow for the title screen
import os
import pygame
from util import * ## importing from the util.py file so the displayImage function can be utilized

BASE_IMG_PATH = './data/images'

def slideshow(path): # for the title screen (?)
    load_images(path) ## returns a list of photos from function
    for image in images:
        pass ## iterate through list here, printing the photos to make a powerpoint-like style
