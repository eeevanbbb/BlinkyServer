# This file handles serving of GET requests.

from pybars import Compiler

import State

valid_routes = ["/", "/state", "/commands"]
json_routes  = ["/state", "/commands"]

compiler = Compiler()

# def _json_list()

def is_valid_route(route):
	return route in valid_routes

def is_json_route(route):
	return route in json_routes

def page_for_route(route):
	assert(is_valid_route(route))

	if route == "/":
		return home_page()
	elif route == "/state":
		return state_page()
	elif route == "/commands":
		return commands_page()

	return "PAGE NOT FOUND"

def page_not_found(route):
	return "page_not_found"


def template_for_file(filename):
	with open(filename, 'r') as template_file:
		source = unicode(template_file.read(), "utf-8")
	return compiler.compile(source)

def home_page():
	return "Welcome!"

def state_page():
	template = template_for_file('state.handlebars')
	return template({'command': State.get_command(),
					 'color': State.get_color_string(),
					 'speed': State.get_speed_string(),
					 'bpm': State.get_bpm_string(),
					 'dyna_color': State.get_dyna_color_string()})

def commands_page():
	template = template_for_file('commands.handlebars')
	return template({'commands': [{"text": command} for command in State.get_available_commands()]})

