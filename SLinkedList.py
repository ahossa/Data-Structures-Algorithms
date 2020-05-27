## Singly-Linked-List Implementation in Python
## SLinkedList.py
## created: 10.02.2020 MONDAY

from Node import Node


class SLinkedList():

    # Constructor
    def __init__(self):
        # pHeadNode is just a ptr, HeadNode.next points to HeadNode
        self.pHeadNode = Node(None, 0)

    ##                    Insert Node at Head                           ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   
    # (1)If HeadNode doesnt exist, add the node at Head and Make HeadNode
    #    ptr point to the NewNode
    # (2)If HeahNode exists, make newnode point to oldHead and HeadNode
    #    ptr point to NewNode
    # Time Comp: O(1), constant time
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def insertHeadNode(self, NewNode):
        if self.pHeadNode.next is None:
            self.pHeadNode.next = NewNode
            return

        oldHead = self.pHeadNode.next
        self.pHeadNode.next = NewNode
        NewNode.next = oldHead

    # Insert a Node at the Tail
    # Time Comp: O(n), Linear
    def insertTailNode(self, newNode):
        if not self.pHeadNode.next:
            return False
        
        tmpNode = self.pHeadNode.next
        
        while tmpNode.next is not None :
            tmpNode = tmpNode.next

        tmpNode.next = newNode;
        return True;

    ##                    Insert a node after the head node                 ##
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   
    # (1) if the list is empty or pHeadNode doesnt point to Head, return false
    # (2) 1st Node will point to the New Node
    # (3) NewNode will point to the old 2nd node (now 3rd node)
    # Time Comp : O(1), constant time
    # # # # # # # # # # # # # # ## # # # # # # # # ## # # # # # # # # # # # # # #
    def insertAfterHeadNode(self, newNode):
        if self.pHeadNode.next is None:
            return False

        HeadNode = self.pHeadNode.next
        oldNodeAfterHead = HeadNode.next
        HeadNode.next = newNode
        newNode.next = oldNodeAfterHead
        return True

    # Insert Node at a position
    def insertAt(self, newNode, pos):
        if pos <= 0:
            return False
        if pos == 1:
            self.insertHeadNode(newNode)
            return True
        elif pos == self.getSize():
            self.insertTailNode(newNode)
            return True
        
        oldNode = self.getNode(pos)
        self.getNode(pos - 1).next = newNode
        newNode.next = oldNode
        return True





    # Take a peek at the head
    # Time Comp: O(1), constant time
    def peekHead(self):
        return self.pHeadNode.next.value

    # Take a peek at the tailNode
    # Time Comp: O(n)
    def peekTail(self):
        return self.getNode(self.getSize()).value
 

    # return the string version of the list
    def debugPrint(self, DoPrintOutput = False):
        list = ""
        if not self.pHeadNode.next:
            list = list + "EMPTY"
        else:
            tmpNode = self.pHeadNode.next
            while tmpNode.next:
                list = list + str(tmpNode.value) + " "
                tmpNode = tmpNode.next
            
            list = list + str(tmpNode.value)  ## last node
        
        if (DoPrintOutput):
            print(list)
        
        return list

    # Get the Total size of the list
    # Time Comp: O(n)
    def getSize(self):
        size = 0
        if not self.pHeadNode.next:
            return size
        tmpNode = self.pHeadNode.next
        while tmpNode.next:
            tmpNode = tmpNode.next
            size += 1
        return size + 1 # +1 for tail node
    
    # Get the Node at in a certain position
    # Time Comp:O(n)
    def getNode(self, pos):
        if pos == 1:
            return self.pHeadNode.next
        elif pos > self.getSize() or pos <= 0:
            return Node(None)

        tmpNode = self.pHeadNode.next
        for i in range(1,pos):
            tmpNode = tmpNode.next
        
        return tmpNode

    # Get the Head Node
    def getHeadNode(self):
        return self.pHeadNode.next
    
    # Get the tail Node
    def getTailNode(self):
        return self.getNode(self.getSize())
    
    # Delete the HeadNode
    def popHeadNode(self):
        oldHead = self.pHeadNode.next
        newHead = oldHead.next
        self.pHeadNode.next = newHead
        oldHead.next = None
        return oldHead.value

    # Delete the Tail Node
    def popTailNode(self):
        tmpNode = self.pHeadNode.next

    # Search List with Key
    # on found, returns the index. else returns -1
    # Time Comp: O(n)
    def searchList(self, key):
        tmpNode = self.pHeadNode.next
        ind = 0
        while tmpNode:
            if tmpNode.value == key.value:
                return ind
            tmpNode = tmpNode.next
            ind += 1
        return -1


# End SLinkedList()


