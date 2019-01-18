class LLNode(object):
	def __init__(self, data=None):
		self.data = data
		self.next = None

class SingleLL(object):
	def __init__(self):
		self.size = 0
		self.head = None

	def __len__(self):
		return self.size

	def __str__(self):
		v = []
		v.append('head')
		x = self.head
		while x != None:
			v.append('->')
			v.append(str(x.data))
			x.next
		return ' '.join(v)

	def search(self, key):
		x = self.head
		while x != None and x.data != key:
			x = x.next
		return x

	def insert(self, x):
		node = LLNode(x)
		node.next = self.head
		self.head = node
		self.size += 1

	def delete(self, x):
		y = self.head
		while y != None and y.next != x:
			y = y.next
		if y != None:
			y.next = x.next
			self.size -= 1
