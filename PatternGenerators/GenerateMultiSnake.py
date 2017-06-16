# This file generates the MultiSnake pattern and puts it in the ../Patterns folder.

import Helper

def generate_pattern():
    length = 10
    count = 5
    output = ""
    for i in range(0,150):
        ranges = []
        spacing = (150 - (length * count)) / count
        for j in range(0, count):
            start = i + (j * (spacing + length))
            end = start + length
            if start >= 150:
                start -= 150
                end -= 150
            if end > 150:
                ranges.append((start, 150))
                ranges.append((0, end - 150))
            else:
                ranges.append((start, end))
        range_mapping = {}
        for aRange in ranges:
            range_mapping[aRange] = "Color"
        output += Helper.instruction_for_ranges(range_mapping)
    Helper.write_pattern("MultiSnake", output)


if __name__ == '__main__':
    print "Generating MultiSnake..."
    generate_pattern()