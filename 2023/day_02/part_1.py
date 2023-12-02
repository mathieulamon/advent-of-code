import os


def read_input():
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'input.txt')

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    file.close()

    return data


def solve_part_1(data):
    max_red = 12
    max_green = 13
    max_blue = 14
    result = 0

    for idx, line in enumerate(data, 1):
        red_ok = True
        green_ok = True
        blue_ok = True
        res_ok = True
        set_cubes = line.split(': ')[1].split('; ')
        for cubes in set_cubes:
            for cube in cubes.split(', '):
                digits = int(''.join(list(filter(str.isdigit, cube))))
                if 'red' in cube:
                    red_ok = digits <= max_red
                elif 'green' in cube:
                    green_ok = digits <= max_green
                elif 'blue' in cube:
                    blue_ok = digits <= max_blue
            if not (red_ok and green_ok and blue_ok):
                res_ok = False
                break

        if res_ok:
            result += idx

    return result


if __name__ == '__main__':
    # Read file
    data = read_input()

    # Solve part 1
    result = solve_part_1(data)

    # Display solution of puzzle 1
    print("Result part 1 : {}".format(result))
