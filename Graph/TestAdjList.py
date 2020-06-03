## UnitTest for Adjacency-List Graph class
## TestAdjList.py
## created: 02.06.2020 TUESDAY 

import unittest
from .AdjList import AdjList as Graph
from .Node import GraphNode as GphNode
from LinkedList.Node import LinkedListNode as LLNode 

class TestAdjList(unittest.TestCase):
    
    def test_AdjMatrix(self):
        print("TEST ADJ LIST GRAPH")

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
        self.assertEqual(graph.searchNode('C').getId(), 3)

        ## TEST EDGE INSERTION
        self.assertEqual(graph.addEdge(23, 69), False)     # Node 23 Doesn't exist
        self.assertEqual(graph.addEdge('O', 'E'), False)   # Node 'E' Doesn't exist
        self.assertEqual(graph.addEdge('O', 'C'), True)    # Both Nodes exist, would be succesfull
        self.assertEqual(graph.addEdge('O', 'B'), True)    # Both Nodes exist, would be succesfull
        self.assertEqual(graph.addEdge('A', 'C'), True)    # Both Nodes exist, would be succesfull

        edgeList = graph.getEdgeList()
        
        Node1 = LLNode('C')
        Node2 = LLNode('B')

        NodeOId = graph.searchNode('O').getId()
        self.assertEqual(edgeList[NodeOId].searchList(Node1), 1)   # Would return 1 since its the 1st node after head "O"
        self.assertEqual(edgeList[NodeOId].searchList(Node2), 2)   # Would return 2 since its the 2nd node after head "O"

        NodeAId = graph.searchNode('A').getId()
        self.assertEqual(edgeList[NodeAId].searchList(Node1), 1)   # Would return 1 since its the 1st node after head "A"
        self.assertEqual(edgeList[NodeAId].searchList(Node2), -1)  # Would -1 since there's no edge A->B , So LL Node B doesn't exist


        ## TEST EDGE SEARCH
        self.assertEqual(graph.searchEdge('O', 'E'), False)   # Node 'E' Doesn't exist
        self.assertEqual(graph.searchEdge('O', 'C'), 1)       # Would return 1 since its the 1st node after head "O"
        self.assertEqual(graph.searchEdge('O', 'B'), 2)       # Would return 2 since its the 2nd node after head "O"
        self.assertEqual(graph.searchEdge('A', 'C'), 1)       # Would return 1 since its the 1st node after head "A"
        self.assertEqual(graph.searchEdge('A', 'B'), -1)      # Would return -1 since node B exist but doesn't have A->B edge
