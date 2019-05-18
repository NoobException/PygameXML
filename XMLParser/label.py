#!python3
#*.* coding:"utf-8" *.*

import pygame
from pygame.locals import *

from XMLParser import Surface, Debug

class Label(Surface):
    DEFAULT = {
        "text" : "",
        "font" : "consolas",
        "font_size" : 32,
        "background" : (0, 0, 0, 0),
        "font_color" : "(255, 255, 255)",
        "text_align" : "center",
        "transparent" : True
    } 
    def __init__(self, properties = {}, parent = None):
        super().__init__(properties = properties, parent = parent)
        self.mergeProperties(Label.DEFAULT)
        self.text = str(self.text)
        
    def draw(self):
        if self.transparent:
            self.background = self.parent.background
        super().draw()
        self.fontObject = pygame.font.SysFont(self.font, self.font_size)
        text = self.fontObject.render(self.text, True, self.font_color)
        self.width = max(self.width, text.get_width() + 2 * self.padding)
        self.height = max(self.height, text.get_height() + 2 * self.padding)

        if self.surface.get_size() != (self.width, self.height):
            self.surface = pygame.Surface((self.width, self.height))
            Debug.log([self.name, self.width, self.height])

        tx = (self.width - text.get_width()) // 2
        ty = (self.height - text.get_height()) // 2

        self.surface.blit(text, (tx, ty))