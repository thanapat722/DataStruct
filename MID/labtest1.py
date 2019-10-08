class Stack:
    def __init__(self, list = None):
        if list is None:
            self.items = []
        else:
            self.items = list
        self.Size = len(self.items)
    
    def __str__(self):
        return str(self.items)
        
    def push(self, data):
        self.items.append(data)
        self.Size += 1

    def pop(self):
        self.Size -= 1
        return self.items.pop()

    def size(self):
        return self.Size
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.Size == 0

class Queue:
    def __init__(self, list = None):
        if list is None:
            self.items = []
        else:
            self.items = list
        self.Size = len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def enqueue(self, data):
        self.items.append(data)
        self.Size += 1
    
    def dequeue(self):
        self.Size -= 1
        return self.items.pop(0)

    def size(self):
        return self.Size
    
    def isEmpty(self):
        return self.Size == 0
    
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, head = None):
    if head is None:
        self.head = Node(None)
    else:
        self.head = head

            
