#!python3
#*.* coding:"utf-8" *.*

import pygame
from pygame.locals import *

from XMLParser import Surface

class Image(Surface):
    DEFAULT = {
        "source" : None
    }
    def __init__(self, properties = {}, parent = None):
        super().__init__(properties = properties, parent = parent)
        self.mergeProperties(Image.DEFAULT)


    def draw(self):
        try:
            img = pygame.image.load(self.source)
        except:
            return

        self.width, self.height = img.get_size()
        self.surface = img