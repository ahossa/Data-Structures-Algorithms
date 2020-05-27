## Tree-Node Implementation in Python
## Describes a Node class for Tree Implementations
## created: 18.02.2020 TUESDAY

class TreeNode():
    def __init__(self, id, val = None, left = None,
                 right = None):
        self.id = id
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = None

        ## Set the Parent to Current Node if 
        #  Right Child or Left child exists
        if self.leftChild is not None :
            self.leftChild.parent = self
        if self.rightChild is not None :
            self.rightChild.parent = self

    
    #### 
    # Returns the Id of the Node 
    def getId(self):
        return self.id

    ####
    # Sets the value for Node 
    def setValue(self, value):
        self.val = value
    ####
    # Returns the Value Node 
    def getValue(self):
        return self.val
        
    ####
    # Returns the Parent of the Node 
    # Note: Parent Can only be set by Constructor
    #       Since Only Parent can set Child, eiter left or right
    #       Child Shouldn't be able to set parent 
    def getParent(self):
        return self.parent
    
    ####
    # Sets the Left child for Node 
    def setLeftChild(self, leftChNode):
        self.leftChild = leftChNode
        leftChNode.parent = self

    ####
    # Returns the Left child of the node
    def getLeftChild(self):
        return self.leftChild

    ####
    # Sets the Right child for Node 
    def setRightChild(self, rgtChNode):
        self.rightChild = rgtChNode
        rgtChNode.parent = self
    
    ####
    # Returns the Right child of the node
    def getRightChild(self):
        return self.rightChild


    #### 
    # Returns TRUE if there's a Left Child for the Node
    def hasLeftChild(self):
        return self.leftChild is not None
    
    #### 
    # Returns TRUE if there's a Right Child for the Node    
    def hasRightChild(self):
        return self.rightChild is not None
    
    ####
    # ROOT : Beginning of the tree. The HeadNode
    # Returns TRUE if It's the root node for the tree
    def isRoot(self):
        return self.parent is None
    
    ####    
    # LEAF : The bottom-most Nodes of the Tree
    #        Who doesn't have any children
    #        
    #  ** Note : For a Single Node Tree ROOT = LEAF ** 
    # 
    # Returns TRUE if node is a leaf
    def isLeaf(self):
        return not (self.leftChild and self.rightChild)
    
    ####
    # Returns TRUE is Node has any Children
    def hasAnyChildren(self):
        return (self.leftChild is not None or 
                self.rightChild is not None)
    
    ####
    # Returns TRUE if Node has both LEFT + RIGHT child
    def hasBothChildren(self):
        return ( self.leftChild is not None and 
                 self.rightChild is not None)
    

