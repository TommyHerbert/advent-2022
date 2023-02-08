def solve_part_a(filename):
    return max(get_elves(filename))


def solve_part_b(filename):
    elves = get_elves(filename)
    elves.sort()
    return sum(elves[-3:])


def get_elves(filename):
    elves = [0]
    with open(filename) as input:
        for line in input.readlines():
            if line == '\n':
                elves.append(0)
            else:
                elves[-1] += int(line.strip())
    return elves

