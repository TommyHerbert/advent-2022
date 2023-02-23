from utils import get_lines


def solve_part_a(path):
    return len([line for line in get_lines(path) if fully_overlapping(line)])


def fully_overlapping(line):
    ranges = parse(line)
    range1, range2 = sort_ranges(ranges)
    return range1[1] >= range2[1]


def parse(line):
    range_strings = line.strip().split(',')
    ranges = []
    for range_string in range_strings:
        ranges.append(tuple([int(c) for c in range_string.split('-')]))
    return tuple(ranges)


def sort_ranges(ranges):
    range1, range2 = ranges
    if range1[0] < range2[0]:
        return range1, range2
    if range1[0] > range2[0]:
        return range2, range1
    return (range1, range2) if range1[1] > range2[1] else (range2, range1)

