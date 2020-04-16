import collections
import tree
import string
import random

class Bin_Tree(tree.Tree):
    def __init__(self):
        self._root = self.Position()
    
    class Position(tree.Tree.Position):
        def __init__(self):
            self._data = None
            self._left = None
            self._right = None

        def element(self):
            return self._data

        def getleft(self):
            return self._left

        def getright(self):
            return self._right

        def mkelement(self,data):
            self._data = data    

        def mkleft(self, posn):
            self._left = posn

        def mkright(self, posn):
            self._right = posn    

        def __eq__(self, other):
            if other == None:
                return False
            else:
                return self.element() == other.element() 

    def root(self):
        return self._root

    def insert_preorder(self, data):
        if self._root.element() == None:
            self._root.mkelement(data)
        else:
            posn = self._root
            while posn != None:
                if data <= posn.element():
                    if posn.getleft() != None:
                        posn = posn.getleft()
                    else:
                        posn.mkleft(self.Position())
                        posn.getleft().mkelement(data)
                        posn = None
                else:
                    if posn.getright() != None:
                        posn = posn.getright()
                    else:
                        posn.mkright(self.Position())
                        posn.getright().mkelement(data)
                        posn = None

    def parent(self, p):
        if p == self._root:
            return None
        else:
            posn = self._root
            while posn != None:
                if p.element() <= posn.element():
                    if posn.getleft().__eq__(p):
                        return posn
                    else:
                        posn = posn.getleft()
                else:
                    if posn.getright().__eq__(p):
                        return posn
                    else:
                        posn = posn.getright()

    def num_children(self,p):
        if p.getleft() != None and p.getright() != None:
            return 2
        elif p.getleft() == None and p.getright() == None:
            return 0
        else:
            return 1

    #list -> Pre-Order
    def children(self, p):
        L = []
        if self.num_children(p) == 2:
            L.append(p.getleft())
            L.append(p.getright())
            return L
        elif p.getleft() != None:
            L.append(p.getleft())
            return L
        elif p.getright() != None:
            L.append(p.getright())
            return L
        else:
            return L

    def __len__(self):
        counter = 1
        if self.is_empty == True:
            return counter - 1
        else:
            p = self._root.getleft()
            while p != None:
                counter += self.num_children(p)
                p = p.getleft()
            p = self._root.getright()
            while p !=None:
                counter += self.num_children(p)
                p = p.getright()
            return counter + self.num_children(self._root) 

    def k(self): #LPR
        p = self._root
        while p != None:
            p = p.getleft()
        self.inorder(p)

    def inorder(self,p): #LPR
        if p != None and p.getleft() != None:
            self.inorder(p.getleft())
        if p != None:
            print(p.element())
        if p != None and p.getright() != None:
            self.inorder(p.getright())

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self._root):
                print(p.element())

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self._root):
                print(p.element())

###############################################################################
b = Bin_Tree()
#Inserts Alphabests into BinTree
for i in string.ascii_uppercase:
    b.insert_preorder(i)

#Since the Alphabet Values are in ascending order, the binary tree is imperfect
#Inserting Random Numbers into the binary tree will return a more conventional
# display as per traversal method
#As to this regard, i have taken initiative to demonstrate this with numbers as well

print('For Alphabets')
print('Inorder Traversal')
b.inorder(b.root())
print('Preorder Traversal')
b.preorder()
print('Postorder Traversal')
b.postorder()
print('################################################################\n')
BT = Bin_Tree()
L = []
#Generates Random Numbers and places in list
for i in range(20):
    L.append(random.randint(0,100))
#Inserts generated numbers into BinTree
for i in L:
    BT.insert_preorder(i)
print('For Random Numbers')
print('Inorder Traversal')
BT.inorder(BT.root())
print('Preorder Traversal')
BT.preorder()
print('Postorder Traversal')
BT.postorder()

