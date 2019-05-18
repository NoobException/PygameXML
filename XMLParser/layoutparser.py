#!python3
#*.* coding:"utf-8" *.*

from XMLParser import *

class LayoutParser:
    def __init__(self, interface):
        self.interface = interface
        self.loader = Loader()
        self.widgetCount = 0

    def parseLayout(self, filename):
        root = self.loader.parseFile(filename)
        self.parseItem(root)

    def parseItem(self, item, parent = 'interface'):
        tag = item.tag
        attrib = item.attrib
        self.widgetCount += 1
        Debug.log(f"Processing object <{tag}> with attributes {attrib}")

        name = attrib["name"] if "name" in attrib else f"Element{self.widgetCount}"
        attrib["name"] = name
        parentObject = self.interface[parent]

        element = None
        if tag == "window":
            element = Window(properties = attrib, parent = parentObject)
            self.interface.window = element

        elif tag == "surface":
            element = Surface(properties = attrib, parent = parentObject)
        
        elif tag == "image":
            element = Image(properties = attrib, parent = parentObject)

        elif tag == "label":
            element = Label(properties = attrib, parent = parentObject)

        self.interface[name] = element

        for child in item:
            self.parseItem(child, parent = name)
