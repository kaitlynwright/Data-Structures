import LinkedList
import copy
import sys

class Underflow(Exception):
	pass

class Stack():
	def __init__ (self):
		self.list = LinkedList.SingleLL()
		self.top = 0

	def is_empty(self):
		if self.list.head is None:
			return True
		else:
			return False

	def push(self, x):
		new_node = LinkedList.LLNode(x) #create new node with given data
		new_node.next = self.list.head	#move old head of list to the next to new node
		self.list.head = new_node  # make new node the head of the list

		self.top += 1             #increment the index of the top of the stack

	def pop(self):
		if self.is_empty():
			return Underflow("StackError")

		poppedItem = self.list.head.data # grab the value of the head of the list
		self.list.head = self.list.head.next  #  move the value in the next position to the head
		self.top -= 1        # decrement the index of the top of the stack
		return poppedItem

def print_stack(s):
	stackCopy = copy.deepcopy(s)
	printList = []
	if stackCopy.is_empty():
		print("Empty")
	else:
		for i in range(stackCopy.top):
			printList.append(str(stackCopy.pop()))
		print(' '.join(printList))

def driver():
	s = Stack()
	with open(sys.argv[1]) as f:
		n = int(f.readline().strip())
		for _ in range(n):
			in_data = f.readline().strip().split()
			action, value_option = in_data[0], in_data[1:]
			if action == "push":
				value = int(value_option[0])
				s.push(value)

			elif action == "pop":
				print(s.pop())

			elif action == "print":
				print_stack(s)

if __name__ == "__main__":
	driver()
