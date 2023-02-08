import utils

scores = {
    'A X\n': 4, 'A Y\n': 1, 'A Z\n': 7,
    'B X\n': 8, 'B Y\n': 5, 'B Z\n': 2,
    'C X\n': 3, 'C Y\n': 9, 'C Z\n': 6
}


def solve_part_a(path):
    score = 0
    for line in utils.get_lines(path):
        score += scores[line]
    return score

