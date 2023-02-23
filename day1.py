from utils import get_lines


def solve_part_a(path):
    return max(get_elves(path))


def solve_part_b(path):
    elves = get_elves(path)
    elves.sort()
    return sum(elves[-3:])


def get_elves(path):
    elves = [0]
    for line in get_lines(path):
        if line == '\n':
            elves.append(0)
        else:
            elves[-1] += int(line.strip())
    return elves

