# This file is responsible for DynamicColor.

import State
from random import randint
import time

def start_dynamic_color():
	color = State.get_color()
	while True:
		if State.get_dyna_color():
			new_color = [randint(0,255) for i in range(0,3)]

			transition_time = 3.0
			numberOfSteps = State.get_speed() * transition_time

			color_delta = [(new_color[i] - color[i]) / numberOfSteps for i in range(0,3)]

			while transition_time > 0:
				if State.get_dyna_color():
					transition_time -= 1.0 / State.get_speed()

					color = [int(color[i] + color_delta[i]) for i in range(0,3)]
					State.set_color(color)

					time.sleep(1.0 / State.get_speed())
				else:
					return
		else:
			return