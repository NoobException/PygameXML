#!python3
#*.* coding:"utf-8" *.*

import pygame
from pygame.locals import *

from XMLParser import Surface

class Window(Surface):
    DEFAULT = {
        "title" : "App"
    }
    def __init__(self, properties = {}, parent = None):
        super().__init__(properties = properties, parent = parent)
        self.mergeProperties(Window.DEFAULT)

    def run(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.window = pygame.display.set_mode((self.width, self.height))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return

                if event.type == KEYDOWN and event.key == K_SPACE:
                    pygame.image.save(self.surface, "ss.png")
                    pygame.quit()
                    return 

                
            self.display()
            self.window.blit(self.surface, (0,0))
            pygame.display.update()