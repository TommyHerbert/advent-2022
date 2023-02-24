from utils import get_lines


def solve_part_a(path):
    return len([line for line in get_lines(path) if fully_overlapping(line)])


def solve_part_b(path):
    return 0 # TODO


def fully_overlapping(line):
    ranges = parse(line)
    if ranges[0][0] == ranges[1][0]:
        return True
    if ranges[0][0] < ranges[1][0]:
        return ranges[0][1] >= ranges[1][1]
    return ranges[1][1] >= ranges[0][1]


def parse(line):
    range_strings = line.strip().split(',')
    ranges = []
    for range_string in range_strings:
        ranges.append(tuple([int(c) for c in range_string.split('-')]))
    return tuple(ranges)

