import numpy as np
import os
import sys


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tuple(self):
        return (self.x, self.y)


def parse_data(data):
    """ Transform data into numpy array (int)

    Args:
        data (list): List of input data (string)

    Returns:
        new_array (np.array): Array of int containing height of points
        visited (np.array): Array of visited points
        starting_point (Point): Starting point
        ending_point (Point): Ending point
    """
    # Look for starting and ending point
    for i in range(len(data)):
        index_s = data[i].find('S')
        index_e = data[i].find('E')
        if index_s >= 0:
            starting_point = Point(index_s, i)
            data[i] = data[i].replace('S', 'a')
        if index_e >= 0:
            ending_point = Point(index_e, i)
            data[i] = data[i].replace('E', 'z')

    # Create numpy array with input data
    new_array = np.array(
        [[ord(x) - 97 for x in data[i]] for i in range(len(data))], np.int8
    )

    # Save visited points
    visited = np.zeros((len(new_array), len(new_array[0])), dtype=bool)

    return new_array, visited, starting_point, ending_point


def read_input():
    """ Read data from file

    Returns:
        data (list): All data
    """
    script_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_path, 'input.txt')

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    file.close()

    return data


def solve_puzzle_1(data):
    """ Get shortest path between source and destination
        A move need to have a difference of height of 0 or 1

    Args:
        data (list): Height of all points

    Returns:
        result (int): Length of the shortest path
    """
    # Parse data
    array, visited, start_point, end_point = parse_data(data)

    # Start at the end and come back
    result, _ = min_path(array, visited, end_point, start_point, 'None')

    print(result)


def min_path(array, visited, current_point, end_point, last_move):
    """ Recursive method to find shortest path between starting point and ending point

    Args:
        array (np.array): Array of heights
        visited (np.arry): Array of visited points
        current_point (Point): Current point
        end_point (Point): Point to reach
        last_move (string): Direction of the last move
    """
    # Get current values
    x = current_point.x
    y = current_point.y

    if x == end_point.x and y == end_point.y:
        # Final case : The end point is reached
        visited[y][x] = False
        return 0, visited

    visited[y][x] = True

    # Axis length
    x_len = len(array[0])
    y_len = len(array)

    # Keep distances
    distances = []

    # Compute distances of every 4-neighbours if rules are ok
    if x + 1 < x_len and (array[y][x] - array[y][x + 1] == 1 or array[y][x] - array[y][x + 1] == 0) and not visited[y][x + 1] and not last_move == 'left':
        # Move right
        current_point.x += 1

        distance, visited = min_path(
            array, visited, current_point, end_point, 'right')

        distances.append(distance)
        current_point.x -= 1

    if x - 1 >= 0 and (array[y][x] - array[y][x - 1] == 1 or array[y][x] - array[y][x - 1] == 0) and not visited[y][x - 1] and not last_move == 'right':
        # Move left
        current_point.x -= 1

        distance, visited = min_path(
            array, visited, current_point, end_point, 'left')

        distances.append(distance)
        current_point.x += 1

    if y + 1 < y_len and (array[y][x] - array[y + 1][x] == 1 or array[y][x] - array[y + 1][x] == 0) and not visited[y + 1][x] and not last_move == 'down':
        # Move up
        current_point.y += 1

        distance, visited = min_path(
            array, visited, current_point, end_point, 'up')

        distances.append(distance)
        current_point.y -= 1

    if y - 1 >= 0 and (array[y][x] - array[y - 1][x] == 1 or array[y][x] - array[y - 1][x] == 0) and not visited[y - 1][x] and not last_move == 'up':
        # Move down
        current_point.y -= 1

        distance, visited = min_path(
            array, visited, current_point, end_point, 'down')

        distances.append(distance)
        current_point.y += 1

    # Return max_value if distance is empty ("cul de sac")
    visited[y][x] = False
    if len(distances) == 0:
        return sys.maxsize, visited

    return min(distances) + 1, visited


if __name__ == '__main__':
    # Read input
    data = read_input()

    # Solve puzzle 1
    result = solve_puzzle_1(data)
