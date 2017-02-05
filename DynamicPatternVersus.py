# This file is a dynamic pattern. Use this as an example for creating dynamic patterns.
# Dynamic patterns must implement get_frame(color), which takes as input the current color and should return an array of exactly 150 colors,
# as well as get_sleep_time(speed), which takes the current speed and should return a Float, 
# and get_name(), which should return a String.
# Dynamic patterns should manage their own state.

import State

class Versus():
	def __init__(self):
		self.name = "Versus"

	def get_name(self):
		return self.name

	def get_frame(self, color):
		colors = []
		params = State.get_pattern_parameters()
		team1end = 0
		team2begin = 150
		color1 = [255,0,0]
		color2 = [0,0,255]
		# if "Team1Color" in params:
		# 	color1 = params["Team1Color"]
		# if "Team2Color" in params:
		# 	color2 = params["Team2Color"]
		if "Team1" in params:
			team1end = int(params["Team1"])
		if "Team2" in params:
			team2begin = 150 - int(params["Team2"])
		if team1end > 150:
			team1end = 150
		if team2begin > 150:
			team2begin = 150
		if team1end > team2begin:
			team2begin = team1end
		for i in range(0,blue_end):
			colors.append(color1)
		for i in range(team1end, team2begin):
			colors.append([0,0,0])
		for i in range(team2begin, 150):
			colors.append(color2)
		return colors


	def get_sleep_time(self, speed):
		return 1.0 / speed