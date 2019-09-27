class Stack:
    def __init__(self, list = None):
        if list == None :
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

s = Stack()
name = input()
for i in name :
    s.push(i)
print(s.items)
print(s.pop())
print(s.items)
print(s.peek())
print(s.size())
print(s.isEmpty())