# This file generates a new Random pattern and places the resulting file in the ../Patterns folder.

from random import randint

def new_random_pattern(length):
	output = ""
	for i in range(0,length):
		randIndex = randint(0,149)
		randRed = randint(0,255)
		randGreen = randint(0,255)
		randBlue = randint(0,255)
		output += "[(0,%s): (0,0,0); (%s,%s): (%s,%s,%s); (%s,150): (0,0,0)] - Speed\n" % (str(randIndex), str(randIndex), str(randIndex+1), str(randRed), str(randGreen), str(randBlue), str(randIndex+1))
	with open("Patterns/_Random.txt", "w") as pattern_file:
		pattern_file.write(output)