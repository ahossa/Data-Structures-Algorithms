## PYTHON STACK
## Stack.py 
## created: 09.02.2020 SUNDAY 

# Stack implementation with Lists
class Stack:

    # constructor
    def __init__(self):
        self.items = []
    
    # returns true if the stack is empty
    def isEmpty(self):
        return (self.size() == 0)
    
    # adds an item to the stack
    def push (self, item):
        self.items.append(item)

    # removes an item from the top of Stack
    def pop(self):
        return self.items.pop()
    
    # returns the size of stack  
    def size (self):
        size = 0
        for item in self.items:
            size = size + 1
        return size

    # Take a peek at the top item of Stack
    def peekTop(self):
        return self.items[-1]
    
    # Take a peek at the bottom items of the Stack
    def peekBottom(self):
        return self.items[0]

    # Clear the Stack
    def clear(self):
        self.items.clear()
    
    # Prints the whole stack in a single line
    def print(self):
        for item in self.items:
            print(item, end = " ")
        print ("\n")

## Class End




## TODO
## Add a constructor that takes size and filler element