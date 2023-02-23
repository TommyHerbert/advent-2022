from utils import get_lines
from functools import reduce


def solve_part_a(path):
    return sum([get_priority(l) for l in get_lines(path)])


def solve_part_b(path):
    groups = divide(get_lines(path))
    return sum([get_badge_priority(group) for group in groups])


def get_priority(line):
    halfway = int(len(line.strip())/2)
    first_half = {c for c in line[:halfway]}
    for c in line[halfway:]:
        if c in first_half:
            return value(c)
    return 0


def value(character):
    if character.islower():
        return ord(character) - 96
    else:
        return ord(character) - 38


def get_badge_priority(group):
    sets = [{character for character in line.strip()} for line in group]
    matches = reduce(lambda s1, s2: s1.intersection(s2), sets)
    return value(list(matches)[0])


def divide(data):
    threes = []
    for i in range(len(data)):
        if i%3 == 0:
            threes.append([data[i]])
        else:
            threes[-1].append(data[i])
    return threes

