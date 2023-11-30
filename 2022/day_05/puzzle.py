import os
import queue

from collections import deque
from copy import deepcopy


def split_file(data):
    """ Create initial stacks with input data
        Separate stacks from moving instructions

    Args:
        data (list): List of data containing initial disposition and instructions

    Returns:
        data (list): List of instructions
        stacks (list): List of deque
    """
    lines = []  # Contains temp lines
    stacks = []  # Contains n stacks
    counter = 0  # Define where to cut list for keeping instructions

    for value in data:
        counter += 1
        # Save line until there is a blank line
        if not value == '':
            lines.append(value)
        else:
            # Create stacks
            last_line = lines.pop()
            for i in range(len(last_line.split())):
                stack = deque()
                stacks.append(stack)

            # Cut list
            data = data[counter:]
            break

    # Reverse lines order
    lines = lines[::-1]
    for line in lines:
        for i in range(1, len(line), 4):
            if not line[i] == ' ':
                stacks[i//4].append(line[i])

    return data, stacks


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


def rearrangement(data, stacks):
    """ Execute all instructions and move crates
        Move all crates one by one if multiples

    Args:
        data (list): List of instructions
        stacks (list): List of deque

    Returns:
        message (string): Message to give to elves
    """
    for value in data:
        # Split to get information
        splited_value = value.split()
        number_to_move = int(splited_value[1])
        move_from = int(splited_value[3]) - 1
        move_to = int(splited_value[5]) - 1

        # Move
        for i in range(0, number_to_move):
            if stacks[move_from]:
                x = stacks[move_from].pop()
                stacks[move_to].append(x)

    # Retrive message
    message = ''.join(stacks[i].pop() for i in range(len(stacks)))

    return message


def rearrangement_bloc(data, stacks):
    """ Execute all instructions and move crates
        Keep original order if moving multiples crates

    Args:
        data (list): List of instructions
        stacks (list): List of deque

    Returns:
        message (string): Message to give to elves
    """
    for value in data:
        # Split to get information
        splited_value = value.split()
        number_to_move = int(splited_value[1])
        move_from = int(splited_value[3]) - 1
        move_to = int(splited_value[5]) - 1

        # Save all number in a temporary queue for saving order
        temp_queue = queue.LifoQueue()
        for i in range(0, number_to_move):
            if stacks[move_from]:
                x = stacks[move_from].pop()
                temp_queue.put(x)

        # Put in the destination
        while not temp_queue.empty():
            stacks[move_to].append(temp_queue.get())

    # Retrive message
    message = ''.join(stacks[i].pop() for i in range(len(stacks)))

    return message


if __name__ == '__main__':
    # Read input
    data = read_input()

    # Create initial stacks from model in input
    # Split stacks from instructions
    data, stacks = split_file(data)

    # Backup for puzzle 2
    backup_stacks = deepcopy(stacks)

    # Solve puzzle 1
    message = rearrangement(data, stacks)

    # Display solution of puzzle 1
    print("The message is : {}.".format(message))

    # Solve puzzle 2
    message = rearrangement_bloc(data, backup_stacks)

    # Display solution of puzzle 2
    print("The message is : {}.".format(message))
