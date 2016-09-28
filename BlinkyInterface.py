# This file is the interface with the BlinkyTape API.

import threading
import subprocess
import time

from BlinkyTape import BlinkyTape
import State

# blinky_tape = BlinkyTape('/dev/ttyACM0', ledCount=150)

def stop():
	State.previous_routine_should_continue = False
	print "Stopping"

def start_command(command):
	if command == "Stop":
		stop()
	else:
		with open("Patterns/%s.txt" % command, 'r') as instruction_file:
			instructions = instruction_file.readlines()
		start_with_instructions(instructions)

def start_with_instructions(instructions):
	previous_routine_should_continue = False
	thread = threading.Thread(target=blinky_loop, args=(instructions, ))
	thread.daemon = True
	thread.start()

def blinky_loop(instructions):
	State.previous_routine_should_continue = True

	for instruction in instructions:
		execute_instruction(instruction)
		if not State.previous_routine_should_continue:
			return

	blinky_loop(instructions)

def execute_instruction(instruction):
	fields = parse_fields(instruction)
	ranges = parse_ranges(fields[0])
	speed = parse_speed(fields[1])
	for range_triple in ranges:
		for i in range(range_triple[0], range_triple[1]):
			# blinky_tape.sendPixel(range_triple[2][0], range_triple[2][1], range_triple[2][2])
			pass
		print "Sending (%s,%s,%s)" % (str(range_triple[2][0]), str(range_triple[2][1]), str(range_triple[2][2]))
	time.sleep(1.0 / speed)



# Returns an array of whitespace-stripped strings
def parse_fields(instruction):
	fields = instruction.replace(" ","").replace("\n","").split("-")
	return fields

# Returns an array of triples of the form (start, end, [R,G,B])
def parse_ranges(ranges):
	range_triples = []
	range_mappings = ranges.replace("[","").replace("]","").split(";")
	for range_mapping in range_mappings:
		comps = range_mapping.split(":")
		boundaries = comps[0].replace("(","").replace(")","").split(",")
		start = int(boundaries[0])
		end = int(boundaries[1])
		color = State.get_color()
		if comps[1] != "Color":
			rgb_strings = comps[1].replace("(","").replace(")","").split(",")
			color = [int(s) for s in rgb_strings]
		range_triples.append((start,end,color))
	return range_triples

# Returns a float
def parse_speed(speed_string):
	if speed_string == "Speed":
		return State.get_speed()
	else:
		return float(speed_string)