from .TreeNode import TreeNode as Node 
from Debug import LOG_DEBUG

class BinarySearchTree():

    ## Constructor
    def __init__(self):
        self.__rootNodePtr = None
        self.__size = 0

        # Set this to True for Debug Statements
        self.debugMode = False
    
    ## - - - - - - - - PUBLIC METHODS - - - - - - - - - - - -##
    
    ###
    # Returns TRUE if BST is Empty
    def isEmpty(self):
        return (self.__rootNodePtr is None and 
            self.__size == 0)
    
    ###
    # Returns the Size of BST
    def getSize(self):
        return self.__size
    
    ###
    # Returns the RootNode of BST
    def getRootNode(self):
        return self.__rootNodePtr

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
        LOG_DEBUG("================================", 
            self.debugMode)
        LOG_DEBUG(" OPERATION : Insert " + str(newNodeValue), 
            self.debugMode)     
        
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
    # Search for a Node in BST by Node Value
    #
    # @arg searchNodeval : Value of the Node to be searched for
    # @ret Returns the Node when found, None otherwise
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def searchNode(self, searchNodeVal):
        LOG_DEBUG("================================", 
            self.debugMode)
        LOG_DEBUG("OPERATION : Search " +str(searchNodeVal),
            self.debugMode)
        
        rootNode = self.__rootNodePtr
        
        # Node found in the root node (Good News!)
        if rootNode.getValue() == searchNodeVal:
            LOG_DEBUG("Search Node: " + str(searchNodeVal) + 
                "Found in Root Node" + str(rootNode.getId()),self.debugMode)
            return rootNode
        return self.__searchInChildren(rootNode, searchNodeVal)


    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #
    # Delete a Node in BST by Node Value
    #
    # @arg delNodeVal : Value of the Node to be Deleted
    # @ret Returns the Node when deleted, None otherwise
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def deleteNode(self, delNodeVal):
        LOG_DEBUG("================================", self.debugMode)
        LOG_DEBUG("OPERATION : DELETE " +str(delNodeVal), self.debugMode)
        
        if (delNodeVal is None or
            self.__rootNodePtr is None):
            return None
        
        rootNode = self.__rootNodePtr
        return self.__deleteNode(rootNode, delNodeVal)
    

    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #
    # Get all the child nodes for a given Parent node
    #
    # @arg parentNode : Parent Node whose children we want to get
    # @ret Returns the Children in a List []
    #      Returns an empty List [] if there's no children
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def getChildrenNodes(self, parentNode):
        LOG_DEBUG("================================", 
            self.debugMode)
        LOG_DEBUG("OPERATION : GetAllChildren " +str(parentNode.getValue()),
            self.debugMode)
        
        assert(isinstance(parentNode, Node))
        children = []                
        return self.__getChildren(parentNode, children)






    ## - - - - - - - - PRIVATE METHODS - - - - - - - - - - - -##
    
    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #
    # Helper Function for DeleteNode
    #
    # @arg parentNode : Parent Node whose children needs to be looked at for del  
    # @arg delNodeVal : Value of the Node to be Deleted
    # @ret Returns the Node when deleted, None otherwise
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def __deleteNode(self, parentNode, delNodeVal):
        assert(isinstance(parentNode, Node))

        # Search for the node to delete and check if it exist
        delNode = self.__searchInChildren(parentNode,delNodeVal)
        if delNode is None:
            LOG_DEBUG("Node : " + str(delNodeVal) + " Not Found to Delete", self.debugMode)
            return None
        
        assert(isinstance(delNode, Node))
        parent = delNode.getParent()

        # Case 1: Node has no child
        if not delNode.hasAnyChildren():
            self.__size -= 1
            if delNode.isRightChild():
                LOG_DEBUG("Node :" + str(delNodeVal) + " Right Ch & Leaf", self.debugMode)
                parent.setRightChild(None)
                return delNode
            elif delNode.isLeftChild():
                LOG_DEBUG("Node :" + str(delNodeVal) + " Left Ch & Leaf", self.debugMode)
                parent.setLeftChild(None)
                return delNode
            else:
                # It must be root Node
                return None
            
        # Case 2: Node has children
        # Get all its child nodes and re-insert it into the BST
        childrenList = self.getChildrenNodes(delNode)
        self.__size = self.__size - len(childrenList) -1

        if delNode.isRightChild():
            LOG_DEBUG("Node :" + str(delNodeVal) + " Right Ch & Not Leaf", self.debugMode)
            parent.setRightChild(None)
        elif delNode.isLeftChild():
            LOG_DEBUG("Node :" + str(delNodeVal) + " Left Ch & Not Leaf", self.debugMode)
            parent.setLeftChild(None)
        else:
            return None
        
        # Re-Insert the Children, Ids will be re-assigned too
        for child in childrenList:
            LOG_DEBUG("Re-Inserting Child-Node :" + str(child.getValue()) + " After deletion", self.debugMode)
            self.insertNode(child.getValue())
        return delNode

    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #
    # Get all the child nodes for a given Parent node
    # THe traversal is Root -> Left -> Right
    # @arg parentNode : Parent Node whose children we want to get
    # @arg childrenList : List of Children, this is taken by ref and returned
    #                     by the method
    # @ret Returns the Children in a List []
    #      Returns an empty List [] is there's no children
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def __getChildren(self, parentNode, childrenList):
        assert(isinstance(parentNode, Node))

        if parentNode.hasAnyChildren():
            if parentNode.hasLeftChild():
                LOG_DEBUG("FOUND LEFT-CHILD : " + str(parentNode.getLeftChild().getValue()) +
                    " FOR PARENT : " + str(parentNode.getValue()),self.debugMode)
                childrenList.append(parentNode.getLeftChild())
                self.__getChildren(parentNode.getLeftChild(), childrenList)
        
            if parentNode.hasRightChild():
                LOG_DEBUG("FOUND RIGHT-CHILD : " + str(parentNode.getRightChild().getValue()) +
                    " FOR PARENT : " + str(parentNode.getValue()),self.debugMode)
                childrenList.append(parentNode.getRightChild())
                self.__getChildren(parentNode.getRightChild(), childrenList)
        
        return childrenList

    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #
    # Helper function for searching
    # 
    # @arg parentNode : the Parent Node whose children are  to be searched for
    # @arg searchNodeval : Value of the Node to be searched for
    # @ret Returns the Node when found, None otherwise
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def __searchInChildren(self, parentNode, searchNodeVal):
        assert(isinstance(parentNode, Node))
        
        # Parent has no children to compare with
        if not parentNode.hasAnyChildren():
            LOG_DEBUG("Parent Node: " + str(parentNode.getValue()) + 
                    " Has NO CHILDREN ", self.debugMode)
            return None
        
        # Search in LEFT-SUBTREE
        if searchNodeVal <= parentNode.getValue():
            LOG_DEBUG("Searching in LEFT-SUBTREE ", self.debugMode)
            leftCh = parentNode.getLeftChild()
            return self.__searchInNode(leftCh, searchNodeVal)
        
        # Search in RIGHT-SUBTREE
        else:
            LOG_DEBUG("Searching in RIGHT-SUBTREE ", self.debugMode)
            rightCh = parentNode.getRightChild()
            return self.__searchInNode(rightCh, searchNodeVal)


    ##                    ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    #
    # Helper function for searching
    # 
    # @arg parentNode : the Parent Node whose children are also to be searched recursively
    #                   Searchs in the parent Node and the cotinue the search on 
    #                   Its chilren nodes
    # @arg searchNodeval : Value of the Node to be searched for
    # @ret Returns the Node when found, None otherwise
    #
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def __searchInNode(self, parentNode, searchNodeVal):
        if parentNode is None:
            return None
    
        if (parentNode.getValue() == searchNodeVal):
            LOG_DEBUG("Search Node: " + str(searchNodeVal) + 
                " Found in Node " + str(parentNode.getId()),self.debugMode)
            return parentNode
        else:
            LOG_DEBUG("Search Node: " + str(searchNodeVal) + 
                " Not Found. Searching is Children of " + 
                str(parentNode.getValue()),self.debugMode)
            return self.__searchInChildren(parentNode,searchNodeVal)

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

