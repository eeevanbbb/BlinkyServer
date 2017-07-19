#! /bin/sh

# Start the blinky server
BASEDIR=$(dirname "$0")
echo "Starting the BlinkyServer from ${BASEDIR}"
python -u $BASEDIR/Main.py
