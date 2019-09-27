class Stack:
    def __init__(self, list = None):
        if list == None:
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
        
def notMatch(open, c):
    if open is '(' and c is ')':
        return False
    elif open is '[' and c is ']':
        return False
    elif open is '{' and c is '}':
        return False
    else: return True

mstr = str(input("Enter input string: "))
s = Stack()
error = False
for c in mstr:
    if c is '(' or c is '[' or c is '{':
        s.push(c)
    elif c is ')' or c is ']' or c is '}':
        if s.isEmpty():
            error = True
        else:
            open = s.pop()
            if notMatch(open, c):
                error = True

if error:
    print("Mismatch")
else:
    if s.isEmpty == False:
        print("Mismatch")
    else:
        print("Match")