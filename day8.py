from utils import get_lines


def solve_part_a(data):
    trees = as_ints(get_lines(data))
    visibility_map = initialise_visibility(trees)
    for row in range(len(trees)):

        # west to east
        highest = -1
        for column in range(len(trees[row])):
            height = trees[row][column]
            if height > highest:
                visibility_map[row][column] = 1
                highest = height
        
        # east to west
        highest = -1
        for column in range(len(trees[row]) - 1, -1, -1):
            height = trees[row][column]
            if height > highest:
                visibility_map[row][column] = 1
                highest = height
    
    for column in range(len(trees[0])):

        # north to south
        highest = -1
        for row in range(len(trees)):
            height = trees[row][column]
            if height > highest:
                visibility_map[row][column] = 1
                highest = height
        
        # south to north
        highest = -1
        for row in range(len(trees) - 1, -1, -1):
            height = trees[row][column]
            if height > highest:
                visibility_map[row][column] = 1
                highest = height

    return sum([sum(row) for row in visibility_map])


def as_ints(strings):
    return [[int(c) for c in s if c in '1234567890'] for s in strings]


def initialise_visibility(trees):
    visibility_map = []
    for row in range(len(trees)):
        visibility_map.append([0] * len(trees[row]))
    return visibility_map


def solve_part_b(data):
    return 0 # TODO

