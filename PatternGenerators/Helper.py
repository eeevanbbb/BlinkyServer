# This file contains some helper methods for the generators.

def write_pattern(name, text):
	with open("../Patterns/%s.txt" % name, "w") as pattern_file:
		pattern_file.write(text)

def sort_ranges(ranges):
	return sorted(ranges, key=lambda x: x[0])

# Takes as input a mapping of tuple ranges to colors
def instruction_for_ranges(range_mappings, speed="Speed"):
	current = 0
	sorted_ranges = sort_ranges(range_mappings.keys())
	full_ranges = []
	for current_range in sorted_ranges:
		if current_range[0] > current:
			full_ranges.append((current,current_range[0]))
		full_ranges.append(current_range)
		current = current_range[1]
	if current < 150:
		full_ranges.append((current, 150))
	output = "["
	for i, current_range in enumerate(full_ranges):
		current_color = "(0,0,0)"
		if current_range in range_mappings:
			current_color = range_mappings[current_range]
		output += "(%s,%s): %s" % (str(current_range[0]), str(current_range[1]), current_color)
		if i != len(full_ranges) - 1:
			output += "; "
	output += "] - %s\n" % speed
	return output


def instruction_for_pixel(position, color="Color", speed="Speed"):
	return instruction_for_ranges({(position,position+1): color}, speed)

def color_string_for_color(color):
	return "(%s,%s,%s)" % (str(color[0]),str(color[1]),str(color[2]))

def instruction_for_pixels(positions, colors=[], speed="Speed"):
	if len(colors) == 0:
		colors = ["Color" for i in range(0,len(positions))]
	range_mappings = {}
	for i in range(0,positions):
		position = positions[i]
		range_mappings[range(position,position+1)] = colors[i]
	return instruction_for_ranges(range_mappings, speed)
