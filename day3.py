import utils


def solve_part_a(path):
    return sum([get_priority(l) for l in utils.get_lines(path)])


def solve_part_b(path):
    return 0 # TODO


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

