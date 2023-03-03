from utils import get_lines


class State:
    def __init__(self):
        self.stacks = []

    def apply(self, instruction, all_at_once):
        number, source, target = instruction
        if all_at_once:
            index = number * -1
            self.stacks[target] += self.stacks[source][index:]
            self.stacks[source] = self.stacks[source][:index]
        else:
            for i in range(number):
                self.move_one(source, target)
    
    def move_one(self, source, target):
        self.stacks[target].append(self.stacks[source][-1])
        self.stacks[source] = self.stacks[source][:-1]

    def add_to_top(self, stack, crate):
        while len(self.stacks) <= stack:
            self.stacks.append([])
        self.stacks[stack].append(crate)

    def invert(self):
        for stack in self.stacks:
            stack.reverse()

    def get_top_crates_string(self):
        return ''.join([s[-1] for s in self.stacks])


def solve_part_a(path):
    return solve(path, all_at_once=False)


def solve_part_b(path):
    return solve(path, all_at_once=True)


def solve(path, all_at_once):
    state, instructions = parse(get_lines(path))
    for instruction in instructions:
        state.apply(instruction, all_at_once)
    return state.get_top_crates_string()


def parse(data):
    state = State()
    instructions = []
    for line in data:
        if line[:2] == ' 1':
            state.invert()
        elif line[0] in ' [':
            crates = parse_crates(line)
            for stack in range(len(crates)):
                crate = crates[stack]
                if crate != ' ':
                    state.add_to_top(stack, crate)
        elif line[0] == 'm':
            instructions.append(parse_instruction(line))
    return state, instructions


def parse_crates(line):
    return [line[i] for i in range(1, len(line), 4)]


def parse_instruction(line):
    tokens = line.split()

    # convert stack numbers to zero-based indexes 
    return [int(tokens[1]), int(tokens[3]) - 1, int(tokens[5]) - 1]

