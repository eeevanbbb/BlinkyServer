# This file keeps the current state of the lights.

import BlinkyInterface

color = [0,0,255]
speed = 1.0
dyna_color = False
bpm = 120
command = "None"

previous_routine_should_continue = True

available_commands = ["Clear","Stop","RoundAndRound","Flash","Snake","OutsideIn","Random","Solid","Rainbow","DCStart","DCStop","OutsideInRemix","Beauty","FourOnTheFloor","AlternatePush","DownbeatPeaks","Dart","Swarm","BrightDark","Christmas1","Christmas2","Christmas3","ChristmasDance","Christmas4","FadeRed","FadeGreen","FadeBlue"]


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