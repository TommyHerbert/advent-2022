from utils import get_lines

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
    return add_scores(path, scores_a)


def solve_part_b(path):
    return add_scores(path, scores_b)


def add_scores(path, score_table):
    return sum([score_table[line] for line in get_lines(path)])

