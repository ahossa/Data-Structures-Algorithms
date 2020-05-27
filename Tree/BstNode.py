## BST Node Implementation in Python
## Describes a Node class for BST Implementations
## created: 25.02.2020 TUESDAY

class BstNode():
    def __init__(self, value, leftChild = None,
                rightChild = None):
        
        self.value = value
        self.leftChildPtr = leftChild
        self.rightChildPtr = rightChild
        
        
        # BST doesnt have an index
        # we're working with index only for debugging purposes
        self.Index = 0   

