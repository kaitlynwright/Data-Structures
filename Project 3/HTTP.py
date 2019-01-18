import minHeap
import sys

class queueNode:
	def __init__(self, ip_addr = None, tier = None, estimate = None, count = None):
		self.ip_addr = ip_addr
		self.tier = tier
		self.estimate = estimate
		self.count = count

	def __lt__(self, other):
		if self.estimate == other.estimate:
			return self.count < other.count
		else:
			return self.estimate < other.estimate

	def __gt__(self, other):
		if self.estimate == other.estimate:
			return self.count > other.count
		else:
			return self.estimate > other.estimate

	def __eq__(self, other):
		return self.estimate == other.estimate

	def __le__(self, other):
		if self.estimate == other.estimate:
			return self.count < other.count
		else:
			return self.estimate < other.estimate

	def __ge__(self, other):
		if self.estimate == other.estimate:
			return self.count > other.count
		else:
			return self.estimate > other.estimate

	def __ne__(self, other):
		return self.estimate != other.estimate

def requests(file):
	queueA = minHeap.MinHeap()
	queueB = minHeap.MinHeap()

	with open(file, "r") as f:
		n = int(f.readline().strip())
		for i in range(n):
			ip_addr, tier, estimate = f.readline().strip().split(" ")
			node = queueNode(str(ip_addr), str(tier), int(estimate), i)
			if tier == 'A':
				queueA.insert(node)
			elif tier == 'B':
				queueB.insert(node)
			i += 1

	for i in range(queueA.bhsize):
		print(queueA.remove().ip_addr)

	for i in range(queueB.bhsize):
		print(queueB.remove().ip_addr)

if __name__ == "__main__":
	requests(sys.argv[1])

