import os


def compare(n1, n2):
    """ Get max between 2 numbers

    Args:
        n1 (int): First number
        n2 (int): Second number

    Returns:
        int: -1 if n1 is the max, 1 is n2 is the max, otherwise 0
    """

    return -1 if n1 > n2 else 1 if n2 > n1 else 0


def count_contained_pairs(data):
    """ Count how many pairs are fully countains by the other in the par

    Args:
        data (list): List of camp's number to be cleaned by pair

    Returns:
        nb_pairs_contained (int): Number of fully contain pairs in the other
    """
    nb_pairs_contained = 0  # Contains nb of pairs fully contain in the other

    for value in data:
        # Split values between elf
        first_elf, second_elf = value.split(',')

        # Split upper and lower range
        first_elf_low, first_elf_up = map(int, first_elf.split('-'))
        second_elf_low, second_elf_up = map(int, second_elf.split('-'))

        # Check if one is fully contain
        c1 = compare(first_elf_low, second_elf_low)
        c2 = compare(first_elf_up, second_elf_up)

        if c1 * c2 <= 0:
            nb_pairs_contained += 1

    return nb_pairs_contained


def count_overlaped_pairs(data):
    """ Count how many pairs overlap the other

    Args:
        data (list): List of camp's number to be cleaned by pair

    Returns:
        nb_pairs_overlaped (int): Number of overlaped pairs in the other
    """
    nb_pairs_overlaped = 0  # Contains nb pairs overlaped in the other

    for value in data:
        # Split values between elf
        first_elf, second_elf = value.split(',')

        # Split upper and lower range
        first_elf_low, first_elf_up = map(int, first_elf.split('-'))
        second_elf_low, second_elf_up = map(int, second_elf.split('-'))

        # Use set to determine intersection
        # Need +1 because upper boundary is not taken in account
        s1 = set(range(first_elf_low, first_elf_up + 1))
        s2 = set(range(second_elf_low, second_elf_up + 1))

        if len(s1.intersection(s2)) > 0:
            nb_pairs_overlaped += 1

    return nb_pairs_overlaped


def read_input():
    """ Read input file containing data

    Returns:
        data (list): All data
    """
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'input.txt')

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    file.close()

    return data


if __name__ == '__main__':
    # Read input
    data = read_input()

    # Solve puzzle 1
    result = count_contained_pairs(data)

    # Display solution of puzzle 1
    print("Number of fully contain pairs in the other : {}.".format(result))

    # Solve puzzle 2
    result = count_overlaped_pairs(data)

    # Display solution of puzzle 2
    print("Number of overlaped pairs in the other : {}.".format(result))
