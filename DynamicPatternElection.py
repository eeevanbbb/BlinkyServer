# This file is a dynamic pattern. Use this as an example for creating dynamic patterns.
# Dynamic patterns must implement get_frame(color), which takes as input the current color and should return an array of exactly 150 colors,
# as well as get_sleep_time(speed), which takes the current speed and should return a Float, 
# and get_name(), which should return a String.
# Dynamic patterns should manage their own state.

import State

class Election(object):
	def __init__(self):
		self.name = "Election"

	def get_name(self):
		return self.name

	def get_frame(self, color):
		colors = []
		params = State.get_pattern_parameters()
		blue_end = 0
		red_begin = 150
		blue_end = params["Blue"]
		red_begin = 150 - params["Red"]
		for i in range(0,blue_end):
			colors.append([0,0,255])
		for i in range(blue_end, red_begin):
			colors.append([0,0,0])
		for i in range(red_begin, 150):
			colors.append([255,0,0])
		return colors


	def get_sleep_time(self, speed):
		return 1.0 / speed