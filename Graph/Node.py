
class Node:
    def __init__(self, val= None, id = None):
        self.__value = val
        self.__id = id
    
    def setValue(self, val):
        self.__value = val
    
    def getValue(self):
        self.__value
    
    def setId(self, id):
        self.__id = id
    
    def getId(self):
        return self.__id