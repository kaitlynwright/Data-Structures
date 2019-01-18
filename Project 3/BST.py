import sys

class BSTNode:
	def __init__(self, key=None):
		self.key = key
		self.right = None
		self.left = None
		self.p = None

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def minimum(self, x):
		while x.left != None:
			x = x.left
		return x.key

	def maximum(self, x):
		while x.right != None:
			x = x.right
		return x.key

	def insert(self, z):
		y = None
		x = self.root

		while x != None:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.p = y

		if y == None:
			self.root = z		#tree was empty
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z

	def transplant(self, u, v):
		if u.p == None:
			self.root = v
		elif u == u.p.left:
			u.p.left = v
		else:
			u.p.right = v
		if v != None:
			v.p = u.p

	def remove(self, x):
		if x.left == None:
			self.transplant(x, x.right)
		elif x.right == None:
			self.transplant(x, x.right)
		else:
			y = self.minimum(x.right)
			if y.p != x:
				self.transplant(y, y.right)
				y.right = x.right
				y.right.p = y
			self.transplant(x, y)
			y.left = x.left
			y.left.p = y

	def search(self, x, k):
		if x == None or k == x.key:
			return x
		if k < x.key:
			return self.search(x.left, k)
		else:
			return self.search(x.right, k)

	def inorder(self, x):
		l = []
		if x != None:
			l = self.inorder(x.left)
			l.append(str(x.key))
			l = l + self.inorder(x.right)
		return l

	def preorder(self, x):
		l = []
		if x != None:
			l.append(str(x.key))
			l = l + self.preorder(x.right) + self.preorder(x.left)
		return l

	def postorder(self, x):
		l = []
		if x != None:
			l = l + self.postorder(x.right) + self.postorder(x.left)
			l.append(str(x.key))
		return l

	def to_list_inorder(self):
		return self.inorder(self.root)

	def to_list_preorder(self):
		return self.preorder(self.root)

	def to_list_postorder(self):
		return self.postorder(self.root)


def driver():
	bst = BinarySearchTree()

	with open(sys.argv[1]) as f:
		n = int(f.readline().strip())
		for _ in range(n):
			in_data = f.readline().strip().split()
			action, value_option = in_data[0], in_data[1:]
			if action == "insert":
				value = int(value_option[0])
				node = BSTNode(value)
				bst.insert(node)
			elif action == "remove":
				value = int(value_option[0])
				x = bst.search(bst.root, value)
				if x == None:
					print("TreeError")
				else:
					bst.remove(x)
			elif action == "search":
				value = int(value_option[0])
				x = bst.search(bst.root, value)
				if x != None:
					print("Found")
				else:
					print("NotFound")
			elif action == "max":
				if bst.root != None:
					print(bst.maximum(bst.root))
				else:
					print("Empty")
			elif action == "min":
				if bst.root != None:
					print(bst.minimum(bst.root))
				else:
					print("Empty")
			elif action == "preprint":
				if bst.root != None:
					print(' '.join(bst.to_list_preorder()))
				else:
					print("Empty")
			elif action == "inprint":
				if bst.root != None:
					print(' '.join(bst.to_list_inorder()))
				else:
					print("Empty")
			elif action == "postprint":
				if bst.root != None:
					print(' '.join(bst.to_list_postorder()))
				else:
					print("Empty")
if __name__ == "__main__":
	driver()
