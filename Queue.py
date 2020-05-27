## PYTHON QUEUE 
## Queue implementation Lists
## created: 09.02.2020 SUNDAY 

# Queue implementation with Lists
# Queue follows FIFO = First IN First Out
class Queue:

    # constructor
    def __init__(self):
        self.items = []
        self.size = 0
    
    # returns true if the queue is empty
    def isEmpty(self):
        return (self.Size() == 0)
    
    # adds an item to the queue
    def push (self, item):
        self.items.insert(0, item)
        self.size += 1

    # removes an item from the top of queue
    def pop(self):
        self.size -= 1
        return self.items.pop()
    
    # returns the size of Queue  
    def Size (self):
        return self.size

    # Take a peek at the top item of Queue
    def peekTop(self):
        return self.items[-1]
    
    # Take a peek at the bottom items of the Queue
    def peekBottom(self):
        return self.items[0]

    # Clear the Queue
    def clear(self):
        self.items.clear()
        self.size = 0
    
    # Prints the whole Queue in a single line
    def print(self):
        for item in self.items:
            print(item, end = " ")
        print ("\n")

## Class End