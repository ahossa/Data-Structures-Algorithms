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


    ## Get the List of NODES in the Graph
    def getNodesList(self):
        return self.__NodesList
    
    ## Get the list of EDGES in the Graph
    def getEdgeList(self):
        return self.__EdgeList

    ## Get the Total number of Nodes in the graph
    def getNumNodes(self):
        return len(self.__NodesList)
    
    ## Get the Total number of Edges in the Graph
    def getNumEdges(self):
        return len(self.__EdgeList)
    
    ## Returns TRUE if the Graph is EMPTY (i.e No Nodes)
    def isEmpty(self):
        return len(self.__NodesList) == 0


    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    # 
    # Adds a Node to the Graph (i.e Adds to the Nodes List)
    # Edge Case consideration : What if the Node (by value) already exist ?
    #                           A new node with the same value but different
    #                           Node Id is created as now 
    # Node Id starts from 0 and follows Insertion Order
    #
    # @arg newNodeValue : Value for the new Node
    # @ret Returns a Copy of the Newly Created Node
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def addNode(self, newNodeValue):
        # Add node to the NODES List 1st
        nodeId = self.getNumNodes()
        newNode = Node(nodeId, newNodeValue)
        self.__NodesList.append(newNode)
        return newNode

    
    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    #
    # Adds a Directed Edge between the Start & End Node
    # Edge-Id = Start-Node Id + End-Node Id
    # 
    # @arg startNodeVal : Value of Start Node
    # @arg endNodeVal : Value of End Node
    # @arg weight : Optional Wgt for the created Edge. Default Wgt value 1
    # @ret Returns a copy of the newly created Edge
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def addEdge(self, startNodeVal, endNodeVal, weight = 0):      
        # Chk at 1st if the Nodes exist in the Graph
        startNode = self.searchNode(startNodeVal)
        endNode = self.searchNode(endNodeVal)
        
        if (startNode is None or endNode is None):
            return None

        edgeId = str(startNode.getId()) + str(endNode.getId())      
        newEdge = Edge(startNode, endNode, edgeId, 1)
        
        # Set Edge weight when provided
        if weight != 0:
            newEdge.setEdgeWgt(weight)
        
        self.__EdgeList[edgeId] = newEdge
        return newEdge
        
    
    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    # Search for a Node in the Graph
    # Considertion : Add functionality to search by Node Id ?
    #
    # @arg nodeVal : Value of the Node to be seared for
    # 
    # @ret Returns the node if Found, None otherwise
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def searchNode(self, nodeVal):
        for node in self.__NodesList:
            if node.getValue() == nodeVal:
                return node
        return None
    

    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    # Search for an edge in the graph by providing an Edge Id
    # Edge-Id = Start-Node Id + End-Node Id
    # 
    # @arg edgeId : Edge Id for the Edge to Search
    # @ret Returns the Edge if found, None otherwise
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def searchEdgeById(self, edgeId):
        if edgeId in self.__EdgeList:
            return self.__EdgeList[edgeId]
        return None
    

    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    # Search for an Edge in the Graph by providing Start & End Node values
    # 
    # @arg startNodeVal : Value for Start Node 
    # @arg endNodeVal : Value for the End Node
    # @ret Returns the Edge if found, None otherwise
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
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


    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    # Remove an Edge from the Graph by providing the Edge Id
    # 
    # @arg edgeId : Id for the Edge to be removed
    # @ret Returns a copy of the Removed Edge upon successful Delete, None otherwise
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def removeEdgeById(self, edgeId):
        rmvEdge = self.searchEdgeById(edgeId)
        if rmvEdge is None:
            return None
        self.__EdgeList.pop(edgeId)
        return rmvEdge


    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    # Remove an Edge from the Graph by providing Start & End Node values
    # 
    # @arg startNodeVal : Edge Start node value
    # @arg endNodeVal: Edge End Node value
    # @ret Returns a copy of the Removed Edge upon successful Delete, None otherwise
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def removeEdgeBySource(self, startNodeVal, endNodeVal):
        rmvEdge = self.searchEdgeBySource(startNodeVal, endNodeVal)
        if rmvEdge is None:
            return None
        self.__EdgeList.pop(rmvEdge.getId())
        return rmvEdge