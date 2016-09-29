# This file generates the RoundAndRound pattern and puts it in the ../Patterns folder.

import Helper

def generate_pattern():
	output = ""
	for i in range(0,150):
		output += Helper.instruction_for_pixel(i)
	Helper.write_pattern("RoundAndRound", output)


if __name__ == '__main__':
	print "Generating RoundAndRound..."
	generate_pattern()