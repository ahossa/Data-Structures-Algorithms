## UnitTest for Binary Search Tree (BST) class
## TestBST.py 
## created: 05.03.2020 THURSDAY 

import unittest
from .BinarySearchTree import BinarySearchTree as BST


class TestBST(unittest.TestCase):
    
    # Test queue peek related methods
    def test_BST(self):
        print("TEST BST: Testing Insertion Start")

        ## NOTE : Turn on the Debug Statements from BST constructor to see MAGIC!!
        
        ## TEST BST INSERTION
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

        ## TEST BST SEARCHING
        self.assertEqual(bst.searchNode(96).getId(), 5)
        self.assertEqual(bst.searchNode(90).getId(), 1)
        self.assertEqual(bst.searchNode(69), None)
        
        ## TEST BST GET ALL CHILDREN
        children = bst.getChildrenNodes(bst.getRootNode())
        self.assertEqual(len(children), 6)


        ## TEST BST DELETION

        #      (90)
        #     /     \
        #  (65)     (95)
        #  /  \     /   \
        #(60) (89)      (96)
        self.assertEqual(bst.deleteNode(99).getId(), 2)
        self.assertEqual(bst.searchNode(95).getId(), 5)
        self.assertEqual(bst.searchNode(96).getId(), 6)
        

        # TEST BST IN-ORDER TRAVERSAL
        List = bst.traverseNodesInorder(bst.getRootNode())
        self.assertEqual(len(List), 6)
        self.assertLessEqual(List[0].getValue(), List[1].getValue())      # 60 < 65
        self.assertLessEqual(List[1].getValue(), List[2].getValue())      # 65 < 89
        for node in List:
            self.assertLessEqual(List[0].getValue(), node.getValue())      # 60 is the smallest number
            self.assertGreaterEqual(List[5].getValue(), node.getValue())   # 96 is the largest number

        # TEST BST GET SMALLEST & LARGEST
        self.assertEqual(bst.getSmallestNode().getValue(), 60);            # 60 is the Smallest in current BST 
        self.assertEqual(bst.getLargestNode().getValue(), 96);             # 96 is the Largest in current BST 

        # TEST ANCESTORS
        ancestorsList = bst.getAncestors(bst.getLargestNode())
        self.assertEqual(len(ancestorsList), 2)
        self.assertEqual(ancestorsList[0].getValue(), 95);            
        self.assertEqual(ancestorsList[1].getValue(), 90);            
        self.assertEqual(bst.getAncestors(bst.getRootNode()), []);        # Root node has no ancestor            

        # TEST GET LEAF NODES
        leafNodesList= bst.getLeafNodes();
        self.assertEqual(len(leafNodesList), 3)
        self.assertEqual(leafNodesList[0].getValue(), 60);            
        self.assertEqual(leafNodesList[1].getValue(), 89);     
        self.assertEqual(leafNodesList[2].getValue(), 96);     

        # HEIGHT OF BST
        #      (90)
        #     /     \
        #  (65)     (95)
        #  /  \     /   \
        #(60) (89)      (96)
        #                  \
        #                  (100)
        bst.insertNode(100)
        self.assertEqual(bst.getHeight(), 3) 
        


