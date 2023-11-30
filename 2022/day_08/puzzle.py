import numpy as np
import os


def calculate_scenic_score(data):
    """ Find better spot to build the house by calculating scenic score

    Args:
        data (list): Grid with trees height (0 shortest and 9 tallest)

    Returns:
        result (int): Scenic score from the best tree 
    """
    # Create numpy array with input data
    x = np.array(
        [[int(x) for x in data[i]] for i in range(len(data))], np.int8
    )

    # Create numpy array with values set to 0. Contains scenir score for each tree
    side_size = len(x[0])
    y = np.zeros((side_size, side_size), dtype=np.int32)

    # Need to do an addition if it's first scan for calculate score instead of multiplication
    first_scan = True

    for _ in range(4):
        # Scan rows from left to right
        for i in range(len(x)):
            # Iterate over each trees
            for j in range(len(x[i])):
                current_tree = x[i][j]
                nb_trees_visible = 0
                counter = 1
                while j - counter >= 0:
                    tree = x[i][j - counter]  # Tree to compare
                    # Next tree is visible, no matter if he's taller, smaller or equals than current
                    nb_trees_visible += 1
                    # Tree is smaller than current -> see the next one
                    if tree < current_tree:
                        counter += 1
                    else:
                        # Tree is equals or taller than current -> break
                        break

                # Calcule new scenic score
                current_score = y[i][j]
                y[i][j] = nb_trees_visible if first_scan else current_score * \
                    nb_trees_visible

        # At the end, rotate both matrices of 90°
        # So we can scan other views (up-down, right-left, down-up) with the same logic (left-right)
        x = np.rot90(x)
        y = np.rot90(y)

        # End of first scan
        first_scan = False

    # Get max value
    index_x, index_y = np.unravel_index(y.argmax(), y.shape)
    result = y[index_x][index_y]

    return result


def count_visible_trees(data):
    """ Count how many trees are visible from outside the grid

    Args:
        data (list): Grid with trees height (0 shortest and 9 tallest)

    Returns:
        result (int): Number of trees visible from outside
    """
    # Create numpy array with input data
    x = np.array(
        [[int(x) for x in data[i]] for i in range(len(data))], np.int8
    )

    # Create numpy array with false value. Contains visible trees from outside
    side_size = len(x[0])
    y = np.zeros((side_size, side_size), dtype=bool)

    for _ in range(4):
        # Scan rows from left to right
        for i in range(len(x)):
            # Keep height of the tallest tree
            tallest_tree = -1
            for j in range(len(x[i])):
                # Set tree as visible if he's taller than tallest in the row
                current_tree = x[i][j]
                if current_tree > tallest_tree:
                    y[i][j] = True
                    # Update tallest
                    tallest_tree = current_tree
        # At the end, rotate both matrices of 90°
        # So we can scan other views (up-down, right-left, down-up) with the same logic (left-right)
        x = np.rot90(x)
        y = np.rot90(y)

    # Count number of visible trees
    result = np.count_nonzero(y)

    return result


def read_input():
    """ Read input from file

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
    result = count_visible_trees(data)

    # Display result for puzzle 1
    print("Number of visible trees : {}.".format(result))

    # Solve puzzle 2
    result = calculate_scenic_score(data)

    # Display result for puzzle 2
    print("Best scenic score : {}.".format(result))
