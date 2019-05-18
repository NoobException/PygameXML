#!python3
#*.* coding:"utf-8" *.*

import pygame
from pygame.locals import *

from XMLParser import UIElement

class Surface(UIElement):
    DEFAULT = {
        "width" : 0,
        "height" : 0,
        "scale" : 1,
        "x" : 0,
        "y" : 0,

        "background" : (0, 0, 0, 0),
        "transparent" : False,
        "border_size" : 0,
        "border_color" : 0,
        "padding" : 0,

        "layout_halign" : "center",
        "layout_valign" : "top",

        "layout_direction" : "right",
        "item_spacing" : 0
    }
    def __init__(self, properties = {}, parent = None):
        super().__init__(properties = properties, parent = parent)
        self.mergeProperties(Surface.DEFAULT)
        if not self.transparent:
            self.surface = pygame.Surface((self.width, self.height))
        else:
            self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)

    def draw(self):

        self.surface.fill(self.background)
        if self.border_size > 0:
            pygame.draw.rect(self.surface, self.border_color, [0, 0, self.width, self.height], self.border_size)

    
    def get_inner_size(self):

        if self.layout_direction == "right":
            totalWidth = sum(child.width * child.scale for child in self.children if isinstance(child, Surface))
            if len(self.children) > 0:
                totalHeight = max([child.height * child.scale for child in self.children if isinstance(child, Surface)])
            else:
                totalHeight = self.height * self.scale - 2 * self.padding

           
            if len(self.children) > 0:
                totalWidth += self.item_spacing * (len(self.children) - 1)

        elif self.layout_direction == "down":
            totalWidth = max(child.width * child.scale for child in self.children if isinstance(child, Surface))
            totalHeight = sum(child.height * child.scale for child in self.children if isinstance(child, Surface))


        return (totalWidth, totalHeight)

    def display(self):
        self.draw()
        currentChildX = currentChildY = 0

        innerWidth, innerHeight = self.get_inner_size()

        if self.layout_halign == "center":
            currentChildX = (self.width - 2 * self.padding - innerWidth) // 2

        if self.layout_valign == "top":
            currentChildY = 0

        elif self.layout_valign == "center":
            currentChildY = (self.height - 2 * self.padding - innerHeight) // 2

        for child in self.children:
            if isinstance(child, Surface):

                if self.layout_direction == "right" and self.layout_valign == "center":
                    currentChildY = (self.height - 2 * self.padding - child.height * child.scale) // 2

                elif self.layout_direction == "down" and self.layout_halign == "center":
                    currentChildX = (self.width - 2 * self.padding - child.width * child.scale) // 2

                child.x = currentChildX
                child.y = currentChildY
                child.display()

                if self.layout_direction == "right":
                    currentChildX += child.width + self.item_spacing 
                
                elif self.layout_direction == "down":
                    currentChildY += child.height + self.item_spacing
                

        blitSurface = pygame.transform.scale(self.surface, [ int(self.width * self.scale), int(self.height * self.scale)])
        if self.parent != None and isinstance(self.parent, Surface):
            self.parent.surface.blit(blitSurface, (self.x + self.parent.padding, self.y + self.parent.padding))
