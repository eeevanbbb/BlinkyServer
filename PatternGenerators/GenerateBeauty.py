# This file generates the Beauty pattern and puts it in the ../Patterns folder.

# 1, 315, 629, 943... are all similar. Perhaps repeat every 314?

import math

import Helper

BEAUTY_STEP = 50
BEAUTY_GRANULARITY = 50.0

def generate_pattern():
	output = ""
	# for offset in range(0,60*60*5):
	for offset in range(0,314):
		range_mappings = {}
		for i in range(0,150):
			color = [int(((math.sin((i + (BEAUTY_STEP * n) + offset) / BEAUTY_GRANULARITY) + 1) / 2) * 255) for n in range(0,3)]
			range_mappings[(i,i+1)] = Helper.color_string_for_color(color)
		output += Helper.instruction_for_ranges(range_mappings)
	Helper.write_pattern("Beauty",output)


if __name__ == '__main__':
	print "Generating Beauty..."
	generate_pattern()