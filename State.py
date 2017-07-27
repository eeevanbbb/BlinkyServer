# This file keeps the current state of the lights.

import os

import DynamicPatternRegistry

color = [0,0,255]
speed = 1.0
dyna_color = False
bpm = 120
command = "None"
pattern_parameters = {} # String: String

running_loop = ""
blinky_lock = False

available_commands = map((lambda x: x.replace(".txt","")), os.listdir(os.path.join(os.path.dirname(__file__), 'Patterns')))
for command in available_commands:
	if command[0] == "_":
		available_commands.remove(command)

# There's probably a better way to do this, but this works on MacOS
DEBUG_MACHINE = False
if ".DS_Store" in available_commands:
	available_commands.remove(".DS_Store")
	DEBUG_MACHINE = True

def is_debug_machine():
	return DEBUG_MACHINE

special_commands = ["Random"]

# Getters

def get_available_commands():
	return sorted(available_commands + special_commands + get_dynamic_commands())

def get_command():
 	return command

def get_color():
 	return color

def get_inverse_color():
	return [255-color[0], 255-color[1], 255-color[2]]

def get_speed():
	return speed

def get_bpm():
	return bpm

def get_dyna_color():
	return dyna_color

def get_special_commands():
	return special_commands

def get_dynamic_commands():
	return DynamicPatternRegistry.get_dynamic_pattern_names()

def is_dynamic_command(command):
	return command in get_dynamic_commands()

def class_for_dynamic_command(command):
	return DynamicPatternRegistry.dynamic_pattern_class_for_name(command)

def get_pattern_parameters():
	return pattern_parameters


# Setters

def set_current_command(new_command):	
	global command
	command = new_command
	return True

def set_color(new_color):
	global color
	color = new_color
	return True

def set_speed(new_speed):
	global speed
	speed = new_speed
	return True

def set_bpm(new_bpm):
	global bpm
	bpm = new_bpm
	return True

def set_dyna_color(new_dyna_color):
	global dyna_color
	dyna_color = new_dyna_color
	return True

def set_pattern_parameters(new_pattern_parameters):
	global pattern_parameters
	pattern_parameters = new_pattern_parameters
	return True