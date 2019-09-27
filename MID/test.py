# class Stack:
#     def __init__(self, list = None):
#         if list is None:
#             self.items = []
#         else:
#             self.items = list
#         self.listSize = len(self)
    
#     def __str__(self):
#         return str(self.items)
    
#     def push(self, data):
#         self.items.append(data)
#         self.listSize += 1

#     def pop(self):
#         self.listSize -= 1
#         return self.items.pop()
    
#     def peek(self):
#         return self.items[-1]

#     def isEmpty(self):
#         return self.items == []
    
#     def size(self):
#         return self.listSize

# class Queue:
#     def __init__(self, list = None):
#         if list is None:
#             self.items = []
#         else:
#             self.items = list
#         self.listSize = len(self)
    
#     def __str__(self):
#         return str(self.items)

#     def enQueue(self, data):
#         self.items.append(data)
#         self.listSize += 1

#     def deQueue(self):
#         self.listSize -= 1
#         return self.items.pop(0)
    
#     def isEmpty(self):
#         return self.items == []

#     def size(self):
#         return self.listSize

# class Node:
#     def __init__(self, data, next = None):
#         self.data = data
#         if next is None:
#             self.next = None
#         else:
#             self.next = next
    
#     def __str__(self):
#         return str(self.data)

# class LinkedList:
#     def __init__(self):
#         self.head = self.tail = None
#         self.listSize = 0
    
#     def __str__(self):
#         p = self.head
#         s = ''
#         while p is not None:
#             s += str(p.data) + ' '
#             p = p.next
#         return str(s)
    
#     def size(self):
#         return self.listSize
    
#     def isEmpty(self):
#         return self.listSize == 0

#     def append(self, data):
#         if self.listSize == 0:
#             pass

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

s = Stack([1,2,3,5,9])
s.pop()
s.push(10)
print('Peek:',s.peek(),'isEmpty:',s.isEmpty(),'Size:',s.size(),'\n','Stack:', s)

class Queue:
    def __init__(self, list = None):
        if list is None:
            self.items = []
        else:
            self.items = list
        self.Size = len(self.items)
    
    def __str__(self):
        return str(self.items)

    def enQueue(self, data):
        self.items.append(data)
        self.Size += 1

    def deQueue(self):
        self.Size -= 1
        return self.items.pop(0)

    def size(self):
        return self.Size

    def isEmpty(self):
        return self.Size == 0
    
class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
    
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.Size = 0

    def __str__(self):
        p = self.head
        s = ''
        while p is not None:
            s += str(p.data)
            s += ' '
            p = p.next
        return s
    
    def size(self):
        return self.Size
    
    def isEmpty(self):
        return self.Size == 0

    def append(self, data):
        if self.Size == 0:
            self.first(data)
        else:
            self.Size += 1
            node = Node(data)
            self.tail.next = node
            self.tail = node
    
    def addHead(self, data):
        if self.Size == 0:
            self.first(data)
        else:
            self.Size += 1
            node = Node(data)
            node.next = self.head
            self.head = node
    
    def first(self, data):
        self.Size += 1
        node = Node(data)
        self.head = self.tail = node
    
    def before(self, data):
        p = self.head
        while p.next is not None:
            if p.next.data == data:
                return p
            p = p.next
        return None
    
    def isIn(self, data):
        p = self.head
        while p.next is not None:
            if p.data == data:
                return True
            p = p.next
        return False
    
    def search(self, data):
        p = self.head
        while p is not None:
            if p.data == data:
                return p
            p = p.next
        return None
    
    def remove(self, data):
        self.Size -= 1
        node = self.search(data)
        if node is self.head:
            self.head = node.next
        elif node is self.tail:
            bef = self.before(data)
            bef.next = None
            self.tail = bef
        else:
            self.before(data).next = node.next
        return node

    def removeHead(self):
        return self.remove(self.head.data)

    def removeTail(self):
        return self.remove(self.tail.data)

a = LinkedList()
for i in range(0,11):
    a.append(i)
a.removeHead()
a.addHead(12)
a.remove(4)
a.removeTail()
print(a,'\nHead:',a.head,'Tail:',a.tail)
print('Size:',a.size(),'isIn:',a.isIn(5),'isEmpty:',a.isEmpty(),'Before 8 is',a.before(8))
