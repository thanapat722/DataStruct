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
        self.items.pop(0)

def encode(string):
    a = 0
    if string == []:
        return print("Error : Emp\ty String")
    for ele in string:
        # for j in ele:
        x = ord(ele)
        y = s2.items[a]
        if x != 32:
            if x+y >= ord('a') and x+y <= ord('z') or x+y >= ord('A') and x+y <= ord('Z'):
                s3.enQueue(chr(x+y))
                a += 1
            else:
                s3.enQueue(chr(x+y - 26))
                a += 1
        else:
            s3.enQueue(' ')
        if a > s2.size()-1:
            a = 0

def decode(string):
    a = 0
    if string == []:
        return print("Error : Empty String")
    for ele in string:
        # for j in ele:
        x = ord(ele)
        y = s2.items[a]
        if x != 32:
            if x-y >= ord('a') and x-y <= ord('z') or x-y >= ord('A') and x-y <= ord('Z'):
                s4.enQueue(chr(x-y))
                a += 1
            else:
                s4.enQueue(chr(x-y + 26))
                a += 1
        else:
            s4.enQueue(' ')
        if a > s2.size()-1:
            a = 0
    # if s3.items != s4.items:
    #     s4.items = ["Error : Not Matched!"]


s1 = Queue()
s2 = Queue()
s3 = Queue()
s4 = Queue()
mes = input("Enter message to encode : ")
for i in mes:
    s1.enQueue(i)
code = input("Enter code seq. : ")
for i in code:
    s2.enQueue(int(i))
print("Your message : " + ''.join(s1.items))
print("Your code : " + str(s2.items))
encode(s1.items)
print("Encoded message : " + ''.join(s3.items))
decode(s3.items)
print("Decoded message : " + ''.join(s4.items))