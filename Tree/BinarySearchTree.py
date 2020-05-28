from .TreeNode import TreeNode as Node 
from Debug import LOG_DEBUG

class BinarySearchTree():

    ## Constructor
    def __init__(self):
        self.__rootNodePtr = None
        self.__size = 0

        # Set this to True for Debug Statements
        self.debugMode = False
    
    
    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   
    #
    # Insert a Node into BST
    # Id 1 starts from Root and follows insertion sequence for Id assignment
    #
    # @arg newNodeValue : Value of the new node to be inserted
    # @ret Returns Id of the newly inserted Node into BST
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def insertNode(self, newNodeValue):     
        # If root is empty or Size 0 that means BST is empty
        # In that case insert the Node at Root
        if (self.__rootNodePtr is None and 
            self.__size == 0):
            
            LOG_DEBUG("Inserting Root Node" + str(newNodeValue),
                    self.debugMode)
            self.__rootNodePtr = Node(1,newNodeValue)
            self.__size += 1
            return self.__rootNodePtr.getId()
        
        rootNode = self.__rootNodePtr
        return self.__insert(rootNode, newNodeValue);

    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    #
    # Helper function to insert the NewNode value into a parent node
    # @arg parentNode : The Parent Node
    # @arg newNodeVal : Value of the new node to be inserted
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def __insert(self, parentNode, newNodeVal):      
        assert(isinstance(parentNode, Node))
        
        ## If New Node <= Parent Node, Go to Left Sub-Tree 
        if newNodeVal <= parentNode.getValue():
            return self.__insertIntoLeftSubtree(parentNode, newNodeVal)

        
        ## If New Node > Parent Node, Go to Right Sub-Tree 
        if newNodeVal > parentNode.getValue() :
            return self.__insertIntoRightSubtree(parentNode, newNodeVal)
    
    
    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    #
    # Helper Function to Insert a Node Value into Left Subtree
    # @arg parentNode : The Parent Node
    # @arg newNodeVal : Value of the new node to be inserted
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def __insertIntoLeftSubtree(self, parentNode, newNodeVal):
        
        # Make sure ParentNode is an instance of Node Class
        assert(isinstance(parentNode, Node))

        LOG_DEBUG ("NewNode " + str(newNodeVal) +
                " <= ParentNode " + str(parentNode.getValue()),
                self.debugMode)
        
        if parentNode.hasLeftChild():
            LOG_DEBUG("Parent " + str(parentNode.getValue()) + 
                    " has left child", self.debugMode)
            return self.__insert(parentNode.getLeftChild(), newNodeVal)
        
        else:
            LOG_DEBUG("Inserting Child " + str(newNodeVal) +
                    " To left of " + str(parentNode.getValue()),
                    self.debugMode)
            self.__size += 1
            LOG_DEBUG("Current Size " + str(self.__size), self.debugMode)
            parentNode.setLeftChild(
                Node(self.__size, newNodeVal) 
            )
            return parentNode.getLeftChild().getId()
    
    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    #
    # Helper Function to Insert a Node Vale into Right Subtree
    # @arg parentNode : The Parent Node
    # @arg newNodeVal : Value of the new node to be inserted
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def __insertIntoRightSubtree(self, parentNode, newNodeVal):
        
        # Make sure ParentNode is an instance of Node Class        
        assert(isinstance(parentNode, Node))
        
        LOG_DEBUG("NewNode " + str(newNodeVal) +
                " > ParentNode " + str(parentNode.getValue()),
                self.debugMode)
        
        if parentNode.hasRightChild():
            LOG_DEBUG("Parent " + str(parentNode.getValue()) + 
                    " has rght child", self.debugMode)
            return self.__insert(parentNode.getRightChild(), newNodeVal)
        
        else:
            LOG_DEBUG("Inserting Child " + str(newNodeVal) +
                    " To right of " + str(parentNode.getValue()), 
                    self.debugMode)
            
            self.__size += 1
            LOG_DEBUG("Current Size " + str(self.__size), self.debugMode)
            parentNode.setRightChild(
                Node(self.__size, newNodeVal)
            )
            return parentNode.getRightChild().getId()

    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    #
    #
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    #def searchNode(self, key):
    
    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    #
    #
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    #def removeNode(self, key):
    
    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    #
    # @ret: Returns TRUE if BST is Empty
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def isEmpty(self):
        return (self.__rootNodePtr is None and 
                self.__size == 0)
    
    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  
    #
    # @ret: Returns the size of the BST
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def getSize(self):
        return self.__size
    
    

    
    
    
    
