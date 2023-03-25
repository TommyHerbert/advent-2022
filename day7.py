from utils import get_lines


def solve_part_a(input_file, cutoff):
    moves = get_moves(input_file)
    state = {'path':[], 'sizes':{}}
    for move in moves:
        update(state, move)
    return sum([s for s in state['sizes'].values() if s <= cutoff])


class Tree:
    def __init__(self):
        self.children = []
        self.parent = None
        self.size = 0

    def __iter__(self):
        self.iterator = self.generate()
        return self
    
    def __next__(self):
        return next(self.iterator)

    def generate(self):
        yield self
        for child in self.children:
            yield child


def get_moves(input_file):
    moves = []
    for line in get_lines(input_file):
        line = line.strip()
        if line[0] == '$':
            moves.append((line.split()[1:], []))
        else:
            moves[-1][1].append(line)
    return moves


def update(state, move):
    command, output = move
    if command[0] == 'cd':
        state['path'] = change_directory(state['path'], command[1])
    else:
        update_sizes(output, state)


def change_directory(path, directory):
    if directory == '/':
        return []
    if directory == '..':
        return path[:-1]
    return path + [directory]


def update_sizes(output, state):
    for line in output:
        tokens = line.split()
        name = tokens[1]
        if tokens[0] == 'dir':
            if name not in state['sizes']:
                state['sizes'][name] = 0
        else:
            size = int(tokens[0])
            for directory in state['path']:
                state['sizes'][directory] += size


def solve_part_b(data):
    return 0 # TODO

