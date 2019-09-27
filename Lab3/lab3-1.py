class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.size() == 0
    
    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)
    
s = Queue()
str = "Thanapat"
for i in str:
    s.enQueue(i)
print(s.size())
print(s.items)
for i in range(0,s.size()):
    s.deQueue()
print(s.isEmpty())
print(s.items)