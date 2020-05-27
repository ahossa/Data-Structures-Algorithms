## Tree-Node Implementation in Python
## Describes a Node class for Tree Implementations
## created: 18.02.2020 TUESDAY

class TreeNode():
    def __init__(self, key, val = None, left = None,
                 right = None, parent = None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
    

    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.leftChild and self.rightChild)
    
    def hasAnyChildren(self):
        return (self.leftChild or self.rightChild)
    
    def hasBothChildren(self):
        return self.leftChild and self.rightChild
    
    def replaceNodeData(self, val)
