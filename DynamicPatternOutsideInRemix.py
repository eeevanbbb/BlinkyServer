# This file is a dynamic pattern. Use this as an example for creating dynamic patterns.
# Dynamic patterns must implement get_frame(color), which takes as input the current color and should return an array of exactly 150 colors,
# as well as get_sleep_time(speed), which takes the current speed and should return a Float, 
# and get_name(), which should return a String.
# Dynamic patterns should manage their own state.

class OutsideInRemix(object):

	def __init__(self):
		self.name = "OutsideInRemix"
		self.i = 0
		self.color = [0,0,0]

	def color_pixel_for_offset(self, offset):
		return [int(round(self.color[i] - (3.4 * offset))) for i in range(0,3)]

	def get_name(self):
		return self.name

	def get_frame(self, color):
		self.color = color
		colors = []
		if self.i < 75:
			for x in range(0, self.i + 1):
				colors.append(self.color_pixel_for_offset(self.i - x))
			for x in range(self.i + 1,149 - self.i):
				colors.append([0,0,0])
			for x in range(149 - self.i, 150):
				colors.append(self.color_pixel_for_offset(x - (149 - self.i)))
		else:
			for x in range(0, self.i - 75 + 1):
				colors.append([0,0,0])
			for x in range(self.i - 75 + 1, 75):
				colors.append(self.color_pixel_for_offset(74 - (x - (self.i - 75 + 1))))
			for x in range(75, 149 - (self.i - 75)):
				colors.append(self.color_pixel_for_offset(74 - ((149 - (self.i - 75)) - 1 - x)))
			for x in range(149 - (self.i - 75), 150):
				colors.append([0,0,0])
		self.i = (self.i + 1) % 150
		return colors

	def get_sleep_time(self, speed):
		return 1.0 / speed