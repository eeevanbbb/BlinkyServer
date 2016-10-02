# This file handles the POST requests for this application.

import State
import BlinkyInterface

valid_routes = ["/update","/stop","/clear"]

MAX_SPEED = 60
MAX_BPM = 600

def is_valid_route(route):
	return route in valid_routes

def invalid_request(route):
	return "invalid_request"

def process_route_with_data(route, data):
	assert(route in valid_routes)

	success = True
	if route == "/update":
		if "command" in data:
			new_command = data["command"]
			if validate_command(new_command):
				success = State.set_current_command(new_command) and success 
				BlinkyInterface.start_command(new_command)
		if "color" in data:
			new_color = data["color"]
			print new_color
			if validate_color(new_color):
				success = State.set_color(new_color) and success
		if "speed" in data:
			new_speed = data["speed"]
			if validate_speed(new_speed):
				success = State.set_speed(new_speed) and success
		if "bpm" in data:
			new_bpm = data["bpm"]
			if validate_bpm(new_bpm):
				success = State.set_bpm(new_bpm) and success
		if "dynamic_color" in data:
			new_dyna_color = data["dynamic_color"]
			if validate_dynamic_color(new_dyna_color):
				success = State.set_dyna_color(new_dyna_color) and success
				BlinkyInterface.start_dynamic_color(new_dyna_color)
	elif route == "/stop":
		BlinkyInterface.start_command("Stop")
		success = True
	elif route == "/clear":
		BlinkyInterface.start_command("Clear")
		success = State.set_current_command("None") and success
	else:
		success = False

	return success

def validate_command(command):
	return command in State.special_commands or command in State.get_available_commands()

def validate_color(color):
	if len(color) != 3:
		return False
	for i in range(0,3):
		if color[i] < 0 or color[i] > 255:
			return False
	return True

def validate_speed(speed):
	return speed >= 0 and speed <= MAX_SPEED

def validate_bpm(bpm):
	return bpm >= 0 and bpm <= MAX_BPM

def validate_dynamic_color(dyna_color):
	return type(dyna_color) == type(True)