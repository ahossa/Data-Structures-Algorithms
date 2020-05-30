## Adjacency-Matrix Graph class
## AdjMatrix.py
## created: 29.05.2020 FRIDAY

from .Graph import Graph
from .Node import Node

class AdjMatrix(Graph):
    def __init__(self, numNodes = 0):
        self.__numNodes = numNodes
        self.__matrix = []
        
        self.debugMode = True
        # create a row of Nodes
        # Then create a column of rowNodes
        # Id follows the insertion order
        
        if numNodes == 0:
            return

        id = 0
        for i in range(0, numNodes):
            row = []
            for j in range(0, numNodes):
                id += 1
                row.append(Node(id,0))
            self.__matrix.append(row)


    def getNumNodes(self):
        return self.__numNodes
    
    def getMatrix(self):
        return self.__matrix

    def getMatrixSize(self):
        return (len(self.__matrix) * self.__numNodes)
    
    def isEmpty(self):
        return self.__numNodes == 0





    def setNode(self, nodeValue):
        pass
    
    def setEdge(self, edge):
        pass
    
    def searchNode(self, nodeVal):
        pass
    
    def searchEdge(self, edge):
        pass
    
    def removeNode(self, nodeVal):
        pass
    
    def removeEdge(self, edge):
        pass