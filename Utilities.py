# This file contains utilities used by modules in the application.

import time

def log_debug(s):
	print "[%s] %s" % (time.asctime(), s)