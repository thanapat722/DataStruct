class node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right

    def __str__(self):
        return str(self.data)

    def getData(self): # accessor
        return self.data

    def getLeft(self): # accessor
        return self.left

    def getRight(self): # accessor
        return self.right

    def setData(self, data): # mutator
        self.data = data

    def setLeft(self, left): # mutator
        self.left = left
        
    def setRight(self, right): # mutator
        self.right = right
    
class BST:
    def __init__(self, root = None):         
        self.root = None if root is None else root 

    def addI(self, data):
        if self.root is None:             
            self.root = node(data)
        else:             
            fp = None       # father of p             
            p = self.root   # start comparing from root             
            while p:        # while p is not None
                fp = p                 
                p = p.left if data < p.data else p.right    # if data < p.data            
                                                            # p = p.left              
                                                            # else:                  
                                                            # p = p.left             
            if data < fp.data:
                fp.left = node(data)
            else:
                fp.right = node(data)
    
    def add(self, data):
        self.root = BST._add(self.root, data)

    def _add(root, data):   # recursive _add         
        if root is None:             
            return node(data)         
        else:             
            if data < root.data:                 
                root.left = BST._add(root.left, data)             
            else:                 
                root.right = BST._add(root.right, data)         
        return root      
    
    def inOrder(self):
        print('inOrder',end=' ')
        BST._inOrder(self.root)
        print()

    def _inOrder(root):         
        if root:   # if root is not None            
            BST._inOrder(root.left)
            print(root.data, end = ' ')
            BST._inOrder(root.right)

    def printSideway(self):         
        BST._printSideway(self.root, 0)
        print() 

    def _printSideway(root, level):         
        if root :  # if root is not None             
            BST._printSideway(root.right, level+1)             
            print('\t'*level, root.data, sep = '' )       
            BST._printSideway(root.left, level+1)
    
    def search(self, data):
        if self.root is None:
            return None
        fp = None
        p = self.root
        while p :
            fp = p
            if p.data == data:
                return p
            else:
                if data > p.data:
                    p = p.right
                else:
                    p = p.left

    def path(self, data):
        return BST._path(self.root, data)

    def _path(root, data):
        fp = None
        p = root
        path = []
        while p:
            fp = p
            path.append(p.data)
            if p.data == data:
                s = ''
                for i in path:
                    s += str(i)
                    if i != path[-1]:
                        s += ' -> '
                return s
            elif data > p.data:
                p = p.right
            elif data > p.data:
                p = p.left
            else:
                return None

    def delete(self, data):
        return BST._delete(self.root, data)

    def _delete(root, data):
        if root is not None:
            if data < root.data:
                root.left = BST._delete(root.left, data)
            elif data > root.data:
                root.right = BST._delete(root.right, data)
            else:
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp
                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp

                temp = BST.minRoot(root.right)
                root.data = temp.data
                root.right = BST._delete(root.right, temp.data)
            return root

    def minRoot(root):
        cur = root
        if cur.left is not None:
            cur = BST.minRoot(cur.left)
        return cur



l = [14, 4, 9, 7, 15, 3, 18, 16, 20, 5, 16] 
print(l) 
t = BST()
for ele in l:     
    t.addI(ele)
t.inOrder()
t.printSideway()
print('Search :',t.search(4))
print('Path :',t.path(18))
t.delete(199)
t.printSideway()