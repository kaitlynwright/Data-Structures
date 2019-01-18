from sys import argv
from enum import Enum

class Color(Enum):
	RED = 1
	BLACK = 2

class RBNode:
	def __init__(self, x: "comparable", t_dot_nil, other=None):
		self.key = x
		self.color = other
		self.parent = t_dot_nil
		self.left = t_dot_nil
		self.right = t_dot_nil

class RedBlackTree:
	class EmptyTree(Exception):
		def __init__(self, data=None):
			super().__init__(data)
	class NotFound(Exception):
		def __init__(self, data=None):
			super().__init__(data)	

	def __init__(self):
		self.root = self.nil = RBNode(None, None)
		self.nil.color = Color.BLACK

	def insert(self, z: RBNode) -> None:
		y = self.nil
		x = self.root
		while x != self.nil:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.parent = y
		if y == self.nil:
			self.root = z
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z
		z.left = z.right = self.nil
		z.color = Color.RED
		self.insert_fixup(z)

	def insert_fixup(self, z):
		while z.parent.color == Color.RED:
			if z.parent == z.parent.parent.left:
				y = z.parent.parent.right
				if y.color == Color.RED:
					z.parent.color = Color.BLACK
					y.color = Color.BLACK
					z.parent.parent.color = Color.RED
					z = z.parent.parent
				else:
					if z == z.parent.right:
						z = z.parent
						self.leftRotate(z)
					z.parent.color = Color.BLACK
					z.parent.parent.color = Color.RED
					self.rightRotate(z.parent.parent)
			else:
				y = z.parent.parent.left
				if y.color == Color.RED:
					z.parent.color = Color.BLACK
					y.color = Color.BLACK
					z.parent.parent.color = Color.RED
					z = z.parent.parent
				else:
					if z == z.parent.left:
						z = z.parent
						self.rightRotate(z)
					z.parent.color = Color.BLACK
					z.parent.parent.color = Color.RED
					self.leftRotate(z.parent.parent)
		self.root.color = Color.BLACK

	def leftRotate(self, x: RBNode) -> None:
		y = x.right
		x.right = y.left
		if y.left != self.nil:
			y.left.parent = x
		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.left = x
		x.parent = y

	def rightRotate(self, x: RBNode) -> None:
		y = x.left
		x.left = y.right
		if y.right != self.nil:
			y.right.parent = x
		y.parent = x.parent
		if x.parent  == self.nil:
			self.root = y
		elif x == x.parent.right:
			x.parent.left = y
		else:
			x.parent.right = y
		y.right = x
		x.parent = y

	def transplant(self, u: RBNode, v: RBNode) -> None:
		if u.parent == self.nil:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		v.parent = u.parent

	def remove(self, x: RBNode) -> None:
		z = self.search_iterative(self.root, x.key)
		if z == self.nil:
			raise RedBlackTree.NotFound('delete() cannot find element')
		y = z
		og_color = y.color
		if z.left == self.nil:
			x = z.right
			self.transplant(z, z.right)
		elif z.right == self.nil:
			x = z.left
			self.transplant(z, z.left)
		else:
			y = self.minimum(z.right)
			og_color = y.color
			x = y.right
			if y.parent == z:
				x.parent = y
			else:
				self.transplant(y, y.right)
				y.right = z.right
				y.right.parent = y
			self.transplant(z, y)
			y.left = z.left
			y.left.parent = y
			y.color = z.color
		if og_color == Color.BLACK:
			self.remove_fixup(x)

	def remove_fixup(self, x: RBNode) -> None:
		while x != self.root and x.color == Color.BLACK:
			if x == x.parent.left:
				w = x.parent.right
				if w.color == Color.RED:
					w.color = Color.BLACK
					x.parent.color = Color.RED
					self.leftRotate(x.parent)
					w = x.parent.right
				if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
					w.color = Color.RED
					x = x.parent
				else:
					if  w.right.color == Color.BLACK:
						w.left.color = Color.BLACK
						w.color = Color.RED
						self.rightRotate(w)
						w = x.parent.right
					w.color = x.parent.color
					x.parent.color = Color.BLACK
					w.right.color = Color.BLACK
					self.leftRotate(x.parent)
					x = self.root
			else:
				w = x.parent.left
				if w.color == Color.RED:
					w.color = Color.BLACK
					x.parent.color = Color.RED
					self.rightRotate(x.parent)
					w = x.parent.left
				if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
					w.color = Color.RED
					x = x.parent
				else:
					if  w.left.color == Color.BLACK:
						w.right.color = Color.BLACK
						w.color = Color.RED
						self.leftRotate(w)
						w = x.parent.left
					w.color = x.parent.color
					x.parent.color = Color.BLACK
					x.left.color = Color.BLACK
					self.rightRotate(x.parent)
					x = self.root
			x.color = Color.BLACK

	def minimum(self, x: RBNode) -> RBNode:
		if x == self.nil:
			raise RedBlackTree.EmptyTree('minimum() invoked on empty tree')
		while x.left != self.nil:
			x = x.left
		return x

	def maximum(self, x: RBNode) -> RBNode:
		if x == self.nil:
			raise RedBlackTree.EmptyTree('maximum() invoked on empty tree')
		while x.right != self.nil:
			x = x.right
		return x

	def search_iterative(self, x: RBNode, k: "comparable") -> RBNode:
		while x != self.nil and k != x.key:
			if k < x.key:
				x = x.left
			else:
				x = x.right
		return x

	def search(self, x: RBNode, k: "comparable") -> RBNode:
		z = self.search_iterative(x, k)
		if z == self.nil:
			raise RedBlackTree.NotFound('search({}) not found'.format(k))
		return z

	def preorder(self, n: RBNode, l: "list of keys") -> None:
		if n != self.nil and n != None:
			l.append(n.key)
			self.preorder(n.left, l)
			self.preorder(n.right, l)

	def to_list_preorder(self) -> "list of keys":
		l = []
		self.preorder(self.root, l)
		return l

	def inorder(self, n: RBNode, l: "list of keys") -> None:
		if n != self.nil and n != None:
			self.inorder(n.left, l)
			l.append(n.key)
			self.inorder(n.right, l)

	def to_list_inorder(self) -> "list of keys":
		l = []
		self.inorder(self.root, l)
		return l

	def postorder(self, n: RBNode, l: "list of keys") -> None:
		if n != self.nil and n != None:
			self.postorder(n.left, l)
			self.postorder(n.right, l)
			l.append(n.key)

	def to_list_postorder(self) -> "list of keys":
		l =[]
		self.postorder(self.root, l)
		return l

def driver() -> None:
	rbt = RedBlackTree()
	f = open(argv[1], "r")
	nl = int(f.readline().strip())
	for i in range(nl):
		l = f.readline().strip()
		if l == 'max':
			try:
				x = rbt.maximum(rbt.root)
				print(x.key)
			except RedBlackTree.EmptyTree as e:
				print('Empty')
		elif l == 'min':
			try:
				x = rbt.minimum(rbt.root)
				print(x.key)
			except RedBlackTree.EmptyTree as e:
				print("Empty")
		elif l == 'preprint':
			keys = rbt.to_list_preorder()
			if len(keys) == 0:
				print("Empty")
			else:
				strings = [str(x) for x in keys]
				print(' '.join(strings))
		elif l == 'inprint':
			keys = rbt.to_list_inorder()
			if len(keys) == 0:
				 print("Empty")
			else:
				strings = [str(x) for x in keys]
				print(' '.join(strings))
		elif l == 'postprint':
			keys = rbt.to_list_postorder()
			if len(keys) == 0 or keys == None:
				 print("Empty")
			else:
				strings = [str(x) for x in keys]
				print(' '.join(strings))
		else:
			v = l.split()
			if v[0] == 'insert':
				k = int(v[1])
				z = RBNode(k, rbt.nil)
				rbt.insert(z)
			elif v[0] == 'remove':
				k = int(v[1])
				try:
					z = rbt.search(rbt.root, k)
					rbt.remove(z)
				except RedBlackTree.NotFound as e:
					print('TreeError')
			elif v[0] == 'search':
				k = int(v[1])
				try:
					z = rbt.search(rbt.root, k)
					print('Found')
				except RedBlackTree.NotFound as e:
					print("NotFound")
			else:
				print("illegal input line:", l)
	f.close()	

if __name__ == '__main__':
	driver()
