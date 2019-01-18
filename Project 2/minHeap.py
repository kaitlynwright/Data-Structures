import sys

class HeapError(Exception):
	pass

class MinHeap:
	def __init__(self):
		self.heap = []
		self.heapSize = 0

	def minHeapify(self, i):
		i -= 1
		left = 2*i
		right = 2*i+1
		if left >= self.heapSize and self.heap[left] < self.heap[i]:
			smallest = left
		else:
			smallest = i

		if right >= self.heapSize and self.heap[right] < self.heap[smallest]:
			smallest = right

		if smallest != i:
			temp = self.heap[i]
			self.heap[i] = self.heap[smallest]
			self.heap[smallest] = self.heap[i]
			self.minHeapify(smallest)

	def insert(self, x):
		i = self.heapSize
		self.heap.append(x)
		self.heapSize += 1

		while i > 1 and self.heap[i // 2] > self.heap[i]:
			temp = self.heap[i // 2]
			self.heap[i // 2] = self.heap[i]
			self.heap[i] = temp
			i =  i // 2

	def remove(self):
		if self.heapSize < 1:
			HeapError("heap underflow")
		min = self.heap[1]
		self.heap[1] = self.heap[self.heapSize - 1]
		self.minHeapify(1)
		return min

	def look(self):
		if self.heapSize == 0:
			return HeapError("Empty")
		else:
			return self.heap[1]

	def size(self):
		return self.heapSize

	def is_empty(self):
		if self.heapSize == 0:
			return True
		else:
			return False

	def to_string(self):
		list = []
		if self.heapSize == 0:
			return HeapError("Empty")
		for i in range(self.heapSize):
			list.append(str(self.heap[i]))
		return ' '.join(reversed(list))


def driver():
	minHeap = MinHeap()
	with open(sys.argv[1]) as f:
		n = int(f.readline().strip())
		for _ in range(n):
			in_data = f.readline().strip().split()
			action, value_option = in_data[0], in_data[1:]
			if action == "insert":
				value = int(value_option[0])
				minHeap.insert(value)
			elif action == "remove":
				print(minHeap.remove())
			elif action == "print":
				stringHeap = minHeap.to_string()
				print(stringHeap)
			elif action == "size":
				print(minHeap.heapSize)
			elif action == "best":
				print(minHeap.look())

if __name__ == "__main__":
	driver()
