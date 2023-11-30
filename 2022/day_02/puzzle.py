import os


def compute_score(data, determine_shape=False):
    '''Get the score of the battle at rock, paper, scissors
    Args:
        data (List): Strategy guide given by the elf
        determine_shape (boolean): True if the second element of each row is the result of the battle
            and not the shape played by the player

    Returns:
        int: Total score
    '''
    score = 0  # Contains score
    # Contains winning relation (A = Rock, B = Paper, C = Scissors)
    # Key win over the value
    winning_relations = {
        'A': 'C',
        'B': 'A',
        'C': 'B',
    }

    # Contains losing relation (A = Rock, B = Paper, C = Scissors)
    # Value win over the Key
    losing_relations = {
        'A': 'B',
        'B': 'C',
        'C': 'A',
    }

    for value in data:
        # Split values
        opponent, player = value.split()

        # Get shape if result is given
        if determine_shape:
            player = opponent if player == 'B' else losing_relations[
                opponent] if player == 'C' else winning_relations[opponent]

        # Add score for player's selected shape (A = 1, B = 2, C = 3)
        score += ord(player) - 64

        # Add score for battle result
        score += 3 if player == opponent else 6 if winning_relations[player] == opponent else 0

    return score


def uniform_letters(data):
    '''Uniform letter to easily compare later
    Args:
        data (List): Strategy guide given by the elf

    Returns:
        new_data (List): List with uniformed letters
    '''
    new_data = []

    for value in data:
        # Split values
        _, letter = value.split()

        # Uniform player letter with opponent letter
        letter = chr(ord(letter) - 23)
        new_data.append("{} {}".format(_, letter))

    return new_data


def read_input():
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'input.txt')

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    file.close()

    return data


if __name__ == '__main__':
    # Read file
    data = read_input()

    # Uniform input
    data = uniform_letters(data)

    # Puzzle 1
    score = compute_score(data)

    # Display solution of puzzle 1
    print("Total score of puzzle 1 is {}.".format(score))

    # Puzzle 2
    score = compute_score(data, True)

    # Display solution of puzzle 2
    print("Total score of puzzle 2 is {}.".format(score))
