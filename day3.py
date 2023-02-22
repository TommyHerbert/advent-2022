import utils


def solve_part_a(path):
    # return sum([get_priority(l) for l in utils.get_lines(path)])
    return 0 # TODO


def get_priority(line):
    halfway = len(line.trim())/2
    first_half = Set([c for c in line[:halfway]])
    for c in line[halfway:]:
        if c in first_half:
            return value(c)
    return 0


def value(character):
    if character.islower():
        # TODO what constants do I need here?
        return ord(character) - 40
    else:
        return ord(character) + 20

