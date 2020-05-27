from .BstNode import BstNode as Node 

class BinarySearchTree():

    # constructor
    def __init__(self):
        self.rootNodePtr = None
    
    # simply insert this Node into the BST
    # Explanation: 
    # If the rootnode pointer is empty, the rootNodePtr points to newNode
    # If theres rootNode, Larger number than rootNode Value goes Right
    #   else goes left
    # ReturnCode : 1 = Root, 2 = RightSubTree, 3 = LeftSubTree
    def insertNode(self, newNodeValue):
        newNode = Node(newNodeValue)
    
        # rootNode Empty
        if not self.rootNodePtr:
            self.rootNodePtr = newNode
            return 1
        
        rootNode = self.rootNodePtr
        if newNode.value > rootNode.value :
            return self.insertIntoRightSubtree(rootNode.rightChildPtr, newNode)
        else:
            return self.insertIntoLeftSubtree(rootNode.leftChildPtr, newNode)


    # insert node into Right Subtree
    def insertIntoRightSubtree(self, nodePtr, newNode):
        if not nodePtr:
                nodePtr = newNode
                return 2
        
        rightNode = nodePtr
        if newNode.value > rightNode.value:
            return self.insertIntoRightSubtree(rightNode.rightChildPtr, newNode)
        else:
            return self.insertIntoLeftSubtree(rightNode.leftChildPtr, newNode)
    

    # insert Node into Left Sub Tree
    def insertIntoLeftSubtree(self, nodePtr, newNode):
        if not nodePtr:
                nodePtr = newNode
                return 3
        
        leftNode = nodePtr
        if newNode.value > leftNode.value:
            return self.insertIntoRightSubtree(leftNode.rightChildPtr, newNode)
        else:
            return self.insertIntoLeftSubtree(leftNode.leftChildPtr, newNode)
     
        
    
    #def searchNode(self, key):
    

    #def removeNode(self, key):
    
    
    
    
    def isEmpty(self):
        return self.root is None
    
    

    
    
    
    
