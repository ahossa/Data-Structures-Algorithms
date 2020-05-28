from .TreeNode import TreeNode as Node 
from Debug import LOG_DEBUG

class BinarySearchTree():

    ## Constructor
    def __init__(self):
        self.rootNodePtr = None
        self.size = 0

        # Set this to True for Debug Statements
        self.debugMode = True
    
    
    # Insert a Node into BST
    # Returns the Id of the newly inserted Node
    # Id 1 starts from Root and follows insertion sequence
    # for Id assignment
    def insertNode(self, newNodeValue):     
        # If root is empty or Size 0 that means BST is empty
        # In that case insert the Node at Root
        if (self.rootNodePtr is None and 
            self.size == 0):
            
            LOG_DEBUG("Inserting Root Node" + str(newNodeValue),
                    self.debugMode)
            self.rootNodePtr = Node(1,newNodeValue)
            self.size += 1
            return self.rootNodePtr.getId()
        
        rootNode = self.rootNodePtr
        return self.insert(rootNode, newNodeValue);

    ###
    # Helper function to insert the NewNode value into a parent node
    def insert(self, parentNode, newNodeVal):      
        assert(isinstance(parentNode, Node))
        
        ## If New Node <= Parent Node, Go to Left Sub-Tree 
        if newNodeVal <= parentNode.getValue():
            return self.insertIntoLeftSubtree(parentNode, newNodeVal)

        
        ## If New Node > Parent Node, Go to Right Sub-Tree 
        if newNodeVal > parentNode.getValue() :
            return self.insertIntoRightSubtree(parentNode, newNodeVal)
    
    ###
    # Helper Function to Insert a Node into Left Subtree
    def insertIntoLeftSubtree(self, parentNode, newNodeVal):
        
        # Make sure ParentNode is an instance of Node Class
        assert(isinstance(parentNode, Node))

        LOG_DEBUG ("NewNode " + str(newNodeVal) +
                " <= ParentNode " + str(parentNode.getValue()),
                self.debugMode)
        
        if parentNode.hasLeftChild():
            LOG_DEBUG("Parent " + str(parentNode.getValue()) + 
                    " has left child", self.debugMode)
            return self.insert(parentNode.getLeftChild(), newNodeVal)
        
        else:
            LOG_DEBUG("Inserting Child " + str(newNodeVal) +
                    " To left of " + str(parentNode.getValue()),
                    self.debugMode)
            self.size += 1
            LOG_DEBUG("Current Size " + str(self.size), self.debugMode)
            parentNode.setLeftChild(
                Node(self.size, newNodeVal) 
            )
            return parentNode.getLeftChild().getId()
    
    ###
    # Helper Function to Insert a Node into Right Subtree
    def insertIntoRightSubtree(self, parentNode, newNodeVal):
        
        # Make sure ParentNode is an instance of Node Class        
        assert(isinstance(parentNode, Node))
        
        LOG_DEBUG("NewNode " + str(newNodeVal) +
                " > ParentNode " + str(parentNode.getValue()),
                self.debugMode)
        
        if parentNode.hasRightChild():
            LOG_DEBUG("Parent " + str(parentNode.getValue()) + 
                    " has rght child", self.debugMode)
            return self.insert(parentNode.getRightChild(), newNodeVal)
        
        else:
            LOG_DEBUG("Inserting Child " + str(newNodeVal) +
                    " To right of " + str(parentNode.getValue()), 
                    self.debugMode)
            
            self.size += 1
            LOG_DEBUG("Current Size " + str(self.size), self.debugMode)
            parentNode.setRightChild(
                Node(self.size, newNodeVal)
            )
            return parentNode.getRightChild().getId()

    #def searchNode(self, key):
    

    #def removeNode(self, key):
     
    # Returns TRUE if BST is Empty
    def isEmpty(self):
        return (self.rootNodePtr is None and 
                self.size == 0)
    
    # Get the size of the BST
    def getSize(self):
        return self.size
    
    

    
    
    
    
