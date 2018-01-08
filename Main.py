# This is the main entry point for the application.

import signal
import sys

import argparse

from Server import BlinkyServer
from BlinkyInterface import BlinkyInterface
from Utilities import log_debug
import State
from PubNubServer import PubNubServer

pub_nub_server = None

# https://stackoverflow.com/questions/41398322/cant-quit-a-running-python-script
def sig_handler(signal, frame):
    # Should make it so CTRL^C stops the program
    # But it doesn't work
    global pub_nub_server
    pub_nub_server.stop_listening()
    sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start the BlinkyServer.')
    parser.add_argument('--debug', dest='debug', action='store_const', const=True, default=False, help='Do not look for blinky hardware.')
    args = parser.parse_args()

    State.DEBUG_MODE = args.debug

    if State.is_debug_machine():
        log_debug("STARTING IN DEBUG MODE")

    blinky_interface = BlinkyInterface()

    global pub_nub_server
    pub_nub_server = PubNubServer(blinky_interface)
    pub_nub_server.listen()

    blinky_server = BlinkyServer()
    blinky_server.start_server(blinky_interface)