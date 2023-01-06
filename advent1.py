def solve(filename):
    elves = [0]
    with open(filename) as input:
        for line in input.readlines():
            if line == '\n':
                elves.append(0)
            else:
                elves[-1] += int(line.strip())
    return max(elves)

