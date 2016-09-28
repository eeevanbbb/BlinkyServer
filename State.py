# This file keeps the current state of the lights.

import BlinkyInterface
from os import listdir

color = [0,0,255]
speed = 1.0
dyna_color = False
bpm = 120
command = "None"

previous_routine_should_continue = True

available_commands = map((lambda x: x.replace(".txt","")), listdir("Patterns"))

# Getters

def get_available_commands():
	return available_commands

def get_command():
 	return command

def get_color_string():
 	return "(" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + ")"

def get_speed_string():
	return str(speed)

def get_bpm_string():
	return str(bpm)

def get_dyna_color_string():
	return str(dyna_color)

def get_color():
	return color

def get_speed():
	return speed


# Setters

def set_current_command(new_command):
	assert(new_command in available_commands)
	
	BlinkyInterface.start_command(new_command)
	command = new_command
	return True