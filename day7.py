# with thanks to Bartosz Podolski

from utils import get_lines


def solve_part_a(input_file, cutoff):
    return sum(s for s in get_sizes(input_file) if s <= cutoff)


def get_sizes(file):
    current_path = ""
    directories = {"/home": 0}
    for line in get_lines(file):
        line = line.split()
        if line[0] == "$": # the line is a command
            if line[1] == "ls":
                pass
            else:
                if line[2] == "..":
                    # find index of last occurrence of "/" and keep everything to the left of it
                    current_path = current_path[:current_path.rindex("/")]
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
                    temp_path = temp_path[:temp_path.rindex("/")]
    return directories.values()
