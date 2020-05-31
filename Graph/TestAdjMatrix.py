## UnitTest for Adjacency-Matrix Graph class
## TestAdjMatrix.py
## created: 30.05.2020 SATURDAY 

import unittest
from .AdjMatrix import AdjMatrix as Graph


class TestAdjMatrix(unittest.TestCase):
    
    def test_AdjMatrix(self):
        print("TEST ADJ MATRIX GRAPH")

        ## NOTE : Turn on the Debug Statements from constructor to see MAGIC!!
        
        ## TEST Graph constructor
        graph = Graph()
        self.assertEqual(graph.isEmpty(), True)
        self.assertEqual(graph.getNumNodes(), 0)
        self.assertEqual(graph.getNumEdges(), 0)

        ## TEST NODE INSERTION
        self.assertEqual(graph.addNode('O').getId(), 0)
        self.assertEqual(graph.addNode('A').getId(), 1)
        self.assertEqual(graph.addNode('B').getId(), 2)
        self.assertEqual(graph.addNode('C').getValue(), 'C')
        self.assertEqual(graph.addNode(69).getValue(), 69)
        
        self.assertEqual(graph.getNumNodes(), 5)
        self.assertEqual(graph.getNumEdges(), 0)


        ## TEST NODE SEARCH
        self.assertEqual(graph.searchNode('69'), None)
        self.assertEqual(graph.searchNode(69).getId(), 4)
        self.assertEqual(graph.searchNode('O').getId(), 0)

        ## TEST EDGE INSERTION
        #self.assertEqual(graph.addEdge(23), 0)





