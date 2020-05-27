## UnitTest for Binary Search Tree (BST) class
## TestBST.py 
## created: 05.03.2020 THURSDAY 

import unittest
from BinarySearchTree import BinarySearchTree as Tree


class TestBST(unittest.TestCase):
    
    # Test queue peek related methods
    def test_Insertion(self):
        tree = Tree()
        #     (90)
        self.assertEqual(tree.insertNode(90), 1)

        #      (90)
        #    /      \
        #            (99)
        self.assertEqual(tree.insertNode(99), 2)
        #      (90)
        #     /     \
        #  (65)     (99)
        self.assertEqual(tree.insertNode(65), 3)
        #      (90)
        #     /     \
        #  (65)     (99)
        #  /  \     /   \
        #         (95)
        self.assertEqual(tree.insertNode(95), -3)

