import os


def find_marker(data, nb_char):
    """ Find x unique caracters to determine the start of the communication

    Args:
        data (string): Signal to process
        nb_char (int): Number of unique char needed

    Returns:
        int: Index of the characters where the communication start
    """
    for i in range(len(data)):
        substring_set = set(data[i:i+nb_char])
        if len(substring_set) == nb_char:
            # Marker found
            return i + nb_char


def read_input():
    """ Read input file containing data

    Returns:
        data (string): Signal
    """
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'input.txt')

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    file.close()

    return data[0]


if __name__ == '__main__':
    # Read input
    data = read_input()

    # Solve puzzle 1
    result = find_marker(data, 4)

    # Display result of puzzle 1
    print("Marker found after {} caracters.".format(result))

    # Solve puzzle 2
    result = find_marker(data, 14)

    # Display result of puzzle 2
    print("Marker found after {} caracters.".format(result))
