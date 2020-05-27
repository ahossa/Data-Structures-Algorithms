## UnitTest for LinkedList class
## TestLinkedList.py 
## created: 10.02.2020 MONDAY 

import unittest
from . import Node
from . import SLinkedList


class TestSLinkedList(unittest.TestCase):
    
    # Tests for Insertion related operations
    def test_insertion(self):
        sll = SLinkedList()
        self.assertFalse(sll.insertTailNode(Node(55))) # Empty, cant do
        sll.insertHeadNode(Node(2))                    # 2
        self.assertEqual(sll.peekHead(), 2)
        sll.insertHeadNode(Node(44))                   # 44 2
        self.assertEqual(sll.peekHead(), 44)
        self.assertEqual(sll.peekTail(), 2)
        self.assertTrue(sll.insertAfterHeadNode(Node(77))) # 44 77 2
        self.assertEqual(sll.peekHead(), 44)           
        self.assertEqual(sll.peekTail(), 2)
        self.assertEqual(sll.debugPrint(), "44 77 2")
        self.assertTrue(sll.insertTailNode(Node(55)))    # 44 77 2 55
        self.assertEqual(sll.peekTail(), 55)
        self.assertTrue(sll.insertAt(Node(43),2))        # 44 43 77 2 55
        self.assertTrue(sll.getNode(2).value, 43)
        self.assertEqual(sll.debugPrint(), "44 43 77 2 55")
        self.assertEqual(sll.searchList(Node(2)), 3)        
        self.assertEqual(sll.searchList(Node(111)), -1)        
 

    def test_Peek(self):
        sll = SLinkedList()
        sll.insertHeadNode(Node(30))
        self.assertEqual(sll.peekHead(), sll.peekTail())
        sll.insertHeadNode(Node(40))
        self.assertEqual(sll.peekHead(), 40)
        self.assertEqual(sll.peekTail(), 30)
    
    
    def test_deletion(self):
        sll = SLinkedList()
        sll.insertHeadNode(Node("A"))              # A
        sll.insertTailNode(Node("Z"))              # A Z
        self.assertEqual(sll.peekHead(), "A")
        self.assertEqual(sll.popHeadNode(), "A")   # Z
        self.assertEqual(sll.peekHead(), sll.peekTail())

    
    def test_data_access(self):
        sll = SLinkedList()
        sll.insertHeadNode(Node(99))    # 99
        sll.insertTailNode(Node(65))    # 99 65
        sll.insertAfterHeadNode(Node(69)) # 99 69 65
        self.assertEqual(sll.getHeadNode().value, 99)
        self.assertEqual(sll.getTailNode().value, 65)
        self.assertEqual(sll.getNode(2).value, 69)
        self.assertEqual(sll.getNode(0).value, None)   
        self.assertEqual(sll.getNode(-99).value, None) 
        sll.insertHeadNode(Node(75))  
        self.assertEqual(sll.getHeadNode().value, 75) # 75 99 69 65
        self.assertEqual(sll.getNode(2).value, 99)
        self.assertEqual(sll.debugPrint(), "75 99 69 65")

        