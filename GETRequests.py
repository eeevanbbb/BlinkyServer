# This file handles serving of GET requests.

from pybars import Compiler
from pybars import strlist
import simplejson

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
		return state_json()
	elif route == "/commands":
		return commands_json()

	return "PAGE NOT FOUND"

def page_not_found(route):
	return "page_not_found"


# Handlebars helpers

# This isn't working yet.........
def _ifEqual(this, options, context):
	if this == context:
		return options['fn'](this)
	else:
		return options['inverse'](this)

def _ifNot(this, options, context):
	if callable(context):
		context = context(this)
	if not context:
		return options['fn'](this)
	else:
		return options['inverse'](this)



def template_for_file(filename):
	with open(filename, 'r') as template_file:
		source = unicode(template_file.read(), "utf-8")
	return compiler.compile(source)

def home_page():
	template = template_for_file('Home.handlebars')
	return template({'commands': State.get_available_commands(),
					 'currentCommand': State.get_command(),
					 'dyna_color': State.get_dyna_color(),
					 'speed': str(State.get_speed()),
					 'red': str(State.get_color()[0]),
					 'green': str(State.get_color()[1]),
					 'blue': str(State.get_color()[2])},
					 helpers={'ifEqual': _ifEqual,
					 		  'ifNot': _ifNot})	

def state_json():
	state = {'command': State.get_command(),
			 'color': State.get_color(),
			 'speed': State.get_speed(),
			 'bpm': State.get_bpm(),
			 'dyna_color': State.get_dyna_color()}
	return simplejson.dumps(state)

def commands_json():
	commands = State.get_available_commands()
	return simplejson.dumps(commands)

