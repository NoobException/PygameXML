#!python3
#*.* coding:"utf-8" *.*

import copy

import pygame
from pygame.locals import *

from XMLParser import UIElement, LayoutParser

class Interface(UIElement):
    def __getitem__(self, key):
        return self.interface[key]

    def __setitem__(self, key, item):
        self.interface[key] = item

    def __init__(self): 
        super().__init__()
        self.interface = {}
        self["interface"] = self
        self.window = None
        self.parser = LayoutParser(self)

    def runLayout(self, filename):
        self.parser.parseLayout(filename)
        if self.window != None:
            self.window.run()



