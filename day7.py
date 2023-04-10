from utils import get_lines


def solve_part_a_tree(input_file, cutoff):
    moves = get_moves(input_file)
    tree = Tree('/')
    for move in moves:
        tree = update_tree(tree, move)
    return sum([node.size for node in tree.get_root() if node.size <= cutoff])


def solve_part_b(data):
    return 0 # TODO


class Tree:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.parent = None
        self.children = []

    def __iter__(self):
        self.iterator = self.generate()
        return self
    
    def __next__(self):
        return next(self.iterator)

    def generate(self):
        yield self
        for child in self.children:
            yield child

    def get_root(self):
        if self.parent is None:
            return self
        return self.parent.get_root()

    def add_child(self, name):
        child = Tree(name)
        child.parent = self
        self.children.append(child)

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def update_sizes(self, output):
        local_total = 0
        for line in output:
            tokens = line.split()
            name = tokens[1]
            if tokens[0] == 'dir':
                child = self.find_child(name)
                if child is None:
                    self.add_child(name)
            else:
                local_total += int(tokens[0])
        self.increase(local_total)

    def increase(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.increase(size)


def get_moves(input_file):
    moves = []
    for line in get_lines(input_file):
        line = line.strip()
        if line[0] == '$':
            moves.append((line.split()[1:], []))
        else:
            moves[-1][1].append(line)
    return moves


def update_tree(tree, move):
    command, output = move
    if command[0] == 'cd':
        return change_node(tree, command[1])
    else:
        tree.update_sizes(output)
        return tree


def change_node(tree, directory):
    if directory == '/':
        return tree.get_root()
    if directory == '..':
        return tree.parent
    return tree.find_child(directory)

