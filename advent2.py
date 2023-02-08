import utils

scores_a = {
    'A X\n': 4, 'A Y\n': 8, 'A Z\n': 3,
    'B X\n': 1, 'B Y\n': 5, 'B Z\n': 9,
    'C X\n': 7, 'C Y\n': 2, 'C Z\n': 6
}

scores_b = {
    'A X\n': 3, 'A Y\n': 4, 'A Z\n': 8,
    'B X\n': 1, 'B Y\n': 5, 'B Z\n': 9,
    'C X\n': 2, 'C Y\n': 6, 'C Z\n': 7
}


def solve_part_a(path):
    return sum([scores_a[line] for line in utils.get_lines(path)])


def solve_part_b(path):
    return sum([scores_b[line] for line in utils.get_lines(path)])

