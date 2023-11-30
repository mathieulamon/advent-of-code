import os

size_directories = []


def read_input():
    """ Read input data from file

    Returns:
        data (list): All the data
    """
    script_path = os.path.join(os.path.dirname(__file__))
    file_path = os.path.join(script_path, 'input.txt')

    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    file.close()

    return data


def size_by_directory(data, current_pos, depth):
    """ Get size of every directory in the structure

    Args:
        data (list): List of commands with output
        current_position (int): Position of the current command to execute
        depth (int): Depth of the current directory. Useful to come back to the root folder at the end

    Returns:
        total_sizes (int): Total sizes of directory small or equal than 100'000
    """
    # Use global dictionary to save sizes
    global size_directories

    # Some vars
    current_dir_size = 0

    while (current_pos < len(data)):
        # Get current command
        value = data[current_pos]

        if value == '$ cd ..':
            # Moves on level out : Save dir size
            size_directories.append(current_dir_size)

            # Substract 1 to depth
            depth -= 1

            # Return size and position
            return current_dir_size, current_pos, depth

        elif value.startswith('$ cd'):
            # Call recursive function
            size, current_pos, depth = size_by_directory(
                data, current_pos + 1, depth + 1)

            # When we come back, add size to current dir
            current_dir_size += size

        elif value[0].isdigit():
            # Add file to current size
            current_dir_size += int(value.split()[0])

        # Move index by one
        current_pos += 1

    # Back to the root node
    if depth > 0:
        # Moves on level out : Save dir size
        size_directories.append(current_dir_size)

        # Substract 1 to depth
        depth -= 1

        # Return size and position
        return current_dir_size, current_pos, depth


def solve_puzzle_1(data):
    """ Init function for starting backtracking

    Args:
        data (list): List of commands with output

    Returns:
        total_sizes (int): Sum of sizes of directory <= 100'000
    """
    global size_directories

    # Call recursive
    size_by_directory(data, current_pos=0, depth=0)

    # Total sizes
    total_sizes = 0

    for size in size_directories:
        total_sizes += size if size <= 100000 else 0

    return total_sizes


def solve_puzzle_2(space_needed):
    """ Find the smallest directory to remove to have enought space for the update

    Args:
        space_needed (int): Space needed for the update

    Returns:
        size (int): Size of the smallest directory to remove
    """
    global size_directories
    disk_capacity = 70000000

    sorted_size_directories = sorted(size_directories)
    space_to_gain = sorted_size_directories[-1] - \
        (disk_capacity - space_needed)

    for size in sorted_size_directories:
        if size >= space_to_gain:
            return size


if __name__ == '__main__':
    # Read input
    data = read_input()

    # Solve puzzle 1
    result = solve_puzzle_1(data)

    # Display result of puzzle 1
    print("Total sizes of directory <= 100'000 : {}.".format(result))

    # Solve puzzle 2
    result = solve_puzzle_2(30000000)

    # Display result of puzzle 2
    print("Size of the smallest directory to delete : {}.".format(result))
