import string as string
#import sys
#sys.setrecursionlimit(10**6) 
#Binary Tree
########################################################################################
class Node:
	#Node: data left right
	def __init__(self, data):
		self._data = data
		self._left = None
		self._right = None
	
	#To get the data in a node
	def get_data(self):
		return self._data

	#To mutate data in a node
	def change_data(self, data):
		self._data = data

	#To get the left node
	def get_left(self):
		return self._left

	#To mutate data in left node
	def change_left(self, node):
		self._left = node
	
	#To get right node
	def get_right(self):
		return self._right

	#To change data in right node
	def change_right(self, node):
		self._right = node

########################################################################################
class BinTree:
	#BinTree: A Binary Tree can perform the following operations
	# get_root()
	#	Purpose: To get the root of a BinTree
	# isEmpty()
	#	Purpose: To determine if BinTree is empty
	# search(Node-data)
	#	Purpose: To determine if Node-data is in a BinTree
	# insert(Node)
	#	Purpose: To insert a node into a BinTree
	# deletetree()
	#	Purpose: To delete entire BinTree
	# delete(a-node)
	#	Purpose: To remove a node from BinTree
	# print()
	#	Purpose: To print out all the data in a BinTree


	#Bintree: root
	def __init__(self):
		self._root = None

	#To get the root of a BinTree
	def get_root(self):
		return self._root

	#To determine if root is empty
	def isEmpty(self):
		if self._root == None:
			return True

	#Root->Left->Right
	#To search if Node-data is in BinTree
	def search(self, key):
		if(self._root != None):
			return self.searchhelper(key, self._root)
		else:
			return False
	
	#To help search function
	def searchhelper(self, key, node):
		if(key == node.get_data()):
			return True
		elif(key < node.get_data() and node.get_left() != None):
			return self.searchhelper(key, node.get_left())
		elif(key > node.get_data() and node.get_right() != None):
			return self.searchhelper(key, node.get_right())
		else:
			return False

			
	#Root->Left->Right
	#To insert a node in the BinTree
	def insert(self, node):
		if self.search(node.get_data()) == True:
			print("Error: Duplicate Data")
		else:
			if self.isEmpty():
				self._root = node
			else:
				self.inserthelper(node, self._root)

	#To help insert function
	def inserthelper(self, node, root):
		if (node.get_data() < root.get_data()):
			if(root.get_left() != None):
				self.inserthelper(node, root.get_left())
			else:
				root.change_left(node)
		else:
			if(root.get_right() != None):
				self.inserthelper(node, root.get_right())
			else:
				root.change_right(node)

	#To delete entire Binary Tree
	def deletetree(self):
		self._root = None
	
	#To remove a node from the Binary Tree
	def delete(self, node):
		if self.isEmpty():
			print("Empty Tree")
		elif self.search(node.get_data()) == False:
			print("Node does not exist")
		else:
			self.deletehelper(node,self._root)

	#Function help delete function
	def deletehelper(self, node, root):
		elem = []
		elem = self.dellist(self._root,elem)
		elem.remove(node.get_data())
		self._root = None
		for i in elem:
			self.insert(Node(i))
	
	#To help delete helper function
	def dellist(self,root,elem):
		if(root != None):
			elem.append(root.get_data()) 
			self.dellist(root.get_left(),elem)
			self.dellist(root.get_right(),elem)
		return elem
			
	#To print out all the data in a BinTree
	def print(self, node):
		if(node != None):
			print(node.get_data())
			self.print(node.get_left())
			self.print(node.get_right())

	def lister(self, node, LIST):
		if(node != None):
			LIST.append(node.get_data())
			self.lister(node.get_left(),LIST)
			self.lister(node.get_right(),LIST)
		return LIST	

#Test
BT = BinTree()
ET = BinTree()
for i in string.ascii_lowercase:
    BT.insert(Node(i))

#print(BT.search("a"))
#BT.print(BT.get_root())
#BT.insert(Node("ff"))
#BT.deletetree()
#BT.delete(Node("m"))
#BT.print(BT.get_root())
LIST = []
print(BT.lister(BT.get_root(),LIST))






		