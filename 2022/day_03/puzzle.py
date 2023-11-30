import os


def compute_score(intersection):
    """ Compute score for an intersection set

    Args:
        intersection (set): Set of letters to compute score

    Returns:
        int: Score for this intersection set
    """
    score = 0
    for letter in intersection:
        score += ord(letter) - 38 if letter.isupper() else ord(letter) - 96

    return score


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


def reorganize(data):
    """ Get the score of the priorities item types in the rucksacks

    Args:
        data (list): List of rucksacks given by the elves

    Returns:
        int: Total score
    """
    # Contains score
    score = 0

    for value in data:
        # Break string in two half
        string_len = len(value)

        # Use set de determine intersection between strings
        first_half = set(value[:string_len//2])
        second_half = set(value[string_len//2:])
        intersection = first_half.intersection(second_half)

        # Calculate score
        score += compute_score(intersection)

    return score


def reorganize_safety(data):
    """ Get the score of the priorites item types in the rucksacks
        Add safety by taking the item type that appear in all three rucksacks

    Args:
        data (list): List of rucksacks given by the elves

    Returns:
        int: Total score
    """
    score = 0  # Contains score
    size_list = len(data)  # Use to loop boundary

    for i in range(0, size_list, 3):
        # Intersection between 3 sets
        temp_intersection = set(data[i]).intersection(set(data[i+1]))
        intersection = temp_intersection.intersection(set(data[i+2]))

        # Calculate score
        score += compute_score(intersection)

    return score


if __name__ == '__main__':
    # Read input
    data = read_input()

    # Solve puzzle 1
    score = reorganize(data)

    # Display solution of puzzle 1
    print("Puzzle 2 : Sum of priorites of those items is {}.".format(score))

    # Solve puzzle 2
    score = reorganize_safety(data)

    # Display solution of puzzle 2
    print("Puzzle 1 : Sum of priorites of those items is {}.".format(score))
