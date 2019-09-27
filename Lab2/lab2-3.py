class Stack:
    stack = []
    MAX_SIZE = 4

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def peek(self):
        return self.items[-1]

    def isFull(self):
        return len(self.items) is self.MAX_SIZE

    def push(self, i):
        if not self.isFull():
            self.items.append(i)

    def pop(self):
        #print("pop " + self.peek() + ", " , end = '')
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0
    
    def depart(self, i):
        temp = []
        if i in self.items:
            print("Car " + str(i) + " depart: ")
            for j in range(len(soi.items),int(soi.items.index(i)),-1) :
                print("pop" + self.peek() , end = ' ')
                temp.append(self.pop())
            temp.pop()
            temp.reverse()
            for k in temp:
                print("push" + k , end = ' ')
                self.items.append(k)
        else : print("Car " + str(i) + " cannot depart: NO CAR " + str(i))

soi = Stack()
i = 1

while(True):
    print("\n[= Car Soi Simulation =========]\n Please select a mode:\n [1] View soi\n [2] Add a car\n [3] Depart a car")
    mode = input(" Input => ")
    if mode is '1':
        print(soi.items)
    elif mode is '2':
        if not soi.isFull() :
            soi.push(str(i))
            print("Car " + str(soi.peek()) + " arrived     space left " + str(4-len(soi.items)))
            print(str(soi.items))
            i += 1
        else:
            i -= 1
            print("Car " + (str)(i+1) + " cannot arrive : SOI FULL")
    elif mode is '3':
        soi.depart(input("Enter car number to depart: "))
    else: print("Invalid mode")