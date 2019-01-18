from Stack import *
import sys

def brackets(file):
	with open(file, "r") as f:
		strCt = int(f.readline().strip())

		for i in range(strCt):
			bracketStr = f.readline().strip()

			if isBalanced(bracketStr):
				print("YES")
			else:
				print("NO")

def isMatching(char1, char2):
	if(char1 == '(' and char2 == ')'):
		return True
	elif(char1 == '{' and char2 =='}'):
		return True
	elif(char1 == '[' and char2 == ']'):
		return True
	elif(char1 == '<' and char2 == '>'):
		return True
	else:
		return False


def isBalanced(bracketStr):
	s = Stack()
	balanced = True
	i = 0
	openBrackets = "({[<"
	closeBrackets = ")}]>"

	if (len(bracketStr) % 2) != 0:
		balanced = False

	while i < len(bracketStr) and balanced:
		bracket = bracketStr[i]

		if bracket in openBrackets:
			s.push(bracket)

		elif bracket in closeBrackets:
			topStack = s.pop()
			if not isMatching(topStack, bracket):
				balanced = False
		i += 1

	return balanced


if __name__ == "__main__":
	print(brackets(sys.argv[1]))
