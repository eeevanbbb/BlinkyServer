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

Pattern files coming soon. Although the format is still subject to change, it will likely be a series of instructions, one per line, of the form

`[(A,B): (R,G,B); (C,D): (R',G',B')] - X`

where `(A,B)` and `(C,D)` are distinct ranges spanning `(0,150)` in total. There can be between 1-150 ranges, but the given ranges must span the entire light strip and not leave any gaps. `(R,G,B)` and `(R',G',B')` are RGB triplets (where each components ranges from 0-255) that correspond to lights in the ranges `(A,B)` and `(C,D)` respectively. Alternatively, the triplet can be replaced with the string `Color` to use the current user-chosen color. `X` is a number representing the speed for this instruction, or `Speed` to use the user-chosen speed.

Pattern files will be read from the `Patterns` folder. Some patterns should be procedurally generated. These generators should go in the `PatternGenerators` folder, where they will have access to `Helper.py` which contains some functions that may be of help.

## API

### GET

- / (HTML)
- /state (JSON)
- /commands (JSON)

### POST

- /update

The `/update` route supports the following properties:

- `command` - A string specifying the new pattern to start, `Stop` to freeze the current pattern, or `Clear` to clear the current pattern.
- `color` - A three-length array of RGB values from 0-255.
- `speed` - A floating point value from 0-60.
- `bpm` - An integer value from 0-200.
- `dynamic_color` - A boolean that will tell the system to start or stop dynamically changing the current color.
