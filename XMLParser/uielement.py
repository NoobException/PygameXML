#!python3
#*.* coding:"utf-8" *.*

import copy

class UIElement:
    DEFAULT = {

    }
    def __getitem__(self, key):
        if not key in self.properties:
            return None
        return self.properties[key]

    def __setitem__(self, key, item):
        self.properties[key] = item
        
    def __init__(self, properties = {}, parent = None):
        self.parent = parent
        if parent != None: parent.children.append(self)
        self.user_properties = copy.copy(properties)
        self.properties = properties
        self.mergeProperties(UIElement.DEFAULT)
        self.children = []

    def mergeProperties(self, default):
        for _property in default:
            if not _property in self.user_properties:
                self.properties[_property] = default[_property]

        self.evalProperties()

    def evalProperties(self):
        for _property in self.properties:
            propertyValue = self.properties[_property]
            try:
                exec("self.{propertyName} = {propertyValue}".format(propertyName = _property, propertyValue = propertyValue))
            except:
                exec("self.{propertyName} = '{propertyValue}'".format(propertyName = _property, propertyValue = propertyValue))