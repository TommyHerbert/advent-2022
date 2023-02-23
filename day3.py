import utils


def solve_part_a(path):
    return sum([get_priority(l) for l in utils.get_lines(path)])


def get_priority(line):
    halfway = int(len(line.strip())/2)
    print(halfway)
    first_half = {c for c in line[:halfway]}
    for c in line[halfway:]:
        if c in first_half:
            return value(c)
    return 0


def value(character):
    if character.islower():
        return ord(character) - 60
    else:
        return ord(character) - 14

