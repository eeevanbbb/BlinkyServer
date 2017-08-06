# This is the main entry point for the application.

import argparse

from Server import BlinkyServer
from BlinkyInterface import BlinkyInterface
import State

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start the BlinkyServer.')
    parser.add_argument('--debug', dest='debug', action='store_const', const=True, default=False, help='Do not look for blinky hardware.')
    args = parser.parse_args()

    State.DEBUG_MODE = args.debug

    if State.is_debug_machine():
        print("STARTING IN DEBUG MODE")

    blinky_interface = BlinkyInterface()
    blinky_server = BlinkyServer()

    blinky_server.start_server(blinky_interface)