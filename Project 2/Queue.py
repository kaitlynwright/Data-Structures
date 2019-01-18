import LinkedList
import copy
import sys

class Underflow(Exception):
	pass

class Queue():
	def __init__(self):
		self.list = LinkedList.SingleLL()
		self.end = 0

	def is_empty(self):
		if self.list.head is None:
			return True
		else:
			return False

	def enqueue(self, x):
		new_node = LinkedList.LLNode(x)
		if self.is_empty():
			self.list.head = new_node   # make new node the head if list is empty
		else:
			temp = self.list.head
			while temp.next is not None:
				temp = temp.next      # find the end of the queue
			temp.next = new_node          # place new node at the open space at end of queue

		self.end += 1

	def dequeue(self):
		if self.is_empty() is True:
			return Underflow("QueueError")

		removedItem = self.list.head.data     # isolate item at front of queue
		self.list.head = self.list.head.next   # move next item in queue to the front of the queue
		self.end -= 1
		return removedItem

def print_queue(s):
	queueCopy = copy.deepcopy(s)
	printList = []
	if queueCopy.is_empty():
		print("Empty")
	else:
		for i in range(queueCopy.end):
			printList.append(str(queueCopy.dequeue()))
		print(' '.join(printList))

def driver():
	q = Queue()
	with open(sys.argv[1]) as f:
		n = int(f.readline().strip())
		for _ in range(n):
			in_data = f.readline().strip().split()
			action, value_option = in_data[0], in_data[1:]
			if action == "enqueue":
				value = (value_option[0])
				q.enqueue(value)
			elif action == "dequeue":
				print(q.dequeue())
			elif action == "print":
				print_queue(q)

if __name__ == "__main__":
	driver()
