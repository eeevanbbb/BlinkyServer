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
available_commands.remove(".DS_Store")

# Getters

def get_available_commands():
	return available_commands

def get_command():
 	return command

def get_color():
 	return color

def get_speed():
	return speed

def get_bpm():
	return bpm

def get_dyna_color():
	return dyna_color


# Setters

def set_current_command(new_command):
	assert(new_command in available_commands)
	
	BlinkyInterface.start_command(new_command)
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