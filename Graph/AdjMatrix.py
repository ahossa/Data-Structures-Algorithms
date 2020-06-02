## Adjacency-Matrix Graph class
## AdjMatrix.py
## created: 29.05.2020 FRIDAY

from .Graph import Graph
from .Node import Node
from .Edge import Edge


class AdjMatrix(Graph):
    def __init__(self):
        self.__NodesList = []    # A 1D ARRAY of Nodes

        # # # 
        # NOTE:
        # Creating a Dictionary might be more efficient in this regard
        # With Id Based insertion in the EdgeList
        # I Know this isn't the Ideal AdjMatrix but rather 
        # Optimized AdjMatrix I'd say. See the complexisy analysis
        # for each methods
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
    #
    # Time Complexity : O(1) [List Append]
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
    #
    # Time Complexity : O(n) [Node-Search] + O(1) [Dict Insertion] = O(n)
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
    #
    # Time Complexity : O(n) [List Retrieval]
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
    #
    # Time Complexity : O(1) [Dict retrieval]
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
    #
    # Time Complexity : O(N) [Node-Search] + O(1) [Edge-Search]
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def searchEdgeBySource(self, startNodeVal, endNodeVal):
        # Chk at 1st if the Nodes exist in the Graph
        startNode = self.searchNode(startNodeVal)
        endNode = self.searchNode(endNodeVal)
        
        if (startNode is None or endNode is None):
            return None

        edgeId = str(startNode.getId()) + str(endNode.getId())
        return self.searchEdgeById(edgeId)


    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    # Remove a Node from the Graph
    # Also removed the Edges Connected to that Node
    # 
    # @arg nodeVal : Value of the Node to be removed
    # @ret Returns a copy of the removed Node
    #
    # Time Complexity : O(n) [Node-search] + O(n) [Edge-search] +
    #                   O(1) [Edge-remove] + O(n) [Node-List-Rmv] = O(n)
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def removeNode(self, nodeVal):
        
        # We'd have to do 2 things
        # Remove the Node + 
        # Removed edges associated with that node
        nodeToRmv = self.searchNode(nodeVal)
        
        if nodeToRmv is None:
            return None

        EdgesToRmvList = self.getEdgesForNode(nodeToRmv)
        
        # Remove the Edges 1st
        for edgeToRmv in EdgesToRmvList:
            self.removeEdgeById(edgeToRmv.getId())
        
        # now remove the node
        self.__NodesList.remove(nodeToRmv)
        return nodeToRmv
    

    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    # Get all the edges connected to a Node
    # 
    # @arg startNodeIn : Node Input for the Edge. 
    #                    Only Value is compared for Edge Start or End Node
    #                    When Node Id Provided, both Id & Value is compared 
    #
    # @ret Returns a List of Edges either Starting Or Ending with the given Node
    #
    # Time Complexity : O(n) [Dict Iteration]
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def getEdgesForNode(self, nodeIn):
        allEdgeList = self.getEdgeList().values()
        edgeListForNode = []
        for edge in allEdgeList:
            startNode = edge.getStartNode()
            endNode = edge.getEndNode()
            if startNode.isEqual(nodeIn) or endNode.isEqual(nodeIn):
                edgeListForNode.append(edge)
        
        return edgeListForNode


    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    # Get all the edges connected to a Start Node
    # 
    # @arg startNodeIn : Start Node Input for the Edge. 
    #                    Only Value is compared for for Edge Start Node
    #                    When Node Id Provided, both Id & Value is compared 
    #
    # @ret Returns a List of Edges Starting with the provided Start Node
    #
    # Time Complexity : O(n) [Dict Iteration]
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def getEdgesForStartNode(self, startNodeIn):
        
        edgeList = self.getEdgeList().values()
        edgeListForStartNode = []
        
        for edge in edgeList:
            startNode = edge.getStartNode()
            if startNode.isEqual(startNodeIn):
                # LOG_DEBUG("MATCH FOUND", self.debugMode)
                edgeListForStartNode.append(edge)
        
        return edgeListForStartNode
    

    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    # Get all the edges connected to an End Node
    # 
    # @arg endNodeIn : End Node Input for the Edge. 
    #                  Only Value is compared for for Edge End Node
    #                  When Node Id Provided, both Id & Value is compared 
    #
    # @ret Returns a List of Edges Ending with the provided End Node
    #
    # Time Complexity : O(n) [Dict Iteration]
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def getEdgesForEndNode(self, endNodeIn):
        edgeList = self.getEdgeList().values()
        edgeListForEndNode = []
        
        for edge in edgeList:
            endNode = edge.getEndNode()
            if endNode.isEqual(endNodeIn):
                edgeListForEndNode.append(edge)
        
        return edgeListForEndNode

    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    # Remove an Edge from the Graph by providing the Edge Id
    # 
    # @arg edgeId : Id for the Edge to be removed
    # @ret Returns a copy of the Removed Edge upon successful Delete, None otherwise
    #
    # Time Complexity : O(1) [Dict Removal]
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
    #
    # Time Complexity : O(1) [Dict Removal]
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def removeEdgeBySource(self, startNodeVal, endNodeVal):
        rmvEdge = self.searchEdgeBySource(startNodeVal, endNodeVal)
        if rmvEdge is None:
            return None
        self.__EdgeList.pop(rmvEdge.getId())
        return rmvEdge