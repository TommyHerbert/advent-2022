import utils

scores = {
    'A X\n': 4, 'A Y\n': 8, 'A Z\n': 3,
    'B X\n': 1, 'B Y\n': 5, 'B Z\n': 9,
    'C X\n': 7, 'C Y\n': 2, 'C Z\n': 6
}


def solve_part_a(path):
    return sum([scores[line] for line in utils.get_lines(path)])

