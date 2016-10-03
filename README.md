# BlinkyServer

Version 2.0 of the Python server powering the Trash Kingdom's living room lighting. Version 1.0 is [here](https://github.com/eeevanbbb/BlinkyPython).

===

## Progress

This project is still unfinished. Some patterns are in progress, and some features have yet to be implemented.

## Installation

`pip install -r Requirements.txt`

## Usage

`python Main.py`

## Patterns

The format is subject to change. Currently, it is a series of instructions, one per line, of the form

`[(A,B): (R,G,B); (C,D): (R',G',B')] - X`

where `(A,B)` and `(C,D)` are distinct ranges spanning `(0,150)` in total. There can be between 1-150 ranges, but the given ranges must span the entire light strip and not leave any gaps. `(R,G,B)` and `(R',G',B')` are RGB triplets (where each components ranges from 0-255) that correspond to lights in the ranges `(A,B)` and `(C,D)` respectively. Alternatively, the triplet can be replaced with the string `Color` to use the current user-chosen color. `X` is a number representing the speed for this instruction, or `Speed` to use the user-chosen speed.

Pattern files will be read from the `Patterns` folder. Some patterns should be procedurally generated. These generators should go in the `PatternGenerators` folder, where they will have access to `Helper.py` which contains some functions that may be of help.

Some patterns cannot be expressed by the current instruction format. These are called Dynamic Patterns. To create a dynamic pattern, create a class that responds to the following methods:

- `get_name() # Returns a String`
- `get_frame(color) # Given the current user-chosen color, returns an array of exactly 150 colors (i.e. 3-length arrays)`
- `get_sleep_time(speed) # Given the current user-chosen speed, returns a Float`

Dynamic patterns should manage their own state. When you're ready to add your pattern to the available commands, include it in `DynamicPatternRegistry.py`. Note that, as of now, the above contract is not enforced. Please test your pattern before pushing, or you will cause a crash.

Some patterns are special, and must be handled separately. For instance, the "Random" pattern is generated each time the pattern is selected. See `State.py` and `BlinkyInterface.py` to see how special cases are handled.

## API

### GET

- `/` (HTML)
- `/state` (JSON)
- `/commands` (JSON)

### POST

- `/update` (JSON)
- `/stop`
- `/clear`

The `/update` route supports the following parameters in the JSON body:

- `command` - A string specifying the new pattern to start, `Stop` to freeze the current pattern, or `Clear` to clear the current pattern.
- `color` - A three-length array of RGB values from 0-255.
- `speed` - A floating point value from 0-60.
- `bpm` - An integer value from 0-200.
- `dynamic_color` - A boolean that will tell the system to start or stop dynamically changing the current color.

## Development

This project is still under active development!
