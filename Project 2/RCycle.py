from Queue import *

def Restaurant(file):
	q = Queue()
	totalEnergy = 0
	restCt = 1

	with open(file, "r") as f:
		n = int(f.readline().strip())

		for i in range(restCt, n):
			gain, loss = f.readline().strip().split(" ")
			energy = [int(gain), int(loss)]

			totalEnergy += energy[0]
			totalEnergy -= energy[1]


			if totalEnergy < 0:
				restCt += 1
				pop = q.dequeue()
				q.enqueue(pop)
				break
			else:
				q.enqueue(energy)

	return restCt



print(Restaurant("problem3.input"))
