# This file handles the POST requests for this application.

import State

valid_routes = ["/update","/stop","/clear"]

MIN_SPEED = 0
MAX_SPEED = 60

MIN_BPM = 0
MAX_BPM = 600

def is_valid_route(route):
	return route in valid_routes

def invalid_request(route):
	return "invalid_request"

def process_route_with_data(route, data, blinky_interface):
	assert(route in valid_routes)

	success = True
	if route == "/update":
		if "command" in data:
			new_command = data["command"]
			if validate_command(new_command):
				success = State.set_current_command(new_command) and success 
				blinky_interface.start_command(new_command)
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
				blinky_interface.start_dynamic_color(new_dyna_color)
		if "is_reverse" in data:
			new_is_reverse = data["is_reverse"]
			if validate_is_reverse(new_is_reverse):
				old_is_reverse = State.get_is_reverse()
				success = State.set_is_reverse(new_is_reverse) and success
				if old_is_reverse != new_is_reverse:
					blinky_interface.restart_command()
		if "pattern_parameters" in data:
			new_pattern_parameters = data["pattern_parameters"]
			if validate_pattern_parameters(new_pattern_parameters):
				success = State.set_pattern_parameters(new_pattern_parameters) and success
	elif route == "/stop":
		blinky_interface.start_command("Stop")
		success = True
	elif route == "/clear":
		blinky_interface.start_command("Clear")
		success = State.set_current_command("None") and success
	else:
		success = False

	return success

def validate_command(command):
	return command in State.get_special_commands() or command in State.get_available_commands() or command in State.get_dynamic_commands()

def validate_color(color):
	if len(color) != 3:
		return False
	for i in range(0,3):
		if color[i] < 0 or color[i] > 255:
			return False
	return True

def validate_speed(speed):
	return speed >= MIN_SPEED and speed <= MAX_SPEED

def validate_bpm(bpm):
	return bpm >= MIN_BPM and bpm <= MAX_BPM

def validate_dynamic_color(dyna_color):
	return type(dyna_color) == type(True)

def validate_is_reverse(is_reverse):
	return type(is_reverse) == type(True)

def validate_pattern_parameters(pattern_parameters):
	return isinstance(pattern_parameters, dict)