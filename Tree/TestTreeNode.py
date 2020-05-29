## UnitTest for TreeNode class
## TestTreeNode.py 
## created: 27.05.2020 WEDNESDAY

import unittest
from .TreeNode import TreeNode

class TestTreeNode(unittest.TestCase):

    ### 
    # TEST TreeNode Constructor
    def test_Constructor(self):
        
        # node1 with Id + Value
        #      (1)
        node1 = TreeNode(1,'A')
        self.assertEqual(node1.getId(), 1)
        self.assertEqual(node1.getValue(), 'A')

        # node2 with node1 as left child
        #      (2)
        #     /     \
        #  (1)      ( )
        node2 = TreeNode(2,'B',node1)
        self.assertEqual(node2.getId(), 2)
        self.assertEqual(node2.getValue(), 'B')
        self.assertEqual(node2.getLeftChild().getId(), 1)
        self.assertEqual(node2.getLeftChild().getValue(), 'A')

        # node3 with node1 as left child
        #      (3)
        #     /     \
        #  ( )      (1)
        node3 = TreeNode(3,'C', None, node1)
        self.assertEqual(node3.getId(), 3)
        self.assertEqual(node3.getValue(), 'C')
        self.assertEqual(node3.getRightChild().getId(), 1)
        self.assertEqual(node3.getRightChild().getValue(), 'A')

        print("TEST TREE-NODE: Testing Constructor Complete")


    ### 
    # TEST TreeNode Child related methods
    def test_Child_Related_Methods(self):
        
        # node1 with Id + Value
        # node2 with node1 as left child
        #      (2)
        #     /     \
        #  (1)      ( )
        node1 = TreeNode(1,'A')
        node2 = TreeNode(2,'B',node1)
        
        self.assertEqual(node2.hasAnyChildren(), True)
        self.assertEqual(node2.hasLeftChild(), True)
        self.assertEqual(node2.hasRightChild(), False)
        
        self.assertEqual(node2.getLeftChild().getId(), 1)
        self.assertEqual(node2.getLeftChild().getValue(), 'A')        
        self.assertEqual(node2.getRightChild(), None)
        
        # 3 as left child
        #      (2)
        #     /     \
        #  (1)      (3)
        node2.setRightChild(TreeNode(3,'C'));
        self.assertEqual(node2.getRightChild().getId(), 3)
        self.assertEqual(node2.getRightChild().getValue(), 'C')

        self.assertEqual(node2.hasBothChildren(), True)
        

        ## ROOT - LEAF Relationship
        self.assertEqual(node2.isRoot(), True)
        self.assertEqual(node1.isRoot(), False)
        
        self.assertEqual(node2.isLeaf(), False)
        self.assertEqual(node1.isLeaf(), True)
        self.assertEqual(node2.getRightChild().isLeaf(), True)
        self.assertEqual(node2.getRightChild().isRoot(), False)

        ## CIRCULAR PARENT - CHILD RELATIONSHIP
        self.assertEqual(node2.getRightChild().getParent().getId(), 2)
        self.assertEqual(node2.getRightChild().getParent().getValue(), 'B')

        self.assertEqual(node2.getLeftChild().getParent().getId(), 2)
        self.assertEqual(node2.getLeftChild().getParent().getValue(), 'B')

        # LEFT - RIGHT Child Relationship
        self.assertEqual(node1.isRightChild(), False)
        self.assertEqual(node1.isLeftChild(), True)
        self.assertEqual(node1.isEqual(node2), False)
        
        print("TEST TREE-NODE: Testing Child Methods Complete")






 