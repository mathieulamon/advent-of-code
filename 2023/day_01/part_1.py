import os


def read_input():
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'input.txt')

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    file.close()

    return data


def solve_part_1(data):
    overall_sum = 0

    for line in data:
        digits = list(filter(str.isdigit, line))
        overall_sum += int(digits[0] + digits[len(digits) - 1])

    return overall_sum


if __name__ == '__main__':
    # Read file
    data = read_input()

    # Solve part 1
    result = solve_part_1(data)

    # Display solution of puzzle 1
    print("Result part 1 : {}".format(result))
