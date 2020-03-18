class Node:
    def __init__(self,data,left,right):
        self._data = data
        self._left = left
        self._right = right

    def getdata(self):
        return self._data

    def getleft(self):
        return self._left

    def getright(self):
        return self._right

    def changedata(self,data):
        self._data = data

    def changeleft(self,left):
        self._left = left

    def changeright(self,right):
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root = None

    def getroot(self):
        if self._root == None:
            return "Empty Tree"
        else:
            return self._root

    def insertdata(self,data,node1):
        if self._root == None:
            self._root = Node(data,None,None)
        else:
            node = node1
            while node != None:
                if node.getleft() == None and data <= node.getdata():
                    node.changeleft(Node(data,None,None))
                    node == None
                elif node.getright() == None and data > node.getdata():
                    node.changeright(Node(data,None,None))
                    node = None
                elif data <= node.getdata():
                    node = node.getleft()
                else:
                    node = node.getright()
    
    def print(self):
        if self._root == None:
            print("Empty Tree")
        else:
            node = self._root
            while node != None:
                print(node.getdata())
                if node.getleft() != None:
                    node = node.getleft()
                elif node.getright() != None:
                    node = node.getright()
                else:
                    node = None
    
    def search(self,data):
        if self._root == None:
            return False
        else:
            node = self._root
            while node != None:
                if node.getdata() == data:
                    return True
                elif node.getleft() == None and node.getright() == None:
                    return False
                elif data <= node.getdata():
                    node = node.getleft()
                else:
                    node = node.getright()

    def remove(self,data):
        if self.search(data) == False:
            print("data not in Tree")
        else:
            node = self._root
            LIST = []
            while node != None:
                if node.getdata() == data:
                    temp = node
                    while temp != None:
                        LIST.append(temp.getdata())
                        if temp.getleft() != None:
                            temp = temp.getleft()
                        elif temp.getright() != None:
                            temp = temp.getright()
                        else:
                            temp = None
                    first = LIST[1] 
                    LIST.remove(LIST[0])
                    LIST.remove(LIST[0])
                    node.changedata(first)
                    node.changeleft(None)
                    node.changeright(None)
                    for i in LIST:
                        self.insertdata(i,node)
                elif data <= node.getdata() and node.getleft() != None:
                    node = node.getleft()
                else:
                    node = node.getright()


BT = BinaryTree()
for i in range(15):
    BT.insertdata(i+1,BT.getroot())

#BT.print()
#print(BT.search(13))
BT.remove(14)
BT.print()