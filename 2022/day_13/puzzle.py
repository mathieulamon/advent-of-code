import os


def read_input():
    """ Read data from file

    Returns:
        data (list): All data
    """
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'input_2.txt')

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    file.close()

    return data


def solve_puzzle_1(data):
    """
    """
    result = 0

    for i in range(0, 2, 3):
        first_packet = eval(data[i])
        second_packet = eval(data[i+1])

        compare(first_packet, second_packet)

    return result


def compare(l1, l2):
    """ Compare two packets

    Args:
        p1 (string): First packet
        p2 (string): Second packet

    Returns:
        result (bool): True if packets are ordered
    """
    if len(l1) == 0:
        return True
    if len(l2) == 0:
        return False

    while True:
        match item_p1, item_p2:
            case int(item_p1), int(item_p2):
                if item_p1 < item_p2:
                    return True
                elif item_p1 > item_p2:
                    return False
            case isinstance(item_p1, list), isinstance(item_p2, list):
                return compare(item_p1, item_p2)


if __name__ == '__main__':
    # Read input
    data = read_input()

    # Solve puzzle 1
    result = solve_puzzle_1(data)

    # Display solution for puzzle 1
    print("Sum of indices of pairs is {}.".format(result))
