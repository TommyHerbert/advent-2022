# with thanks to Bartosz Podolski

from utils import get_lines


def solve_part_a(input_file, cutoff):
    return sum(s for s in get_sizes(input_file).values() if s <= cutoff)


def solve_part_b(input_file, allowance):
    sizes = get_sizes(input_file)
    overspend = sizes['/home'] - allowance
    return min([s for s in sizes.values() ])


def get_sizes(file):
    current_path = ""
    directories = {"/home": 0}
    for line in get_lines(file):
        line = line.split()
        if line[0] == "$": # the line is a command
            if line[1] != "ls":
                if line[2] == "..":
                    current_path = parent(current_path)
                elif line[2] == "/":
                    current_path = "/home"
                else:
                    current_path = current_path + "/" + line[2]
                    directories[current_path] = 0
        else: # the line is output from a command
            if line[0] != "dir":
                temp_path = current_path
                # update all parent directories
                while temp_path != "":
                    directories[temp_path] += int(line[0])
                    temp_path = parent(temp_path)
    return directories


def parent(path):
    # find index of last occurrence of "/" and keep everything to the left of it
    return path[:path.rindex('/')]
