## Adjacency-List Graph class
## AdjList.py
## created: 02.06.2020 TUESDAY

from .Graph import Graph
from .Node import GraphNode as GphNode
from .Edge import Edge
from LinkedList.SLinkedList import SLinkedList as LList 
from LinkedList.Node import LinkedListNode as LLNode 

class AdjList(Graph):

    def __init__(self):
        self.__NodesList = []     # An array of Nodes
        self.__EdgeList = []     # An array of LinkedLists(of Ll-Nodes) with every node being the head of LList
                                 # So size of the edgeList is equal to sz of nodesList

        self.debugMode = True
    
    # # # # # # # # # # # # # # # # ACCESOR METHODS # # # # # # # # # # # # # # # # # # # # # # #  

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
        totalEdges = 0
        for LLIter in self.__EdgeList:
            totalEdges += LLIter.getSize()
        return totalEdges - self.getNumNodes()
            
    ## Returns TRUE if the Graph is EMPTY (i.e No Nodes)
    def isEmpty(self):
        return len(self.__NodesList) == 0
    
    
    # # # # # # # # # # # # # # # # NODE METHODS # # # # # # # # # # # # # # # # # # # # # # #  
    
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
        newNode = GphNode(nodeId, newNodeValue)
        self.__NodesList.append(newNode)

        # Now create a LinkedList for the node value and
        # append it to the EdgeList
        newLLNode = LLNode(newNodeValue, nodeId)
        newList = LList()
        newList.insertHeadNode(newLLNode)
        self.__EdgeList.insert(nodeId, newList)  # The Edgelist index num is same as the Node Id
        return newNode
    
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
    
    def removeNode(self, nodeVal):
        pass

    # # # # # # # # # # # # # # # # EDGE METHODS # # # # # # # # # # # # # # # # # # # # # # #  

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
    # Time Complexity : O(n) [Node-Search] + O(n) [LL Tail Insertion] = O(n)
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def addEdge(self, startNodeVal, endNodeVal, weight = 0):      
        # Chk at 1st if the Nodes exist in the Graph
        startNode = self.searchNode(startNodeVal)
        endNode = self.searchNode(endNodeVal)
        
        if (startNode is None or endNode is None):
            return False

        # index for NodeList & EdgeList is same for each Node
        nodeListInd = startNode.getId()

        self.__EdgeList[nodeListInd].insertTailNode(LLNode(endNodeVal))
        return True
    
    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    # Search for an Edge in the Graph by providing Start & End Node values
    # 
    # @arg startNodeVal : Value for Start Node 
    # @arg endNodeVal : Value for the End Node
    # @ret Returns the index of the stored LLNode in EdgeList
    #      Returns False if the start or end node doesn't exist
    #      Returns -1 if the Edge is not found
    #
    # Time Complexity : O(N) [Node-Search] + O(N) [LL traversal for search] = O(N)
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def searchEdge(self, startNodeVal, endNodeVal):
        # Chk at 1st if the Nodes exist in the Graph
        startNode = self.searchNode(startNodeVal)
        endNode = self.searchNode(endNodeVal)
        
        if (startNode is None or endNode is None):
            return False

        # index for NodeList & EdgeList is same for each Node
        startNodeInd = startNode.getId()
        LLendNode = LLNode(endNodeVal)
        edgeList = self.getEdgeList()
        return edgeList[startNodeInd].searchList(LLendNode)  # Returns the found index

    


    def removeEdge(self, edge):
        pass