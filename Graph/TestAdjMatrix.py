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
        
        graph = Graph(5)
        self.assertEqual(graph.isEmpty(), False)
        self.assertEqual(graph.getNumNodes(), 5)
        self.assertEqual(graph.getMatrixSize(), 25)

        matrix = graph.getMatrix()
        id = 0
        for row in matrix:
            for node in row:
                id += 1
                self.assertEqual(node.getId(), id)
                self.assertEqual(node.getValue(), None)
                



