## Graph Node class
## Node.py
## created: 29.05.2020 FRIDAY

from Debug import LOG_DEBUG

class Node:
    def __init__(self, id = None, val = None):
        self.__id = id
        self.__value = val

    
    def setValue(self, val):
        self.__value = val
    
    def getValue(self):
        return self.__value
    
    def setId(self, id):
        self.__id = id
    
    def getId(self):
        return self.__id
    
    def isEqual(self, otherNode):
        if (self.getValue() == otherNode.getValue()):
            if (otherNode.getId() is not None):
                return self.getId() == otherNode.getId()
            return True
        return False
        
    def debugPrint(self, doShowDebugOutput):
        LOG_DEBUG("GRAPH NODE", doShowDebugOutput)
        LOG_DEBUG("ID : " + str(self.getId()), doShowDebugOutput)
        LOG_DEBUG("VAL : " + str(self.getValue()), doShowDebugOutput)
