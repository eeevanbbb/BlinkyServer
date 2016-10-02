# This file generates the Beauty pattern and puts it in the ../Patterns folder.

import math

import Helper

BEAUTY_STEP = 50
BEAUTY_GRANULARITY = 50.0

def generate_pattern():
	output = ""
	for offset in range(0,1000):
		range_mappings = {} #something weird here...
		for i in range(0,150):
			color = [int(((math.sin((n + (BEAUTY_STEP * n) + offset) / BEAUTY_GRANULARITY) + 1) / 2) * 255) for n in range(0,3)]
			range_mappings[(i,i+1)] = Helper.color_string_for_color(color)
		output += Helper.instruction_for_ranges(range_mappings)
	Helper.write_pattern("Beauty",output)


if __name__ == '__main__':
	print "Generating Beauty..."
	generate_pattern()