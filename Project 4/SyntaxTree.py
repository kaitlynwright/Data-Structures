import sys

class STNode:
	def __init__(self, x: str):
		self.key = x
		self.left = None
		self.right = None

class SyntaxTree:
	def init_helper(self, i: int, l: 'list of strings') -> STNode:
		if i >= len(l):
			return None
		node = STNode(l[i])
		node.left = self.init_helper(2 * i, l)
		node.right = self.init_helper(2 * i + 1, l)
		return node

	def __init__(self, l: 'list of strings') -> 'complete syntax tree':
		self.root = self.init_helper(1, l)

	def inorder(self, x):
		l = []
		if x != None:
			l = self.inorder(x.left)
			l.append(str(x.key))
			l = l + self.inorder(x.right)
		return l

	def postorder(self, x):
		l = []
		if x != None:
			l = l +  self.postorder(x.left) + self.postorder(x.right)
			l.append(str(x.key))
		return l

	def expression_helper(self, x):
		ops = ['+', '-', '*']
		l = []

		if x != None:
			if x.key in ops:
				l.append('(')
			l = l + self.expression_helper(x.left)
			l.append(str(x.key))
			l = l + self.expression_helper(x.right)
			if x.key in ops:
				l.append(')')
		return l

	def expression(self):
		return ''.join(self.expression_helper(self.root))


	def evaluate(self, x):
		ops = ['+', '-', '*']

		if x is None:
			return 0

		if x.left is None and x.right is None:
			return int(x.key)

		leftSum = self.evaluate(x.left)
		rightSum = self.evaluate(x.right)

		if x.key == '+':
			return leftSum + rightSum
		elif x.key == '-':
			return leftSum - rightSum
		elif x.key == '*':
			return leftSum * rightSum

def main():
	with open(sys.argv[1]) as f:
		n = f.readline().strip()
		tree = [None] + f.readline().strip().split()

	print(tree)
	syntaxTree = SyntaxTree(tree)
	root = syntaxTree.root
	print(syntaxTree.expression())
	print(syntaxTree.evaluate(root))

if __name__ == '__main__':
	main()
