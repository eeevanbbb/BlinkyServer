on# This file generates the BinarySearch pattern and puts it in the ../Patterns folder.

import math

import Helper

# 100, 0  --> 50
# 100, 1  --> 25, 50, 75
# 100, 2  --> 12, 25, 37, 50, 62, 75, 87

def binary_search_points(length, depth):
    return binary_search_aux(floor(length / 2), floor(length / 4),

def binary_search_aux(pivot, amount, min_amount):
    if amount <= min_amount:
        return []
    points = [pivot + amount, pivot - amount]
    return points + binary_search_aux(pivout + amount, floor(amount / 2)) + binary_search_aux(pivot - amount, floor(amount / 2))


def generate_pattern():
    """
	output = ""
	on_lights = []
    frequency = 75
    for i in range(0,math.ceil(math.log(150,2))):

        output += Helper.instruction_for_pixels(on_lights)
	Helper.write_pattern("BinarySearch",output)
    """
    print "Binary search was not generated"


if __name__ == '__main__':
	print "Generating BinarySearch..."
	generate_pattern()
