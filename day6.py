def solve_part_a(data_source, data_type):
    data = get_data(data_source, data_type)
    start = 0
    end = 1
    while end <= len(data):
        if end - start == 4:
            return end
        match = find_match(data[end], data[start:end])
        if match is not None:
            start += (match + 1)
        end += 1
    return 0


def get_data(source, type):
    if type == 'file':
        with open(source) as data:
            return data.readline()
    return source


def find_match(character, data):
    for i in range(len(data) - 1, -1, -1):
        if data[i] == character:
            return i
    return None

