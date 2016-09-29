# This file generates the Snake pattern and puts it in the ../Patterns folder.

import Helper

def generate_pattern():
	length = 10
	output = ""
	for i in range(0,150):
		ranges = []
		if i+length > 150:
			ranges.append((i,150))
			ranges.append((0,length-(150-i)))
		else:
			ranges.append((i,i+length))
		range_mapping = {}
		for aRange in ranges:
			range_mapping[aRange] = "Color"
		output += Helper.instruction_for_ranges(range_mapping)
	Helper.write_pattern("Snake",output)


if __name__ == '__main__':
	print "Generating Snake..."
	generate_pattern()