## Adjacency-Matrix Graph class
## AdjMatrix.py
## created: 29.05.2020 FRIDAY

from .Graph import Graph
from .Node import Node
from .Edge import Edge

class AdjMatrix(Graph):
    def __init__(self):
        self.__NodesList = []    # A 1D ARRAY of Nodes

        # IDEA:
        # Creating a Dictionary might be more efficient in this regard
        # With Id Based insertion in the EdgeList
        self.__EdgeList = dict()    # A 2D MATRIX of EDGES, a dict is used to be more efficient
        
        self.debugMode = True
        # create a row of Nodes
        # Then create a column of rowNodes
        # Id follows the insertion order
        
        # if numNodes == 0:
        #     return

        # id = 0
        # for i in range(0, numNodes):
        #     row = []
        #     for j in range(0, numNodes):
        #         id += 1
        #         row.append(Node(id,0))
        #     self.__matrix.append(row)


    def getNodesList(self):
        return self.__NodesList
    def getEdgeList(self):
        return self.__EdgeList

    def getNumNodes(self):
        return len(self.__NodesList)
    
    def getNumEdges(self):
        return len(self.__EdgeList)
    
    def isEmpty(self):
        return len(self.__NodesList) == 0

    # Adds a node to the graph
    def addNode(self, newNodeValue):
        # WHAT IF the node already exists?

        # Add node to the NODES List 1st
        nodeId = self.getNumNodes()
        newNode = Node(nodeId, newNodeValue)
        self.__NodesList.append(newNode)
        return newNode


    # Adds an Edge between the start & End Node
    # Adds given weight to the edge, else adds 1
    # Returns None upon failure, else returned the newly entered edge
    def addEdge(self, startNodeVal, endNodeVal, weight = 0):
        
        # Chk at 1st if the Nodes exist in the Graph
        startNode = self.searchNode(startNodeVal)
        endNode = self.searchNode(endNodeVal)
        
        if ( startNode is None or endNode is None):
            return None

        edgeId = str(startNode.getId()) + str(endNode.getId())
        
        newEdge = Edge(startNode, endNode, edgeId, 1)
        
        # Set Edge weight when provided
        if weight != 0:
            newEdge.setEdgeWgt(weight)
        
        self.__EdgeList[edgeId] = newEdge
        return newEdge
        
    
    # Search for a Node in the Graph
    def searchNode(self, nodeVal):
        for node in self.__NodesList:
            if node.getValue() == nodeVal:
                return node
        return None
    

    # Search for an edge in the graph by providing an Edge Id
    def searchEdgeById(self, edgeId):
        if edgeId in self.__EdgeList:
            return self.__EdgeList[edgeId]
    
    # Search for an Edge in the Graph by providing Start & End sources
    def searchEdgeBySource(self, startNodeVal, endNodeVal):
        # Chk at 1st if the Nodes exist in the Graph
        startNode = self.searchNode(startNodeVal)
        endNode = self.searchNode(endNodeVal)
        
        if (startNode is None or endNode is None):
            return None

        edgeId = str(startNode.getId()) + str(endNode.getId())
        return self.searchEdgeById(edgeId)

    def removeNode(self, nodeVal):
        pass
    
    # Remove an Edge from the Graph by providing the Edge Id
    def removeEdgeById(self, edgeId):
        rmvEdge = self.searchEdgeById(edgeId)
        if rmvEdge is None:
            return None
        self.__EdgeList.pop(edgeId)
        return rmvEdge

    def removeEdgeBySource(self, startNodeVal, endNodeVal):
        rmvEdge = self.searchEdgeBySource(startNodeVal, endNodeVal)
        if rmvEdge is None:
            return None
        self.__EdgeList.pop(rmvEdge.getId())
        return rmvEdge