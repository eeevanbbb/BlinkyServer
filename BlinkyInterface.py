# This file is the interface with the BlinkyTape API.

import threading
import subprocess
import time

from BlinkyTape import BlinkyTape
import State
import RandomGenerator

blinky_tape = None
if not State.is_debug_machine():
	blinky_tape = BlinkyTape('/dev/ttyACM0', ledCount=150)

def stop():
	State.previous_routine_should_continue = False

def clear():
	State.previous_routine_should_continue = False
	for i in range(0,150):
		if not State.is_debug_machine():
			blinky_tape.sendPixel(0,0,0)
	print "Clearing"
	if not State.is_debug_machine():
		blinky.show()

def random():
	RandomGenerator.new_random_pattern(1000)
	start_command("_Random")


def start_command(command):
	if command == "Stop":
		stop()
	elif command == "Clear":
		clear()
	elif command == "Random":
		random()
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
			if not State.is_debug_machine():
				blinky_tape.sendPixel(range_triple[2][0], range_triple[2][1], range_triple[2][2])
	if not State.is_debug_machine():
		blinky_tape.show()
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
		if comps[1] == "Inverse":
			color = State.get_inverse_color()
		elif comps[1] != "Color":
			rgb_strings = comps[1].replace("(","").replace(")","").split(",")
			color = [int(s) for s in rgb_strings]
		range_triples.append((start,end,color))
	return range_triples

# Returns a float
FLASH_SPEED = 5.0
def parse_speed(speed_string):
	if speed_string == "Speed":
		return State.get_speed()
	elif speed_string == "BPM":
		return State.get_bpm() / 60.0 + FLASH_SPEED
	elif speed_string == "FLASH":
		return FLASH_SPEED
	else:
		return float(speed_string)