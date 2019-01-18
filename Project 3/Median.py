from  minHeap import *
import sys

def rollingMedian(file):
	maxH = MinHeap()
	minH = MinHeap()
	l = []
	medians = []

	with open(file, "r") as f:
		n = int(f.readline().strip())
		for i in range(n):
			num = int(f.readline().strip())
			l.append(num)

	for i in range(len(l)):
		number = l[i]
		addNumber(minH, maxH, number)
		rebalance(minH, maxH)
		medians.append(calcRollingMedian(minH, maxH))

	for item in medians:
		print(item)

def rebalance(minHeap, maxHeap):
	if (maxHeap.size() - minHeap.size()) > 1:
		x = -maxHeap.remove()
		minHeap.insert(x)
	elif (minHeap.size() - maxHeap.size()) > 1:
		x = minHeap.remove()
		maxHeap.insert(-x)

def addNumber(minHeap, maxHeap, number):
	if (maxHeap.size() == 0) or (number < -maxHeap.look()):
		maxHeap.insert(-number)
	else:
		minHeap.insert(number)

def calcRollingMedian(minHeap, maxHeap):
	if minHeap.size() == maxHeap.size():
		median = round(((-maxHeap.array[1] + minHeap.array[1]) / 2), 1)
	else:
		if maxHeap.size() > minHeap.size():
			median = -maxHeap.array[1]
		else:
			median = minHeap.array[1]
	return median

if __name__ == "__main__":
	rollingMedian(sys.argv[1])
