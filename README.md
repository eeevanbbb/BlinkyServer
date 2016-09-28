# BlinkyServer

Version 2.0 of the Python server powering the Trash Kingdom's living room lighting. Version 1.0 is [here](https://github.com/eeevanbbb/BlinkyPython).

===

## Progress

This project is still unfinished. The basic components have been written, but extra features like speed, color, and most of the commands have not been written yet.

## Installation

`pip install -r Requirements.txt`

## Usage

`python Main.py`

## Patterns

Pattern files coming soon. Although the format is still subject to change, it will likely be a series of instructions, one per line, of the form

`[(A,B): (R,G,B); (C,D): (R',G',B')] - X`

where `(A,B)` and `(C,D)` are distinct ranges spanning `(0,150)` in total. There can be between 1-150 ranges, but the given ranges must span the entire light strip and not leave any gaps. `(R,G,B)` and `(R',G',B')` are RGB triplets (where each components ranges from 0-255) that correspond to lights in the ranges `(A,B)` and `(C,D)` respectively. Alternatively, the triplet can be replaced with the string `Color` to use the current user-chosen color. `X` is a number representing the speed for this instruction, or `Speed` to use the user-chosen speed.

For more complex patterns that involve moving blocks of lights, these files should be procedurally generated. It may be worthwhile to create a tool to do so. It may also not be.

## API

Not all routes from version 1.0 are supported yet. Routes have been split up into GET routes, which request information (either HTML or JSON), or POST routes, which send information via a JSON object. API docs would be a good idea, and they are forthcoming.

