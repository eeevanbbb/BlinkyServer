# This file contains utilities used by modules in the application.

import time

def log_debug(s):
	print "[%s] %s" % (time.asctime(), s)

def color_from_string(color_string):
	return eval(color_string)

def simple_debug_view(ranges):
    output_str = ""
    for range_triple in ranges:
        for i in range(range_triple[0], range_triple[1]):
            if range_triple[2][0] == 0 and range_triple[2][1] == 0 and range_triple[2][2] == 0:
                output_str += "."
            else:
                output_str += "!"
    return output_str