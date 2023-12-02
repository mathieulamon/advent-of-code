import os


def read_input():
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'input.txt')

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    file.close()

    return data


def solve_part_2(data):
    result = 0

    for line in data:
        min_red = 0
        min_green = 0
        min_blue = 0
        set_cubes = line.split(': ')[1].split('; ')
        for cubes in set_cubes:
            for cube in cubes.split(', '):
                digits = int(''.join(list(filter(str.isdigit, cube))))
                if 'red' in cube:
                    min_red = max(min_red, digits)
                elif 'green' in cube:
                    min_green = max(min_green, digits)
                elif 'blue' in cube:
                    min_blue = max(min_blue, digits)
        result += (min_red * min_green * min_blue)

    return result


if __name__ == '__main__':
    # Read file
    data = read_input()

    # Solve part 1
    result = solve_part_2(data)

    # Display solution of puzzle X
    print("Result part 2 : {}".format(result))
