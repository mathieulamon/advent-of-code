import os


def find_max_calories(data, nb_elves=1):
    '''Get the number of calories carried by the elves carrying the most calories
    Args:
        data (List): Calories by elf, separed by a blank line between elves
        nb_elves (int): Number of top elves to find max

    Returns:
        int: Sum of calories of top elves
    '''
    max_calories = []  # Contains sum of calories by elf
    counter_by_elf = 0  # Counter of current elf

    # Sum calories
    for value in data:
        if value == '':
            # Reset counter and add value for current elf
            max_calories.append(counter_by_elf)
            counter_by_elf = 0
        else:
            counter_by_elf += int(value)

    # Sort by values descending
    max_calories.sort(reverse=True)

    # Sum top n elves
    result = 0
    for i in range(0, nb_elves):
        result += max_calories[i]

    return result


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

    # Puzzle 1
    result = find_max_calories(data)

    # Display solution of puzzle 1
    print("Top elf carries {} calories.".format(result))

    # Puzzle 2
    nb_elves = 3
    result = find_max_calories(data, nb_elves)

    # Display solution of puzzle 2
    print("{} top elves carry {} calories.".format(nb_elves, result))
