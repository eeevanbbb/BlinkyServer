# This file handles the POST requests for this application.

import State

valid_routes = ["/command"]

def is_valid_route(route):
	return route in valid_routes

def invalid_request(route):
	return "invalid_request"

def process_route_with_data(route, data):
	assert(route in valid_routes)

	if route == "/command":
		success = False
		new_command = data["command"]
		if new_command in State.get_available_commands():
			success = State.set_current_command(new_command)
		return success