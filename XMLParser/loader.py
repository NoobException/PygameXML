#!python3
#*.* coding:"utf-8" *.*

import xml.etree.ElementTree as ET
import codecs

class Loader:
    """
        Reads XML file, parse, and return tree
    """
    
    def parseFile(self, filename):
        file = codecs.open(filename, 'r', encoding = "utf-8")
        text = file.read()
        file.close()
        return self.parseText(text)
        
    def parseText(self, text):
        root = ET.fromstring(text)
        return root
            
            