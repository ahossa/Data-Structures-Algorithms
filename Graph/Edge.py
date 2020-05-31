from .Node import Node

class Edge:
    def __init__(self, startNode, endNode, id = None, weight = 0, isDirected = True):
        assert(isinstance(startNode, Node))
        assert(isinstance(endNode, Node))

        self.__startNode = startNode
        self.__endNode = endNode
        self.__edgeId = id
        self.__edgeWgt = weight
        self.__isDirected = isDirected    # Directed Edge by default
    
    def getId(self):
        return self.__edgeId
        
    def getStartNode(self):
        return self.__startNode
    
    def getEndNode(self):
        return self.__endNode
    
    def getEdgeWgt(self):
        return self.__edgeWgt

    def isDirectedEdge(self):
        return self.__isDirected
    
    def setEdgeWgt(self, edgeWgt):
        self.__edgeWgt = edgeWgt