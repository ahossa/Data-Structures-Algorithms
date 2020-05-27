## UnitTest for Stack class
## TestStack.py 
## created: 09.02.2020 SUNDAY 

import unittest
from Stack import Stack


class TestStack(unittest.TestCase):
    
    # Test stack peek related methods
    def test_stack_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(55)
        stack.push(4)
        self.assertEqual(stack.peekTop(), 4)
        self.assertEqual(stack.peekBottom(), 1)

    # Test stack size related methods
    def test_stack_size(self):
        stack = Stack()
        stack.push("lion")
        stack.push("monkey")
        stack.push("chetaah")
        stack.pop()
        self.assertFalse(stack.isEmpty())        
        self.assertEqual(stack.size(), 2)
        stack.clear()
        self.assertTrue(stack.isEmpty())  
    






