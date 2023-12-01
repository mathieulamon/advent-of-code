import os


def read_input():
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'input.txt')

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    file.close()

    return data


def solve_part_2(data):
    word_to_digits = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8h',
        'nine': 'n9e'
    }
    overall_sum = 0

    for line in data:
        for key, value in word_to_digits.items():
            line = line.replace(key, key + value)

        digits = list(filter(str.isdigit, line))
        overall_sum += int(digits[0] + digits[len(digits) - 1])

    return overall_sum


if __name__ == '__main__':
    # Read file
    data = read_input()

    # Solve part 1
    result = solve_part_2(data)

    # Display solution of puzzle X
    print("Result part 2 : {}".format(result))
