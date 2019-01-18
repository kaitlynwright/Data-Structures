import sys

def collage(file):
	magazine = {}
	outcome = "YES"

	with open(file, "r") as f:
		magCt, noteCt = f.readline().strip().split(" ")
		magWords = f.readline().strip().split(" ")
		noteWords = f.readline().strip().split(" ")

	if noteCt > magCt:
		outcome = "NO"
		return outcome

	for word in magWords:
		if word in magazine:
			magazine[word] += 1
		else:
			magazine[word] = 1

	for word in noteWords:
		if word in magazine and magazine[word] != 0:
			magazine[word] -= 1
		else:
			outcome = "NO"
	return outcome


if __name__ == "__main__":
	print(collage(sys.argv[1]))
