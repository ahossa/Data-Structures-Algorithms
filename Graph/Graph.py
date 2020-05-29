
class Graph:

    @abstractmethod
    def setNode(self, nodeValue):
        pass
    
    @abstractmethod
    def setEdge(self, edge):
        pass
    
    @abstractmethod
    def searchNode(self, nodeVal):
        pass
    
    @abstractmethod
    def searchEdge(self, edge):
        pass
    
    @abstractmethod
    def removeNode(self, nodeVal):
        pass
    
    @abstractmethod
    def removeEdge(self, edge):
        pass