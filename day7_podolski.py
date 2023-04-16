# with thanks to Bartosz Podolski

from utils import get_lines


def solve_part_a(input_file, cutoff):
    directories = get_file_system_directories(input_file)
    sum_small_directories = 0
    for _, directory in directories.items():
        if directory < cutoff:
            sum_small_directories += directory
    return sum_small_directories


def get_file_system_directories(file):
    # Create a list of directories by judging the inputs
    current_path = ""
    directories = {"/home": 0}
    for line in get_lines(file):
        line = line.split()
        if line[0] == "$":
            if line[1] == "ls":
                pass
            else:
                if line[2] == "..":
                    # Find index of last occurrence of "/" and create new string up until that index
                    current_path = current_path[:current_path.rindex("/")]
                elif line[2] == "/":
                    current_path = "/home"
                else:
                    current_path = current_path + "/" + line[2]
                    directories[current_path] = 0
        else:
            if line[0] != "dir":
                temp_path = current_path
                # Update all parent directories
                while temp_path != "":
                    directories[temp_path] += int(line[0])
                    temp_path = temp_path[:temp_path.rindex("/")]
    return directories
