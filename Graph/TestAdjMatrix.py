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
        self.assertEqual(graph.searchNode('C').getId(), 3)

        ## TEST EDGE INSERTION
        self.assertEqual(graph.addEdge(23, 69), None)    # Node 23 Doesn't exist
        self.assertEqual(graph.addEdge('O', 'E'), None)    # Node 'E' Doesn't exist

        newEdge = graph.addEdge('O', 'C')
        self.assertEqual(newEdge.getStartNode().getValue(), 'O')    
        self.assertEqual(newEdge.getEndNode().getValue(), 'C')    
        self.assertEqual(newEdge.getStartNode().getId(), 0)    
        self.assertEqual(newEdge.getEndNode().getId(), 3)  
        self.assertEqual(newEdge.getEdgeWgt(), 1)    
        self.assertEqual(newEdge.getId(), "03")    
        
        newEdge.setEdgeWgt(99)
        self.assertEqual(newEdge.getEdgeWgt(), 99)    
        self.assertEqual(newEdge.isDirectedEdge(), True)    

        edgeList = graph.getEdgeList()
        if newEdge.getId() in edgeList:
            edge = edgeList[newEdge.getId()]
            self.assertEqual(edge.getStartNode().getValue(), 'O')    
            self.assertEqual(edge.getEndNode().getValue(), 'C')    
            self.assertEqual(edge.getStartNode().getId(), 0)    
            self.assertEqual(edge.getEndNode().getId(), 3)  
            self.assertEqual(edge.getEdgeWgt(), 99)    
            self.assertEqual(edge.getId(), "03")  

        ## TEST EDGE SEARCH BY ID
        self.assertEqual(graph.searchEdgeById(3), None)   # Id 3 doesn't exist
        searchEdge = graph.searchEdgeById("03")
        self.assertEqual(searchEdge.getStartNode().getValue(), 'O')    
        self.assertEqual(searchEdge.getEndNode().getValue(), 'C')    
        self.assertEqual(searchEdge.getStartNode().getId(), 0)    
        self.assertEqual(searchEdge.getEndNode().getId(), 3)  
        self.assertEqual(searchEdge.getEdgeWgt(), 99)    
        self.assertEqual(searchEdge.getId(), "03")
        
        ## TEST EDGE SEARCH BY START & END NODE VAL
        self.assertEqual(graph.searchEdgeBySource('O','A'), None)   # No edge between O->A
        searchEdge = graph.searchEdgeBySource('O','C')
        self.assertEqual(searchEdge.getStartNode().getValue(), 'O')    
        self.assertEqual(searchEdge.getEndNode().getValue(), 'C')    
        self.assertEqual(searchEdge.getStartNode().getId(), 0)    
        self.assertEqual(searchEdge.getEndNode().getId(), 3)  
        self.assertEqual(searchEdge.getEdgeWgt(), 99)    
        self.assertEqual(searchEdge.getId(), "03")

        ## TEST EDGE DELETION BY ID
        self.assertEqual(graph.removeEdgeById(3), None)   # Id 3 doesn't exist
        rmvEdge = graph.removeEdgeById("03")
        edgeList = graph.getEdgeList()
        if rmvEdge.getId() in edgeList:
            assert(False)                  # Removed Edge shouldnt be in the EdgeList


        ## TEST EDGE DELETION BY START & END NODE VAL
        newEdge = graph.addEdge('A', 'C')
        edgeList = graph.getEdgeList()
        if not newEdge.getId() in edgeList:
            assert(False)                  # New edge is part of the edgelist now
        self.assertEqual(graph.removeEdgeBySource('C', 'E'), None)   # Id 3 doesn't exist
        rmvEdge = graph.removeEdgeBySource('A', 'C')
        edgeList = graph.getEdgeList()
        if rmvEdge.getId() in edgeList:
            assert(False)                  # Removed Edge shouldnt be in the EdgeList

        self.assertEqual(len(edgeList), 0) # No Edges



