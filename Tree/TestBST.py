## UnitTest for Binary Search Tree (BST) class
## TestBST.py 
## created: 05.03.2020 THURSDAY 

import unittest
from .BinarySearchTree import BinarySearchTree as BST


class TestBST(unittest.TestCase):
    
    # Test queue peek related methods
    def test_Insertion(self):
        print("TEST BST: Testing Insertion Start")

        ## NOTE : Turn on the Debug Statements to see 
        #         How Each node is inserted
        
        bst = BST()
        self.assertEqual(bst.isEmpty(), True)
        
        #     (90)
        self.assertEqual(bst.insertNode(90), 1)
        self.assertEqual(bst.isEmpty(), False)
        self.assertEqual(bst.getSize(), 1)
        
        #      (90)
        #    /      \
        #            (99)
        self.assertEqual(bst.insertNode(99), 2)
        #      (90)
        #     /     \
        #  (65)     (99)
        self.assertEqual(bst.insertNode(65), 3)
        #      (90)
        #     /     \
        #  (65)     (99)
        #  /  \     /   \
        #         (95)
        self.assertEqual(bst.insertNode(95), 4)
        #      (90)
        #     /     \
        #  (65)     (99)
        #  /  \     /   \
        #         (95)
        #        /    \
        #             (96)
        self.assertEqual(bst.insertNode(96), 5)
        #      (90)
        #     /     \
        #  (65)     (99)
        #  /  \     /   \
        #    (89) (95)
        #        /    \
        #             (96)
        self.assertEqual(bst.insertNode(89), 6)
        #      (90)
        #     /     \
        #  (65)     (99)
        #  /  \     /   \
        #(60) (89)(95)
        #        /    \
        #             (96)
        self.assertEqual(bst.insertNode(60), 7)
        self.assertEqual(bst.isEmpty(), False)
        self.assertEqual(bst.getSize(), 7)

        ## Searching
        self.assertEqual(bst.searchNode(96).getId(), 5)
        self.assertEqual(bst.searchNode(90).getId(), 1)
        self.assertEqual(bst.searchNode(69), None)
        
        ## Get all children
        children = bst.getChildrenNodes(bst.getRootNode())
        self.assertEqual(len(children), 6)


        


