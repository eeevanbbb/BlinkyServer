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

special_commands = ["Stop", "Clear", "Random"]

# Getters

def get_available_commands():
	return available_commands

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


# Setters

def set_current_command(new_command):	
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

def set_dyna_color(new_dyna_color):
	global dyna_color
	dyna_color = new_dyna_color
	return True