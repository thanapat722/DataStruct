class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        if next is None:
            self.next = None
            self.prev = None
        else:
            self.next = next
            self.prev = prev
    
    def __str__(self):
        return str(self.data)
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev
    
    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

class List:
        def __init__(self):
            self.head = None

        def __str__(self):
                if self.head is None:
                    print('Error Empty LinkedList')
                else:
                    p = self.head
                    while True:
                        print(p.getData(), end = ' ')
                        p = p.next
                        if p == None:
                            break

        def size(self):
            p = self.head
            count = 0
            while p is not None:
                count += 1
                p = p.getNext()
            return count
        
        def isEmpty(self):
            return self.head == None
        
        def append(self, data):
            p = Node(data)
            if self.head == None:
                self.head = p
            else:
                t = self.head
                while t.next != None:
                    t = t.next
                p.setPrev(t)
                t.next = p
        
        def addHead(self, data):
            p = Node(data)
            p.setNext(self.head)
            self.head.setPrev(p)
            self.head = p
        
        def isIn(self, data):
            if self.size() != 0:
                p = self.head
                while True:
                        if p.data != data:
                            p = p.next
                        else:
                            return p.data == data
                        if p == None:
                            break
                    
        def before(self, data):
            if self.size() > 1:
                p = self.head
                while True:
                        if p.data != data:
                            p = p.next
                        else:
                            return p.getPrev()
                        if p == None:
                            break
                # while p.data != None:
                #     if p.data != data:
                #         p = p.next
                #     else:
                #         return p.getPrev()
            else:
                print('Error: Your data is at head of LinkedList')
        
        def remove(self, data):
            if self.size() != 0 and self.isIn(data):
                p = self.head
                while p != None:
                    if p.next.getData() == data:
                        tmp = p.next
                        p.setNext(p.next.next)
                        return tmp
                    else:
                        p = p.next
            else:
                print('Error: Your data is not in LinkedList')
                
        # def removeTail(self):
        #     p = self.head
        #     while p.next != None:

        # def removeHead(self)
