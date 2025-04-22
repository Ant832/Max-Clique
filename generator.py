from sys import argv
from random import randint
from math import sqrt

def graph_string(size):
	size += 1
	edges = set()

	for i in range(1, size):
		for j in range(randint(0, int(pow(size, 2/3)))):
			temp = randint(1, size-1)
			if(i != temp):
				edges.add((min(i, temp), max(i, temp)))
	result = ""
	for a, b in sorted(edges):
		result += f"{a}|{b}\n"
	print(len(edges))
	return result

def main():
	if(len(argv) == 3):
		result = graph_string(int(argv[1]))
		with open(argv[2], "w") as output:
			output.write(result)
		return
	print("Please provide file name to output")

if __name__ == "__main__":
	main()
