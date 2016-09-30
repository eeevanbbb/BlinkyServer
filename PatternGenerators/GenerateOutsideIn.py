# This file generates the OutsideIn pattern and puts it in the ../Patterns folder.

import Helper

def generate_pattern():
	output = ""
	ranges = []
	for i in range(0,150):
		if i < 75:
			ranges = [(0,i),(150-i,150)]
		else:
			ranges = [(i-75,150-(i-75))]
		range_mappings = {}
		for aRange in ranges:
			range_mappings[aRange] = "Color"
		output += Helper.instruction_for_ranges(range_mappings)
	Helper.write_pattern("OutsideIn",output)


if __name__ == '__main__':
	print "Generating OutsideIn..."
	generate_pattern()