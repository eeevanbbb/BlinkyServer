# This file generates the Spoopy pattern and puts it in the ../Patterns folder.

import Helper

def generate_pattern():
	length = 10
	output = ""
	colors = [(255,165,0), (0,0,0)]
	range_mapping = {}
	for i in range(0,150 / length):
		range_mapping[(i*length,i*length+length)] = colors[i % 2]
	output += Helper.instruction_for_ranges(range_mapping)
	colors.reverse()
	for i in range(0,150 / length):
		range_mapping[(i*length,i*length+length)] = colors[i % 2]
	output += Helper.instruction_for_ranges(range_mapping)
	Helper.write_pattern("Spoopy",output)


if __name__ == '__main__':
	print "Generating Spoopy..."
	generate_pattern()