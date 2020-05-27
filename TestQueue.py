## UnitTest for Queue class
## TestQueue.py 
## created: 09.02.2020 SUNDAY 

import unittest
from Queue import Queue


class TestQueue(unittest.TestCase):
    
    # Test queue peek related methods
    def test_queue_peek(self):
        queue = Queue()
        queue.push(1)
        queue.push(55)
        queue.push(4)
        self.assertEqual(queue.peekTop(), 1)
        self.assertEqual(queue.peekBottom(), 4)

    # Test queue size related methods
    def test_stack_size(self):
        queue = Queue()
        self.assertTrue(queue.isEmpty())
        queue.push("lion")
        queue.push("monkey")
        queue.push("chetaah")
        queue.pop()
        self.assertFalse(queue.isEmpty())        
        self.assertEqual(queue.Size(), 2)
        queue.clear()
        self.assertTrue(queue.isEmpty())