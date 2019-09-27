class Node:
    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.data)
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next

class List:
        def __init__(self):
            self.head = None

        def __str__(self):
            if self.head is None:
                print('Error: Empty LinkedList')
                return 'Error: Empty LinkedList'
            else:
                p = self.head
                out = ''
                while True:
                    out += str(p.getData()) + ' '
                    p = p.next
                    if p == None:
                        break
                return out

        def size(self):
            p = self.head
            count = 0
            while p != None:
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
                t.next = p
        
        def addHead(self, data):
            p = Node(data)
            p.setNext(self.head)
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
                            return False
            else:
                print('Error: Empty LinkedList')
                return 'Error: Empty LinkedList'
                    
        def before(self, data):
            if self.size() > 1:
                p = self.head
                while p != None:
                        if p.next.data != data:
                            p = p.next
                        else:
                            return p
                        if p == None:
                            break
            else:
                print('Error: Your data is at head of LinkedList')
                return  'Error: Your data is at head of LinkedList'
        
        def remove(self, data):
            if self.size() != 0 and self.isIn(data):
                p = self.head
                while p != None:
                    if p.next.data == data:
                        temp = p.next
                        p.setNext(p.next.next)
                        return temp
                    else:
                        p = p.next
            else:
                print('Error: Your data is not in LinkedList')
                return  'Error: Your data is not in LinkedList'
                
        def removeTail(self):
            p = self.head
            while p.next.next != None:
                p = p.next
            temp = p
            p.next = None
            return temp

        def removeHead(self):
            p = temp = self.head
            self.head = p.next
            return temp
        
        def indexOf(self, data):
            p = self.head
            index = 0
            while data != p.data:
                p = p.next
                index += 1
            return index

        def bottomUp(self, per):
            if self.size() > 0 and per <= 100 and per != 0:
                p = self.head
                for i in range(self.size()-1): # Looped to last index
                    p = p.next
                index = 1
                a = self.head
                while index != int(per * self.size() / 100) : # Looped to per index
                    a = a.next
                    index += 1
                p.next = self.head
                self.head = a.next
                a.next = None
                return self
            elif per > 100 or per <= 0:
                print('Error: Percent Error')
                return 'Error: Percent Error'
            else:
                print('Error: Empty LinkedList')
                return 'Error: Empty LinkedList'

        def deBottomUp(self, per):
            if self.size() > 0 and per <= 100:
                self.bottomUp(100-per)
                # p = self.head
                # for i in range(self.size()-1): # Looped to last index
                #     p = p.next
                # index = 1
                # a = self.head
                # while index != self.size() - int(per * self.size() / 100) : # Looped to size - per index
                #     a = a.next
                #     index += 1
                # p.next = self.head
                # self.head = a.next
                # a.next = None
            else:
                return 'Error: Empty LinkedList or Percent Exceed Limit'
        
        def riffle(self, per):
            if self.size() > 0 and per <= 100 and per != 0:
                count1 = int(per * self.size() / 100)
                count2 = int(self.size() - count1)
                temp1 = self.head
                temp2 = self.head
                for i in range(count1):
                    temp2 = temp2.next
                if count1 >= count2:
                    self.before(temp2.data).next = None
                    for i in range(0, count2):
                        n1 = temp1.next
                        n2 = temp2.next
                        temp1.next = temp2
                        temp2.next = n1
                        temp1 = n1
                        temp2 = n2
                else:
                    p = temp2
                    self.head = temp2
                    for i in range(0, count2-1):
                        p = p.next
                    p.next = None
                    for i in range(0, count1):
                        n1 = temp1.next
                        n2 = temp2.next
                        temp2.next = temp1
                        temp1.next = n2
                        temp1 = n1
                        temp2 = n2
            elif per > 100 or per <= 0:
                return 'Error: Percent Error'
            else:
                return 'Error: Empty LinkedList'

        def deRiffle(self, per):
            if self.size() > 0 and per <= 100 and per != 0:
                count1 = int(per * self.size() / 100)
                count2 = int(self.size() - count1)
                p1 = self.head
                p2 = self.head.next
                temp = p2
                temp2 = p1
                if per == 50:
                    for i in range(0, count1-1):
                        p1.next = p2.next
                        p1 = p2.next
                        p2.next = p1.next
                        p2 = p1.next
                    p1.next = temp
                elif per < 50:
                    for i in range(0, count1):
                        p1.next = p2.next
                        p1 = p2.next
                        if i != count1-1:
                            p2.next = p1.next
                            p2 = p1.next
                    p2.next = temp2  
                    self.head = temp
                else:
                    for i in range(0, count2):
                        p1.next = p2.next
                        p1 = p2.next
                        if i != count2-1:
                            p2.next = p1.next
                            p2 = p1.next
                    while p1.next != None:
                        p1 = p1.next
                    p1.next = temp
                    p2.next = None
            elif per > 100 or per <= 0:
                return 'Error: Percent Error'
            else:
                return 'Error: Empty LinkedList'
